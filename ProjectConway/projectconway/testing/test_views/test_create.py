import os
import json
import datetime
import transaction
import pyramid.httpexceptions as exceptions
from pyramid import testing
from pyramid.testing import DummyRequest
from sqlalchemy import create_engine
from game_of_life import TIME_DELAY
from projectconway.views.create import create_view
from projectconway.views.create import pattern_input_receiver_JSON
from projectconway.views.create import pattern_input_clearer_JSON
from projectconway.views.create import time_slot_reciever_JSON
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

    def test_time_slot_reciever_JSON_in_past(self):
        """
        This test will attempt to request minutes for a time slot
        from the past, this should fail.
        """
        request = DummyRequest(route='/scheduler.json')

        past = datetime.datetime.today() - datetime.timedelta(days=1, hours=1)
        user_input = {
            "date": past.isoformat(),
            "hour": past.hour
        }
        request.content_type = "application/json"

        request.json_body = json.dumps(user_input)

        try:
            response = time_slot_reciever_JSON(request)
        except exceptions.HTTPBadRequest:
            pass
        else:
            raise Exception("View did not return a HTTPBadRequest due to request from the past")

    def test_time_slot_reciever_JSON(self):
        """
        This test will attempt to request minutes for a successful
        time slot
        """
        request = DummyRequest(route='/scheduler.json')

        now = datetime.datetime.today() + datetime.timedelta(hours=1)
        user_input = {
            "date": now.isoformat(),
            "hour": now.hour
        }
        request.content_type = "application/json"

        request.json_body = json.dumps(user_input)

        response = time_slot_reciever_JSON(request)

        # ensure a response is given
        assert response

        # Test the response
        response_dict = json.loads(response)
        slots = response_dict["time_slots"]

        assert len(slots) == 12
        assert slots == [format(i, "02d") for i in range(0, 60, 5)]

    def test_time_slot_reciever_JSON_runs(self):
        """
        This test will attempt to request minutes for a successful
        time slot. This tests ensures that there are runs in the database and ensures
        the correct slots are returned
        """
        request = DummyRequest(route='/scheduler.json')

        now = datetime.datetime.today() + datetime.timedelta(hours=1)
        user_input = {
            "date": now.isoformat(),
            "hour": now.hour
        }
        request.content_type = "application/json"

        request.json_body = json.dumps(user_input)

        # Insert runs that will the next hour with even minutes that are a multiple of 10
        with transaction.manager:
            runs = []
            for minutes in range(0, 60, 10):
                runs.append(Run(create_input_pattern(), datetime.datetime(1975, 1, 1, now.hour, minutes), ""))
            DBSession.add_all(runs)
            DBSession.commit()

        response = time_slot_reciever_JSON(request)

        # ensure a response is given
        assert response

        # Test the response
        response_dict = json.loads(response)
        slots = response_dict["time_slots"]

        assert len(slots) == 6
        assert slots == [format(i, "02d") for i in range(5, 60, 10)]

    def test_time_slot_reciever_JSON_too_far(self):
        """
        This test will attempt to request minutes for a time slot
        from too far in the future
        """
        request = DummyRequest(route='/scheduler.json')

        future = datetime.datetime.today() + datetime.timedelta(weeks=13)
        user_input = {
            "date": future.isoformat(),
            "hour": future.hour
        }
        request.content_type = "application/json"

        request.json_body = json.dumps(user_input)

        try:
            response = time_slot_reciever_JSON(request)
        except exceptions.HTTPBadRequest:
            pass
        else:
            raise Exception("View did not return a HTTPBadRequest due to request from the future")

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