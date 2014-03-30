"""
This module contains logic for the pattern creation process, in which the user creates a pattern, schedules a date and
time at which to go and see the pattern run on the display and then confirms the information to the server-side
database.
"""

from datetime import datetime
from pyramid.httpexceptions import HTTPBadRequest, HTTPFound
from pyramid.view import view_config
from sqlalchemy.exc import ArgumentError
from projectconway import project_config
from projectconway.lib.exceptions import RunSlotTakenError, RunSlotInvalidError
from projectconway.models.run import Run
from game_of_life import TIME_LIMIT, SLEEP_TIME
from game.game_controllers.game_controllers import GameOfLifeController


@view_config(route_name='create', renderer="pattern_input.mako")
def create_view(request):
    """
    This function executes the logic for the pattern creation process, making sure that the user is always on the
    correct page for the process. This means if the user visits a different page, when they return, none of their
    information will be lost.

    @param request The request sent to this page of the web application.
    """

    # If they have refreshed the confirmation page after submitting, redirect them to the pattern create page
    if "confirmed" in request.session.keys():
        request.session.invalidate()
        return HTTPFound(request.route_url('create'))

    data = {}
    data["page"] = "patternpage"
    page_keys = [
        "pattern_input",
        "scheduler",
        "confirmation"
    ]
    pages = {
        page_keys[0]: "pattern_input.mako",
        page_keys[1]: "scheduler.mako",
        page_keys[2]: "confirmation.mako"
    }

    page = ""
    if "create_page" in request.POST:
        req_page = request.POST["create_page"]
        if req_page in pages:
            page = req_page
    elif "create_page" in request.session:
        page = request.session["create_page"]
    if not page:
        page = page_keys[0]
    request.override_renderer = pages[page]

    # scheduler page
    if page == page_keys[1]:
        request.session["create_page"] = page_keys[1]
        data["title"] = "Scheduler"

        if "viewing_date" in request.session:
            viewing_date = request.session["viewing_date"]
        else:
            viewing_date = datetime.today().strftime("%d/%m/%Y")
        data["viewing_date"] = viewing_date

        if "viewing_hour" in request.session:
            viewing_hour = request.session["viewing_hour"]
        else:
            viewing_hour = datetime.now().hour
        data["viewing_hour"] = viewing_hour

        if "viewing_slot" in request.session:
            viewing_slot = request.session["viewing_slot"]
        else:
            viewing_slot = 0
        data["viewing_slot"] = viewing_slot

    # confirmation page
    elif page == page_keys[2]:
        request.session["create_page"] = page_keys[2]
        data["title"] = "Confirmation"

        # Assign mako date variable
        if "viewing_date" in request.POST:
            date = request.POST["viewing_date"]
        elif "viewing_date" in request.session:
            date = request.session["viewing_date"]
        else:
            raise ArgumentError("Viewing date was not submitted")

        # Format date
        try:
            viewing_date = datetime.strptime(date, "%d/%m/%Y")

            # Day suffix
            if 4 <= viewing_date.day <= 20 or 24 <= viewing_date.day <= 30:
                suffix = "th"
            else:
                suffix = ["st", "nd", "rd"][viewing_date.day % 10 - 1]

            data["viewing_date"] = viewing_date.strftime("%A %d" + suffix + " %B %Y")
            request.session["viewing_date"] = date
        except:
            raise ArgumentError("Viewing date incorrectly formatted")

        # Assign mako viewing hour variable
        if "viewing_hour" in request.POST:
            viewing_hour = request.POST["viewing_hour"]
        elif "viewing_hour" in request.session:
            viewing_hour = request.session["viewing_hour"]
        else:
            raise ArgumentError("Viewing hour was not submitted")
        data["viewing_hour"] = viewing_hour
        request.session["viewing_hour"] = viewing_hour

        # Assign make viewing slot variable
        if "viewing_slot" in request.POST:
            viewing_slot = request.POST["viewing_slot"]
        elif "viewing_slot" in request.session:
            viewing_slot = request.session["viewing_slot"]
        else:
            raise ArgumentError("Viewing slot was not submitted")
        data["viewing_slot"] = viewing_slot
        request.session["viewing_slot"] = viewing_slot

        data["display_address"] = project_config["display_address"]

    # pattern input page
    else:
        request.session["create_page"] = page_keys[0]
        data["title"] = "Create Pattern"

    # Work out if a pattern is already in the session
    if 'pattern' in request.session:
        data['pattern'] = request.session['pattern'].replace('\n', "\\n")

    return data


