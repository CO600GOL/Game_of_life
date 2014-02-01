from pyramid.view import view_config
from game_of_life import TIME_LIMIT, TIME_DELAY
from game.game_controllers.game_controllers import GameOfLifeController

@view_config(route_name='pattern_input', renderer="projectconway:templates/pattern_input.mako")
def pattern_input_view(request):
    '''
    Executes the logic for the Pattern Input web page, allowing the user
    to input a pattern to the website - the application must then input
    that pattern to a session for persistance across pages.

    The method also checks for a pattern already existing in the session, so
    that the user can go back and edit it at any point.
    '''

    data = {'title': 'Create Pattern',
            'page': 'patternpage'}

    # Work out if a pattern is already in the session
    if 'pattern' in request.session:
        data['pattern'] = request.session['pattern'].replace('\n', "\\n")

    return data


@view_config(route_name="pattern_input_receiver", renderer='json')
def pattern_input_receiver_JSON(request):
    '''
    This view receives a customers pattern input in the form of a JSON 
    string. We then run a gameoflife for that pattern and return the number 
    of seconds and turns it will run for, taking into consideration the 5 minute
    run time and delays. 
    '''
    # Retrieve pattern from request
    pattern = request.json_body
    request.session["pattern"] = pattern

    golcontroller = GameOfLifeController()
    golcontroller.set_up_game(pattern)

    while(golcontroller.get_turn_count() < (TIME_LIMIT / TIME_DELAY) and not
          golcontroller.get_game().is_game_forsaken()):
        golcontroller.play_next_turn()


    return {"turns": golcontroller.get_turn_count(),
            "runtime": golcontroller.get_turn_count() * TIME_DELAY}
