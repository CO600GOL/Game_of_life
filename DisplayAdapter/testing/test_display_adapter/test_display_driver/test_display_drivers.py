"""
This module contains testing logic for the display driver. The tests should make sure the driver can correctly set up
the necessary helper classes.
"""

from display_adapter.display_driver.display_drivers import DisplayDriver

class TestDisplayDriver(object):
    """
    This class tests the functionality of the DisplayDriver class, ensuring that it can correctly connect the Raspberry
    Pi to the display.
    """

    def test_init(self):
        """
        This method tests initialisation of the display driver, ensuring it has correctly set up the database helper
        and the display controller.
        """
        dd = DisplayDriver()

        # Assert that the DisplayDriver exisrs
        assert dd
        # Assert that the display driver's database helper has been correctly set
        assert hasattr(dd, "_db_helper")
        # Assert that the display driver's display controller has been correctly set
        assert hasattr(dd, "_display_controller")