@view_config(route_name="pattern_input_receiver", renderer='json')
def pattern_input_receiver_JSON(request):
    """
     This function executes the logic for calculating how many generations a user's pattern will survive for and, while
     taking into consideration the delay set to each generation, for how many seconds it will run.

     @param request The request sent to this page of the web application.
    """
    # Retrieve pattern from request
    pattern = request.json_body
    request.session["pattern"] = pattern

    golcontroller = GameOfLifeController()
    golcontroller.set_up_game(pattern)

    while(golcontroller.get_turn_count() < (TIME_LIMIT / SLEEP_TIME) and not
          golcontroller.get_game().is_game_forsaken()):
        golcontroller.play_next_turn()


    return {"turns": golcontroller.get_turn_count(),
            "runtime": golcontroller.get_turn_count() * SLEEP_TIME}


@view_config(route_name="pattern_input_clearer", renderer='json')
def pattern_input_clearer_JSON(request):
    '''
    This view receives a user's pattern input in the form of a JSON string and
    removes it from the session.
    '''
    if 'pattern' in request.session:
        del request.session["pattern"]
    return request.session


@view_config(route_name="time_slot_receiver", renderer='json')
def time_slot_reciever_JSON(request):
    """
    This function executes the logic for validating a person's chosen time slot and adding it to the web session
    should it be.

    @param request The request sent to this page of the web application.
    """
    # Get possible time slots for a given day
    request_time = request.POST["date"]
    try:
        request_time = float(request_time[:10])
        time_slot = datetime.fromtimestamp(request_time).date()
    except:
        raise HTTPBadRequest("Timestring was not formatted correctly!")

    aval_slots = Run.get_time_slots_for_day(time_slot, datetime.now())

    # Render the possible runs times in json
    # in the format:
    # {"hours": [2, 3, 4, 5, 6],
    #  2: [0, 5, 15, 25],
    #  3: [5, 25, 45]
    #  ... }
    response_dict = {}
    hours = set()

    for slot in aval_slots:
        hour = slot.hour
        hours.add(hour)

        if hour not in response_dict:
            response_dict[hour] = []
        response_dict[hour] = response_dict[hour] + [slot.minute]

    response_dict["hours"] = list(hours)

    return response_dict


@view_config(route_name="confirmation_receiver", renderer='conway_json')
def confirmation_receiver_JSON(request):
    """
    This function executes the logic for sending the user's information to the server-side database, clearing the
    session if successful. If it is not successful, it will tell the user what the issue was and give them a possible
    way to get around it.

    @param request The request sent to this page of the web application.
    """
    # Response dict
    data = {
        "success": False
    }

    # Get the information out of the session
    try:
        pattern = request.session["pattern"]
        viewing_date = request.session["viewing_date"]
        viewing_hour = request.session["viewing_hour"]
        viewing_slot = request.session["viewing_slot"]
        viewing_time = "%s-%s-%s" % (viewing_date, viewing_hour, viewing_slot)
    except KeyError:
        raise HTTPBadRequest("Session Timeout")
    finally:
        request.session.invalidate()
        request.session["confirmed"] = True

    time_slot = datetime.strptime(viewing_time, "%d/%m/%Y-%H-%M")

    # Insert run
    try:
        Run.insert_run(pattern, time_slot)
    except RunSlotTakenError:
        data["failure_message"] = "I'm afraid your time slot is taken! Feel free to try another."
    else:
        data["success"] = True

    return data