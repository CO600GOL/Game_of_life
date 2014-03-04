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
from display_adapter.display_driver.display_controllers import PrototypeController
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
        self._display_controller = PrototypeController(serial_name, serial_baudrate)

    def start(self):
        """
        Starts the application: begins checking the current time and working out what information needs to be sent
        to the display at that time.
        """
        mode = ScreensaverMode(self._db_helper.get_random_screensaver())
        last_pattern = None
        last_check_time = datetime.datetime.now() - datetime.timedelta(minutes=10)

        while True:
            current_time = datetime.datetime.now()
            min_current_time = minutify(current_time)

            if (current_time.minute % 5) == 0 and (min_current_time > last_check_time):

                last_check_time = min_current_time
                t_format = "%Y-%m-%d %H:%M:00.000000"
                pattern = self._db_helper.get_run_for_time(current_time.strftime(t_format))
                if pattern:
                    mode = RunMode(pattern)
                else:
                    mode = ScreensaverMode(self._db_helper.get_random_screensaver(), last_pattern)

            if not mode.is_active():
                mode = ScreensaverMode(self._db_helper.get_random_screensaver(), last_pattern)

            last_pattern = mode.get_display_pattern()

            self._display_controller.output_pattern(last_pattern)

            sleep_until_time = current_time + datetime.timedelta(seconds=sleep_time)
            time.sleep((sleep_until_time - datetime.datetime.now()).microseconds / 1000000)

            self.logger.warn("Outputted pattern at: %s" % current_time)

def minutify(dt):
    """
    Takes a datetime object and returns it with an accuracy of minutes
    """
    return dt.replace(second=0, microsecond=0)

if __name__ == "__main__":
    DisplayDriver().start()