"""
This module contains the testing framework for the display driver functionality, and is responsible for testing whether
the pi can correctly and sufficiently connect to the display.
"""

from display_adapter.display_driver.display_drivers import DisplayDriver

class TestDisplayDriver(object):
    """
    This class tests the functionality of the DisplayDriver class, ensuring that it can correctly connect the raspberry
    pi to the display.
    """

    def test_init(self):
        """
        This method tests initialisation of the display driver, ensuring it has correctly set up the database helper
        and the display controller.
        """
        dd = DisplayDriver()

        assert dd
        assert hasattr(dd, "_db_helper")
        assert hasattr(dd, "_display_controller")