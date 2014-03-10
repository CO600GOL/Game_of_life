import time
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
        dt.replace(minute=0, second=0, microsecond=0)

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


    def test_run_get_time_slots_for_day(self):
        """
        Tests the class method get_slots_for_day.
        """
        # Give the method a future date and receive correct no. of time-slots for that date
        date = datetime.date.today() + datetime.timedelta(days=1)
        # Calculate the no. of hours in a given day to test
        noHours = (project_config["maximum_date"] - project_config["minimum_date"]) // 60 // 60

    def teardown_class(self):
        '''
        Closes database session once the class is redundant
        '''
        DBSession.remove()
        testing.tearDown()
