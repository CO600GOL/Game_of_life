"""
This module contains the logic for any display controllers; helper classes for the display driver that take on
the serial communication with the display itself.
"""

import serial


class DisplayControllerInterface(object):
    """
    This class represents a back-bone for all display controllers, taking on all shared functionality.
    """

    def __init__(self, serial_name, baud_rate, timeout=1):
        """
        Ctor - Initialises the display controller with the correct serial communication data.
        """
        #self._connection =

    def output_pattern(self, pattern):
        """
        Outputs the specified pattern to the display.
        """
        raise NotImplementedError

    def __del__(self):
        """
        Dtor - Closes the serial connection between the application and the display.
        """
        pass

class PrototypeController(DisplayControllerInterface):
    """
    This class represents the display controller used for the CO600 Computing Project prototype display.
    """

    def output_pattern(self, pattern):
        """
        Outputs the specified pattern to the display.

        N.B. Completely overrides the super method.
        """
        pass

    def _clear(self):
        """
        Just sends the clear command to the display
        """
        pass

    def _set(self, x, y):
        """
        Just sends the set command to the display, giving coordinates
        """
        pass

    def _draw(self):
        """
        Just sends the draw command to the display, so that it draws it's buffer to the display
        """
        pass

class DisplayContoller(DisplayControllerInterface):
    """
    This class represents the display controller used for Project Conway
    """

    def output_pattern(self, pattern):
        """
        Outputs the specified pattern to the display.

        N.B. Completely overrides the super method.
        """
        pass
