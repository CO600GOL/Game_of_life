"""
This module contains the functionality of all device drivers, which serve as the highest-level controllers of the
device within the raspberry pi. Though they maintain control of the data being passed to the display, they do not do
this directly, instead handing the data off to another helper class.
"""

from display_adapter import db_name, serial_name
from display_adapter.display_driver.database_helpers import DatabaseHelper
from display_adapter.display_driver.display_controllers import PrototypeController
from display_adapter.display_driver.display_modes import RunMode, ScreensaverMode

class DisplayDriver(object):
    """
    This class represents the display driver that links the raspberry pi to the display. This driver will have high-
    level control over the data being sent to the display, but will do this mostly through the help of smaller utility
    classes.
    """

    def __init__(self):
        """
        Ctor - Initialises the display driver, setting up the database helper and display controller.
        """
        pass

    def start(self):
        """
        Starts the application: begins checking the current time and working out what information needs to be sent
        to the display at that time.
        """
        pass