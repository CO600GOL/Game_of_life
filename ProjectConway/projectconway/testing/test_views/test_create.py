"""
This module contains logic for testing the pattern creation process, which is made up of three things; the input
pattern page, the scheduling page and the confirmation page. These tests must evaluate that a user's data can be
transferred across the three pages, and that it is sent to the server-side database when the user confirms the data
is correct.
"""

import math
import json
import time
import datetime
import transaction
import pyramid.httpexceptions as exceptions
from pyramid import testing
from pyramid.testing import DummyRequest
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
    """
    This function creates a string-formatted pattern for the Game of Life that can act as a user's initial input.

    @return A GoL pattern to use as a user's initial input.
    """
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
    """
    This class tests the functionality of the input pattern page, testing that a pattern can be input, cleared and
    stored.
    """

    def test_create(self):
        """
        This method tests the pattern input view, emulating a user visiting the create pattern page for the first time.
        At this point, there is no pattern waiting in the session. The expected result of this test is for the user's
        pattern and page information to be correctly stored.
        """
        request = DummyRequest(route='/create')

        response = create_view(request)

        # Assert that a response was received.
        assert response

        # Assert that the response contains the correct data for this point of the process.
        assert response["page"] == "patternpage"
        assert response["title"] == "Create Pattern"
        assert "pattern" not in response.keys()

    def test_pattern_input_view_pattern(self):
        """
        This method the pattern input view, emulating when a user is revisiting the create pattern page and a pattern
        they have already created is waiting for them in the session. The expected result of this test is for the
        changes the user makes on this page to be correctly stored.
        """
        request = DummyRequest(route='/create')
        input = create_input_pattern()
        request.session["pattern"] = input

        response = create_view(request)

        # Assert that a response has been received.
        assert response

        # Assert that the response contains the correct data for this point in the process.
        assert response["page"] == "patternpage"
        assert response["title"] == "Create Pattern"
        assert response["pattern"] == input.replace('\n', "\\n")

    def test_pattern_input_receiver_JSON(self):
        """
        This method tests the JSON receiver view linked to the pattern input page. The expected result of this test
        is for the correct JSON response to be retrieved.
        """
        # Setup
        request = DummyRequest(route='/pattern_receiver.json')
        input = create_input_pattern()
        request.body = json.dumps(input)
        request.content_type = "application/json"

        request.json_body = input

        response = pattern_input_receiver_JSON(request)

        # Assert that there is a pattern in the session.
        assert request.session["pattern"] == input

        responseDict = response
        # Assert that the correct number of turns has been calculated and stored.
        assert responseDict["turns"] == 53

        # Assert that the correct run time has been calculated and stored.
        assert responseDict["runtime"] == TIME_DELAY * 53
    
    def test_pattern_clearer_JSON(self):
        """
        This method tests the JSON clearer view linked to the pattern input page. The expected result of this test
        is for the correct JSON response to be retrieved.
        """
        # Setup
        request = DummyRequest(route='/pattern_clearer.json')
        input = create_input_pattern()
        request.body = json.dumps(input)
        request.content_type = "application/json"
        
        request.json_body = input
        request.session["pattern"] = input

        response = pattern_input_clearer_JSON(request)
        # Assert that the pattern has been removed from the session
        assert "pattern" not in response.keys()


