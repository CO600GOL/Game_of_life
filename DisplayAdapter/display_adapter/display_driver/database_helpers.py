"""
This module contains the logic for any helper classes
that support the display driver in interacting with the
Raspberry Pi's internal database.
"""

class DatabaseHelper(object):
    """
    This class is a helper for the DisplayDriver, taking all responsibility for communication with the database
    away from the driver itself.
    """

    def __init__(self, db_name):
        """
        Ctor - constructs the database helper, linking to the database with the given name
        """
        pass

    def get_run_for_time(self, time):
        """
        This method queries the internal database for the run to be played at the specified time.
        """
        pass

    def get_random_screensaver(self):
        """
        This method queries the internal database for a random screen saver to display.
        """
        pass