import math
import json
import time
import datetime
import transaction
import pyramid.httpexceptions as exceptions
from pyramid import testing
from pyramid.testing import DummyRequest
from pyramid.httpexceptions import HTTPBadRequest
from sqlalchemy import create_engine
from game_of_life import TIME_DELAY
from projectconway import project_config
from projectconway.views.create import create_view
from projectconway.views.create import pattern_input_receiver_JSON
from projectconway.views.create import pattern_input_clearer_JSON
from projectconway.views.create import time_slot_reciever_JSON
from projectconway.views.create import confirmation_receiver_JSON
from projectconway.models import Base, DBSession
from projectconway.models.run import Run

def create_input_pattern():
    '''
    Create an initial input to represent the data being saved
    to the database.
    '''
    return """\
-*-*-*-*-*
*-*-*-*-*-
-*--------
--*-------
---*------
----*-----
-----*----
*-*-*-*-*-
-*-*-*-*-*
*-*-*-*-*-"""


class TestPatternInput(object):
    '''
    Tests all of the views linked to the Pattern Input web page.
    '''

    def test_create(self):
        '''
        Tests the pattern input view, emulating when the user is visiting
        the page for the first time and there is currently no pattern
        waiting in the session.
        '''
        request = DummyRequest(route='/create')

        response = create_view(request)

        # Test there was a response
        assert response

        # Test the correct presentational values are returned
        assert response["page"] == "patternpage"
        assert response["title"] == "Create Pattern"
        assert "pattern" not in response.keys()

    def test_pattern_input_view_pattern(self):
        '''
        Tests the pattern input view, emulating when the user is re-visiting
        the page and a pattern they have already created is waiting for them
        in the session.
        '''
        request = DummyRequest(route='/create')
        input = create_input_pattern()
        request.session["pattern"] = input

        response = create_view(request)

        # Test there was a response
        assert response

        # Test the correct presentational values are returned
        assert response["page"] == "patternpage"
        assert response["title"] == "Create Pattern"
        assert response["pattern"] == input.replace('\n', "\\n")

    def test_pattern_input_receiver_JSON(self):
        '''
        Tests the JSON receiver view linked to the Pattern Input web page.
        '''
        # Setup
        request = DummyRequest(route='/pattern_receiver.json')
        input = create_input_pattern()
        request.body = json.dumps(input)
        request.content_type = "application/json"

        request.json_body = input

        response = pattern_input_receiver_JSON(request)

        # Test correct input has been given to session
        assert request.session["pattern"] == input

        responseDict = response
        # Test correct number of turns has passed
        assert responseDict["turns"] == 53

        # Test correct time has been calculated
        assert responseDict["runtime"] == TIME_DELAY * 53
    
    def test_pattern_clearer_JSON(self):
        '''
        Tests the JSON clearer view linked to the Pattern Input web page.
        '''
        # Setup
        request = DummyRequest(route='/pattern_clearer.json')
        input = create_input_pattern()
        request.body = json.dumps(input)
        request.content_type = "application/json"
        
        request.json_body = input
        request.session["pattern"] = input
        
        # Test input has been removed from session
        response = pattern_input_clearer_JSON(request)
        assert "pattern" not in response.keys()


