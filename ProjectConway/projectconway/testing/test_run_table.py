import time
import transaction
from sqlalchemy import create_engine
from pyramid import testing
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


class TestRunTable():
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
        Base.metadata.create_all(engine)

    def test_insert(self):
        '''
        Test insertion of data into the runs table
        '''
        with transaction.manager:
            run = Run(create_input_pattern(), self._insert_name)
            DBSession.add(run)
            DBSession.commit()
         
    def test_query(self):
        '''
        Test querying of data from the runs table
        '''
        assert DBSession.query(Run).filter(Run.user_name==self._insert_name).all()
         
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
    
    def teardown_class(self):
        '''
        Closes database session once the class is redundant
        '''
        DBSession.remove()
        testing.tearDown()
