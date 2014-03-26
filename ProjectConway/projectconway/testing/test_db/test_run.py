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


class TestRun():
    '''
    This class tests the Run table used in the web application database.
    '''
     
    def setup_class(self):
        '''
        Setup data that will be needed throughout the class and setup database
        '''
        self._insert_name = str(time.time())
        
        self.config = testing.setUp()
        engine = create_engine('sqlite:///testdb.sqlite')
        DBSession.configure(bind=engine)
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)

    def test__repr__(self):
        """
        This method tests the string representation of a Run row from the runs table. The expected result of this
        test is for the representation of the runs table to be returned correctly.
        """
        run = Run(create_input_pattern(), datetime.datetime.now(), self._insert_name)
        run_repr = run.__repr__()

        # Assert that the run's representation has been returned
        assert run_repr
        # Assert that the representation is a string object
        assert isinstance(run_repr, str)

    def test_insert(self):
        '''
        Test insertion of data into the runs table
        '''
        with transaction.manager:
            run = Run(create_input_pattern(), datetime.datetime.now(), self._insert_name)
            DBSession.add(run)
            DBSession.commit()
         
    def test_query(self):
        '''
        Test querying of data from the runs table
        '''
        # Test logic works
        assert DBSession.query(Run).filter(Run.user_name==self._insert_name).all()
        
        # Test logic works as expected (Grid object is not altered in any way)
        for row in DBSession.query(Run).filter(Run.user_name==self._insert_name).all():
            returned_pattern = row.input_pattern.split('\n')
            test_pattern = create_input_pattern().split('\n')
            for x, row in enumerate(test_pattern):
                for y, col in enumerate(row):
                    if test_pattern[x][y] == '*':
                        assert returned_pattern[x][y] == '*'
                    else:
                        assert returned_pattern[x][y] == '-'
         
    def test_delete(self):
        '''
        Test run deletion
        '''
        # Delete the run inserted by this test
        runs = DBSession.query(Run).filter(Run.user_name==self._insert_name)
        assert runs.all()
        for run in runs:
            DBSession.delete(run)
            DBSession.commit()

        # Ensure deletion
        runs = DBSession.query(Run).filter(Run.user_name==self._insert_name)
        assert not runs.all()

    def test_run_get_runs_for_day(self):
        """
        Tests the class method get_runs_for_day.
        Expect the method call to result in an empty dictionary.
        """
        # Give the method a future date and receive correct no. of time-slots for that date
        date = datetime.date.today() + datetime.timedelta(days=1)

        dayRuns = Run.get_runs_for_day(date)
        # Test that the method returns the right information
        assert dayRuns == []

    def test_run_get_runs_for_day_with_runs(self):
        """
        Tests the class method get_runs_for_day.
        With runs added to the database, expect the method call to return the same number
        of runs as added.
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
        # Test the method returns the correct information
        assert dayRuns == runs

    def test_run_get_time_slots_for_hour(self):
        """
        This method tests the ability of the runs table to retrieve the available time slots for the same hour in which
        a given time slot is to run. The expected result of this test is for the correct number of available timeslots
        to be retrieved when there are no runs to be played in a given hour.
        """
        # Give the method a future date
        time_slot = datetime.datetime.now() + datetime.timedelta(days=20)
        time_slot = time_slot.replace(minute=5)

        # No of possible time slots in an hour is 60 (no. minutes in an hour) / 5 (maximum length of each timeslot) = 12
        no_time_slots = 12

        # Retrieve the time slots for the specified time slot
        time_slots = Run.get_time_slots_for_hour(time_slot)

        # Assert that the correct number of time slots has been recovered (12)
        assert no_time_slots == len(time_slots)

    def test_run_get_time_slots_for_day(self):
        """
        Tests the class method get_slots_for_day.
        """
        # Give the method a future date and receive correct no. of time-slots for that date
        date = datetime.date.today() + datetime.timedelta(days=10)

        min_time = project_config["starting_time"]
        max_time = project_config["closing_time"]
        # Calculate the no. of hours in a given day to test
        no_mins = (max_time.hour*60 + max_time.minute) - (min_time.hour*60 + min_time.minute)
        no_time_slots = math.ceil(no_mins / 5)

        time_slots = Run.get_time_slots_for_day(date, datetime.datetime.now())

        assert no_time_slots == len(time_slots)

    def test_run_get_time_slots_for_day_with_runs(self):
        """
        Tests the class method get_time_slots_for_day
        With runs added to the database, expect the method call to return the full number of
        available time slots - the number of runs
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

        assert no_time_slots - len(runs) == len(time_slots)

    def teardown_class(self):
        '''
        Closes database session once the class is redundant
        '''
        DBSession.remove()
        testing.tearDown()
