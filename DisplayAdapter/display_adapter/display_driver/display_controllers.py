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
        self._connection = serial.Serial(serial_name, baud_rate, timeout=timeout)

    def output_pattern(self, pattern):
        """
        Outputs the specified pattern to the display.
        """
        raise NotImplementedError

    def __del__(self):
        """
        Dtor - Closes the serial connection between the application and the display.
        """
        self._connection.close()

class PrototypeController(DisplayControllerInterface):
    """
    This class represents the display controller used for the CO600 Computing Project prototype display.
    """

    def output_pattern(self, pattern):
        """
        Outputs the specified pattern to the display.

        N.B. Completely overrides the super method.
        """
        self._clear()
        for i, line in enumerate(pattern.split("\n")):
            for j, c in enumerate(line):
                if c == "*":
                    self._set(j, i)
        self._draw()

    def _clear(self):
        """
        Just sends the clear command to the display
        """
        self._connection.write("clr\n")

    def _set(self, x, y):
        """
        Just sends the set command to the display, giving coordinates
        """
        self._connection.write("set %s %s\n" % (str(x), str(y)))

    def _draw(self):
        """
        Just sends the draw command to the display, so that it draws it's buffer to the display
        """
        self._connection.write("drw\n")

class DisplayController(DisplayControllerInterface):
    """
    This class represents the display controller used for Project Conway
    """
 
    def output_pattern(self, pattern):
        """
        Outputs the specified pattern to the display.

        N.B. Completely overrides the super method.
        """
        self._clear()
        for i, line in enumerate(pattern.split("\n")):
            for j, c in enumerate(line):
                if c == "*":
                    self._set(j, i)
        self._draw()

    def _clear(self):
        """
        Just sends the clear command to the display
        """
        self._connection.write("0")

    def _set(self, x, y):
        """
        Just sends the set command to the display, giving coordinates
        """
        self._connection.write("1")
        self._connection.write("%s" % y)
        self._connection.write("%s" % x)

    def _draw(self):
        """
        Just sends the draw command to the display, so that it draws it's buffer to the display
        """
        self._connection.write("3") 