class TestScheduler(object):
    """
    This class tests the functionality of the scheduler page, testing that a time slot can be input, changed and stored.
    """

    def setup_class(self):
        """
        This method sets up the testing logic, storing shared data that will be used for mulitple tests.
        """
        self.config = testing.setUp()
        engine = create_engine('sqlite:///testdb.sqlite')
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)

    # def test_time_slot_reciever_JSON_in_past(self):
    #     """
    #     This test will attempt to request minutes for a time slot
    #     from the past, this should fail.
    #     """
    #     request = DummyRequest(route='/scheduler.json')
    #
    #     past = datetime.datetime.today() - datetime.timedelta(days=1)
    #
    #     user_input = int(time.mktime(past.timetuple()) * 1000)
    #     request.content_type = "application/json"
    #
    #     request.POST["date"] = str(user_input)
    #
    #     try:
    #         time_slot_reciever_JSON(request)
    #     except exceptions.HTTPBadRequest:
    #         pass
    #     else:
    #         raise Exception("View did not return a HTTPBadRequest due to request from the past")

    def test_time_slot_reciever_JSON(self):
        """
        This method will test the time slot receiver JSON view of the scheduling page. The expected result of this test
        is for the correct JSON response to be retrieved.
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

        # Assert that a response has been retrieved.
        assert response

        response_dict = eval(str(response))

        no_of_hours = math.ceil(((project_config["closing_time"].hour*60 + project_config["closing_time"].minute) -
                                (project_config["starting_time"].hour*60 + project_config["starting_time"].minute)) / 60)
        # Assert the response holds the correct data.
        assert len(response_dict["hours"]) == no_of_hours

    def test_time_slot_receiver_JSON_runs(self):
        """
        This method tests the time slot receiver JSON view when there are runs in the server-side database. The
        expected result of this pattern is for the correct JSON response to be retrieved.
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

        # Assert that a response has been received.
        assert response

        response_dict = eval(str(response))
        for min in range(0, 60, 10):
            # Assert that the given slot is not in the response (means there is a run at this point)
            assert min not in response_dict[input_date.hour]

    # def test_time_slot_reciever_JSON_too_far(self):
    #     """
    #     This test will attempt to request minutes for a time slot
    #     from too far in the future
    #     """
    #     request = DummyRequest(route='/scheduler.json')
    #
    #     future = datetime.datetime.today() + datetime.timedelta(weeks=100)
    #     user_input = int(time.mktime(future.timetuple()) * 1000)
    #     request.content_type = "application/json"
    #
    #     request.POST["date"] = str(user_input)
    #
    #     try:
    #         time_slot_reciever_JSON(request)
    #     except exceptions.HTTPBadRequest:
    #         pass
    #     else:
    #         raise Exception("View did not return a HTTPBadRequest due to request from the future")

    def teardown_class(self):
        """
        This method tears down the testing logic to ensure that no data remains after testing that shouldn't. In this
        case, it closes the database session.
        """
        with transaction.manager:
            for run in DBSession.query(Run).all():
                # Delete every run in the session.
                DBSession.delete(run)
            DBSession.commit()

        # Close the session.
        DBSession.remove()
        testing.tearDown()


class TestConfirmation(object):
    """
    This class tests the functionality of the confirmation page, testing that a user's data can be persistently stored
    to the server-side database.
    """

    def setup_class(self):
        """
        This method sets up the class for testing, storing shared that data that will be used in multiple tests.
        """
        self.config = testing.setUp()
        engine = create_engine('sqlite:///testdb.sqlite')
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)

    def test_confirmation_receiver_JSON(self):
        """
        This method tests the confirmation receiver JSON view of the confirmation page. The expected result of this
        test is for the content of a session to be successfully added to the server-side database.
        """
        request = DummyRequest(route='/confirm.json')

        # Create a pattern to be saved to the database
        request.session["pattern"] = create_input_pattern()
        # Create a time and date to be saved for the pattern on the database
        time = datetime.datetime.now().replace(minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
        request.session["viewing_date"] = time.strftime("%d/%m/%Y")
        request.session["viewing_hour"] = time.strftime("%H")
        request.session["viewing_slot"] = time.strftime("%M")

        response_dict = confirmation_receiver_JSON(request)

        # Assert that a response has been retrieved.
        assert response_dict
        # Assert the data has been successfully stored to the database.
        assert response_dict["success"]

        # Assert that the data is inside the database.
        assert Run.get_run_for_time_slot(time)

        # Assert that the session has been emptied.
        assert not "pattern" in request.session
        assert not "viewing_date" in request.session
        assert not "viewing_hour" in request.session
        assert not "viewing_slot" in request.session

    def test_confirmation_receiver_JSON_failure(self):
        """
        This method tests the confirmation receiver JSON view of the confirmation page. The expected result of this
        test is for the session to have already been added to the database and to fail to be added again.
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
        # Assert that the data was not successfully stored.
        assert not response_dict["success"]
        # Assert that the response has been given a failure message.
        assert response_dict["failure_message"]

        # Assert that the session still exists.
        assert not "pattern" in request.session
        assert not "viewing_date" in request.session
        assert not "viewing_hour" in request.session
        assert not "viewing_slot" in request.session

    def teardown_class(self):
        """
        This method tears down the class after testing has been completed, in order to ensure no data exists after
        testing that shouldn't. In this case, closes down the database session.
        """
        with transaction.manager:
            for run in DBSession.query(Run).all():
                # Delete all runs in the database.
                DBSession.delete(run)
            DBSession.commit()

        # Close the database session.
        DBSession.remove()
        testing.tearDown()
