"""
This module contains the functionality of all device drivers, which serve as the highest-level controllers of the
device within the raspberry pi. Though they maintain control of the data being passed to the display, they do not do
this directly, instead handing the data off to another helper class.
"""

import time
import logging
import datetime
from display_adapter import db_name, serial_name, serial_baudrate, sleep_time
from display_adapter.display_driver.database_helpers import DatabaseHelper
from display_adapter.display_driver.display_controllers import DisplayController
from display_adapter.display_driver.display_modes import RunMode, ScreensaverMode

class DisplayDriver(object):
    """
    This class represents the display driver that links the raspberry pi to the display. This driver will have high-
    level control over the data being sent to the display, but will do this mostly through the help of smaller utility
    classes.
    """
    logger = logging.getLogger("display")

    def __init__(self):
        """
        Ctor - Initialises the display driver, setting up the database helper and display controller.
        """
        self._db_helper = DatabaseHelper(db_name)
        self._display_controller = DisplayController(serial_name, serial_baudrate)

    def start(self):
        """
        Starts the application: begins checking the current time and working out what information needs to be sent
        to the display at that time.
        """
        mode = ScreensaverMode(self._db_helper.get_random_screensaver())
        last_pattern = None
        last_check_time = datetime.datetime.now() - datetime.timedelta(minutes=10)

        while True:
            # Check the current time and make it accurate to the second
            current_time = datetime.datetime.now()
            min_current_time = minutify(current_time)

            if (current_time.minute % 5) == 0 and (min_current_time > last_check_time):
                # If the current time is on one of the five min. intervals, attempt to pull a pattern from the
                # internal database.
                last_check_time = min_current_time
                t_format = "%Y-%m-%d %H:%M:00.000000"
                pattern = self._db_helper.get_run_for_time(current_time.strftime(t_format))
                if pattern:
                    # If a pattern is successfully pulled, run the display's 'run mode' on it.
                    mode = RunMode(pattern)
                else:
                    # Otherwise pull a random screensaver from the internal database and run that in 'screensaver
                    # mode'
                    mode = ScreensaverMode(self._db_helper.get_random_screensaver(), last_pattern)

            if not mode.is_active():
                # If the current pattern finishes before the five minute timer has stopped, switch to
                # screensaver mode
                mode = ScreensaverMode(self._db_helper.get_random_screensaver(), last_pattern)

            # Retrieve the latest pattern to be sent to the display
            last_pattern = mode.get_display_pattern()

            # Send the pattern to the display controller for printing.
            self._display_controller.output_pattern(last_pattern)

            # While not working, sleep
            sleep_until_time = current_time + datetime.timedelta(seconds=sleep_time)
            time.sleep((sleep_until_time - datetime.datetime.now()).microseconds / 1000000)

            self.logger.warn("Outputted pattern at: %s" % current_time)

def minutify(dt):
    """
    Takes a datetime object and returns it with an accuracy of minutes

    @param dt The datetime to be minutified.

    @return A datetime object accurate to the minute.
    """
    return dt.replace(second=0, microsecond=0)

# Starts the display driver if this module is called from the command line.
if __name__ == "__main__":
    DisplayDriver().start()
