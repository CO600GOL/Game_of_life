"""
This module contains testing logic for the display driver. The tests should make sure the driver can correctly set up
the necessary helper classes.
"""

from mock import patch
from datetime import datetime
from display_adapter.display_driver.display_drivers import minutify, DisplayDriver

class TestDisplayDriver(object):
    """
    This class tests the functionality of the DisplayDriver class, ensuring that it can correctly connect the Raspberry
    Pi to the display.
    """

    @patch("serial.Serial")
    def test_init(self, dc_mock):
        """
        This method tests initialisation of the display driver, ensuring it has correctly set up the database helper
        and the display controller.
        """
        dd = DisplayDriver()

        # Assert that the DisplayDriver exists
        assert dd
        # Assert that the display driver's database helper has been correctly set
        assert hasattr(dd, "_db_helper")
        # Assert that the display driver's display controller has been correctly set
        assert hasattr(dd, "_display_controller")



def test_minutify():
    """
    This function tests the functionality of the minutify function linked to the Display Driver. The expected result
    of this test is for a datetime object to be made accurate to the minute.
    """
    dt = datetime.now().replace(second=30, microsecond=40000)
    accurate_dt = minutify(dt)
    # Assert the datetime object has been minutified correctly (seconds and microseconds == 0)
    assert accurate_dt.second == 0 and accurate_dt.microsecond == 0
