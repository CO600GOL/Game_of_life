"""
This module contains logic for testing the server-side database. These tests should evaluate whether the database
can be initialised correctly and can function correctly.
"""

import time
import math
import datetime
import transaction
from sqlalchemy  import create_engine
from pyramid import testing
from projectconway import project_config
from projectconway.models import Base, DBSession
from projectconway.models.run import Run


def create_input_pattern():
    """
    This function creates an initial input to represent the data being stored in the database.

    @return An initial input, formatted as a string.
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


class TestRun():
    """
    This class tests the functionality of the runs table and rows.
    """
     
    def setup_class(self):
        """
        This method sets up the testing class, initialising shared data that will be needed during testing.
        """
        self._insert_name = str(time.time())
        
        self.config = testing.setUp()
        engine = create_engine('sqlite:///testdb.sqlite')
        DBSession.configure(bind=engine)
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)

    def test_insert(self):
        """
        This method tests the ability of the runs table to insert a new row. The expected result of this test is for
        a row to be inserted into the table correctly.
        """
        with transaction.manager:
            run = Run(create_input_pattern(), datetime.datetime.now(), self._insert_name)
            DBSession.add(run)
            DBSession.commit()
         
    def test_query(self):
        """
        This method tests the ability of the runs table to retrieve data from the runs table. The expected result of
        this is for a row to be retrieved from the table correctly.
        """
        # Test logic works
        assert DBSession.query(Run).filter(Run.user_name==self._insert_name).all()
        
        # Test logic works as expected (Grid object is not altered in any way)
        for row in DBSession.query(Run).filter(Run.user_name==self._insert_name).all():
            returned_pattern = row.input_pattern.split('\n')
            test_pattern = create_input_pattern().split('\n')
            for x, row in enumerate(test_pattern):
                # For each row of the pattern
                for y, col in enumerate(row):
                    if test_pattern[x][y] == '*':
                        # Assert that the retrieved pattern and the test pattern match at these 'coordinates'.
                        assert returned_pattern[x][y] == '*'
                    else:
                        # Assert that the retrieved pattern and the test pattern match at these 'coordinates'.
                        assert returned_pattern[x][y] == '-'           
         
    def test_delete(self):
        """
        This method tests the ability of the runs table to delete data from it. The expected result of this is for the
        data to be correctly deleted from the table.
        """
        # Delete the run inserted by this test
        runs = DBSession.query(Run).filter(Run.user_name==self._insert_name)
        # Assert that the runs have been retrieved
        assert runs.all()
        for run in runs:
            DBSession.delete(run)
            DBSession.commit()

        runs = DBSession.query(Run).filter(Run.user_name==self._insert_name)
        # Assert that the selected runs have been deleted.
        assert not runs.all()

    def test_run_get_runs_for_day(self):
        """
        This method tests the ability of the runs table to retrieve every run set to be played on a given day. The
        expected result should be for a the call to result an empty dictionary.
        """
        # Give the method a future date and receive correct no. of time-slots for that date
        date = datetime.date.today() + datetime.timedelta(days=1)

        dayRuns = Run.get_runs_for_day(date)
        # Test that the method returns the right information
        assert dayRuns == []

    def test_run_get_runs_for_day_with_runs(self):
        """
        This method tests the ability of the runs table to retrieve every run set to be played on a given day. The
        expected result should be for the call to result in the same number of runs as previously added.
        """
        dt = datetime.datetime.now() + datetime.timedelta(days=1)
        dt = dt.replace(minute=0, second=0, microsecond=0)

        runs = [
            Run(create_input_pattern(), dt, self._insert_name),
            Run(create_input_pattern(), dt + datetime.timedelta(minutes=5), self._insert_name)]
        with transaction.manager:
            DBSession.add_all(runs)
            DBSession.commit

        date = datetime.date.today() + datetime.timedelta(days=1)
        dayRuns = Run.get_runs_for_day(date)
        # Assert that the correct number of runs have been retrieved
        assert dayRuns == runs

    def test_run_get_time_slots_for_day(self):
        """
        This method tests the ability of the runs table to retrieve the available time slots in a given day. The
        expected result of this test is for the number of retrieved time slots to be equal to the number of five minute
        time slots in a day.
        """
        # Give the method a future date and receive correct no. of time-slots for that date
        date = datetime.date.today() + datetime.timedelta(days=10)

        min_time = project_config["starting_time"]
        max_time = project_config["closing_time"]
        # Calculate the no. of hours in a given day to test
        no_mins = (max_time.hour*60 + max_time.minute) - (min_time.hour*60 + min_time.minute)
        no_time_slots = math.ceil(no_mins / 5)

        time_slots = Run.get_time_slots_for_day(date, datetime.datetime.now())

        # Assert that the correct number of available time slots have been retrieved.
        assert no_time_slots == len(time_slots)

    def test_run_get_time_slots_for_day_with_runs(self):
        """
        This method tests the ability of the runs table to retrieve the available time slots in a given day. The
        expected result of this test is for the number of retrieved time slots to be equal to the number of five
        minute time slots in a day minus two (for two runs).
        """
        # Give the method a future date and receive correct no. of time-slots for that date
        date = datetime.date.today() + datetime.timedelta(days=2)

        min_time = project_config["starting_time"]
        max_time = project_config["closing_time"]
        # Calculate the no. of hours in a given day to test
        no_mins = (max_time.hour*60 + max_time.minute) - (min_time.hour*60 + min_time.minute)
        no_time_slots = math.ceil(no_mins / 5)

        date = datetime.datetime.combine(date, datetime.time(hour=12, minute=0, second=0, microsecond=0))

        runs = [
            Run(create_input_pattern(), date, self._insert_name),
            Run(create_input_pattern(), date + datetime.timedelta(minutes=5), self._insert_name)]
        with transaction.manager:
            DBSession.add_all(runs)
            DBSession.commit

        time_slots = Run.get_time_slots_for_day(date, datetime.datetime.now())

        # Assert that the correct number of available time slots have been retrieved.
        assert no_time_slots - len(runs) == len(time_slots)

    def teardown_class(self):
        """
        This method tears down the testing class, closing the database session once the class is redundant.
        """
        DBSession.remove()
        testing.tearDown()