class TestScheduler(object):
    """
    This object contains a group of unit tests that test
    pyramid views that associated with the time_slot views
    """

    def setup_class(self):
        '''
        Setup data that will be needed throughout the class and setup database
        '''
        self.config = testing.setUp()
        engine = create_engine('sqlite:///testdb.sqlite')
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)

    def test_time_slot_reciever_JSON(self):
        """
        This test will attempt to request minutes for a successful
        time slot
        """
        request = DummyRequest(route='/scheduler.json')

        if project_config["start_date"]:
            input_date = datetime.datetime.combine(project_config["start_date"], datetime.time())
        else:
            input_date = datetime.datetime.today() + datetime.timedelta(days=1)

        user_input = int(time.mktime(input_date.timetuple()) * 1000)

        request.content_type = "application/json"
        request.POST["date"] = str(user_input)

        response = time_slot_reciever_JSON(request)

        # ensure a response is given
        assert response

        # Test the response
        response_dict = eval(str(response))

        no_of_hours = math.ceil(((project_config["closing_time"].hour*60 + project_config["closing_time"].minute) -
                                (project_config["starting_time"].hour*60 + project_config["starting_time"].minute)) / 60)
        assert len(response_dict["hours"]) == no_of_hours

    def test_time_slot_receiver_JSON_timestring_failure(self):
        """
        This method will test the functionality of the time_slot_receiver_JSON view. The expected result of this test
        is for the view to catch an error because the timestring for which the time_slot should be retrieved is in the
        wrong format.
        """
        # Set up a dummy request for testing poor formatting of the timestring
        request = DummyRequest(route='/sheduler.json')
        request.POST["date"] = datetime.datetime.now()

        # Assert that an exception is thrown due to the timestring not being formatted correctly
        try:
            response = time_slot_reciever_JSON(request)
        except HTTPBadRequest as e:
            assert e.args[0] == "Timestring was not formatted correctly!"

    def test_time_slot_receiver_JSON_runs(self):
        """
        This test will attempt to request minutes for a successful
        time slot. This tests ensures that there are runs in the database and ensures
        the correct slots are returned
        """
        request = DummyRequest(route='/scheduler.json')

        if project_config["start_date"]:
            input_date = datetime.datetime.combine(project_config["start_date"], datetime.time())
        else:
            input_date = datetime.datetime.today() + datetime.timedelta(hours=1)

        user_input = int(time.mktime(input_date.timetuple()) * 1000)

        request.content_type = "application/json"
        request.POST["date"] = str(user_input)

        # Insert runs that will the next hour with even minutes that are a multiple of 10
        with transaction.manager:
            runs = []
            for minutes in range(0, 60, 10):
                runs.append(Run(create_input_pattern(), datetime.datetime(input_date.year, input_date.month,
                                                                          input_date.day, input_date.hour, minutes), ""))
            DBSession.add_all(runs)
            DBSession.commit()

        response = time_slot_reciever_JSON(request)

        # ensure a response is given
        assert response

        # Test the response
        response_dict = eval(str(response))
        for min in range(0, 60, 10):
            assert min not in response_dict[input_date.hour]

    def teardown_class(self):
        '''
        Closes database session once the class is redundant
        '''
        with transaction.manager:
            for run in DBSession.query(Run).all():
                DBSession.delete(run)
            DBSession.commit()

        DBSession.remove()
        testing.tearDown()


class TestConfirmation(object):
    """
    This object contains a group of unit tests that test
    pyramid views associated with confirming the user's information
    in the database
    """

    def setup_class(self):
        '''
        Setup data that will be needed throughout the class and setup database
        '''
        self.config = testing.setUp()
        engine = create_engine('sqlite:///testdb.sqlite')
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)

    def test_confirmation_receiver_JSON(self):
        """
        This tests that the content of a session can successfully
        be added to the database.
        """
        request = DummyRequest(route='/confirm.json')

        # create a pattern to be saved to the database
        request.session["pattern"] = create_input_pattern()
        # create a time and date to be saved for the pattern on the database
        time = datetime.datetime.now().replace(minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
        request.session["viewing_date"] = time.strftime("%d/%m/%Y")
        request.session["viewing_hour"] = time.strftime("%H")
        request.session["viewing_slot"] = time.strftime("%M")

        response_dict = confirmation_receiver_JSON(request)

        # Test response has arrived
        assert response_dict
        assert response_dict["success"]

        # Test session has been saved to database
        assert Run.get_run_for_time_slot(time)

        # Test session has been emptied
        assert not "pattern" in request.session

        assert not "viewing_date" in request.session
        assert not "viewing_hour" in request.session
        assert not "viewing_slot" in request.session

    def test_confirmation_receiver_JSON_failure(self):
        """
        This tests that the confirmation logic recognises when a
        session has already been added to the database and fails
        to be added again.
        """
        # Add pattern and time to database
        time = datetime.datetime.now().replace(minute=5, second=0, microsecond=0) + datetime.timedelta(days=1)
        with transaction.manager:
            DBSession.add(Run(create_input_pattern(), time, ""))
            DBSession.commit

        # Set up request
        request = DummyRequest(route='/confirm.json')
        request.session["pattern"] = create_input_pattern()
        request.session["viewing_date"] = time.strftime("%d/%m/%Y")
        request.session["viewing_hour"] = time.strftime("%H")
        request.session["viewing_slot"] = time.strftime("%M")

        response_dict = confirmation_receiver_JSON(request)

        # Test response has arrived
        assert response_dict
        assert not response_dict["success"]
        assert response_dict["failure_message"]

        # Test session still exists
        assert not "pattern" in request.session
        assert not "viewing_date" in request.session
        assert not "viewing_hour" in request.session
        assert not "viewing_slot" in request.session

    def teardown_class(self):
        '''
        Closes database session once the class is redundant
        '''
        with transaction.manager:
            for run in DBSession.query(Run).all():
                DBSession.delete(run)
            DBSession.commit()

        DBSession.remove()
        testing.tearDown()
