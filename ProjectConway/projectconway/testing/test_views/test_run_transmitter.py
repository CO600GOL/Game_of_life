"""
This module tests the functionality of the run transmitter, a view that takes unsent runs from the server-side database
and sends them to the raspberry pi. These tests must evaluate that the view functions correctly.
"""

import datetime
import transaction
from pyramid import testing
from sqlalchemy import create_engine
from pyramid.testing import DummyRequest
from projectconway.models import Base, DBSession
from projectconway.models.run import Run
from projectconway.views.run_transmitter import run_transmitter_view

def setup_module(self):
    '''
    Setup data that will be needed throughout the class and setup database
    '''
    self.config = testing.setUp()
    engine = create_engine('sqlite:///testdb.sqlite')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

def create_input_pattern():
    """
    Create an initial input to represent the data being saved
    to the database.
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

def test_run_transmitter_view():
    """
    This function tests the functionality of the run_transmitter view. The expected result of this
    test is that the view functions correctly and retrieves currently unsent runs for the raspberry pi.
    """
    time_slot = datetime.datetime.now() + datetime.timedelta(days=5)

    # Add a pattern and time to the database for testing
    with transaction.manager:
        DBSession.add(Run(create_input_pattern(), time_slot, ""))
        DBSession.commit()

    # Set up request
    request = DummyRequest(route='/run_transmitter.json')
    time_slot -= datetime.timedelta(hours=1)
    request.POST["min_time"] = time_slot.isoformat()

    # Call the view
    response = run_transmitter_view(request)

    # Test that the view has returned a response
    assert response

