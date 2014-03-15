"""
This module contains logic that takes responsibility for the display driver's communication with the display's
serial interface, translating the pattern given to it to numbers that the display can understand.
"""

import serial


class DisplayControllerInterface(object):
    """
    This interface class contains the shared functionality of all display controllers, giving each inheriting controller
     a backbone with which to work.
    """

    def __init__(self, serial_name, baud_rate, timeout=1):
        """
        Ctor - Initialises the display controller with the correct serial communication data.

        @param serial_name The name of the serial with which to connect.
        @param baud_rate The baud rate with which the serial connection should work.
        @param timeout The number of seconds the serial connection should wait before timing out.
        """
        self._connection = serial.Serial(serial_name, baud_rate, timeout=timeout)

    def output_pattern(self, pattern):
        """
        This method sends the specified pattern to the display in a serial way the display can understand.

        @param pattern The pattern to be sent to the display.
        """
        raise NotImplementedError

    def __del__(self):
        """
        Dtor - Closes the serial connection between the application and the display.
        """
        self._connection.close()

class PrototypeController(DisplayControllerInterface):
    """
    The logic in this class exists only to test the display controller, and the display driver in general, on the
    prototype given to the software development team.
    """

    def output_pattern(self, pattern):
        """
        This method sends the specified pattern to the display in a serial way the display can understand. This method
        completely overrides the super method.

        @param pattern The pattern to output to the display.
        """
        self._clear()
        for i, line in enumerate(pattern.split("\n")):
            # for each row in the given pattern.
            for j, c in enumerate(line):
                # for each cell inside that row
                if c == "*":
                    # If the cell is alive, set the coordinates of that cell on the display to be drawn
                    self._set(j, i)
        # Draw the new configuration to the display.
        self._draw()

    def _clear(self):
        """
        This method sends the clear command to the display, turning all of the lights off.
        """
        self._connection.write("clr\n")

    def _set(self, x, y):
        """
        This method sends the set command to the display, giving the coordinates of a cell to turn on.

        @param x The x coordinate of the cell to be set
        @param y The y coordinate of the cell to be set
        """
        self._connection.write("set %s %s\n" % (str(x), str(y)))

    def _draw(self):
        """
        This method sends the draw command to the display, turning all of the set coordinates on.
        """
        self._connection.write("drw\n")

class DisplayController(DisplayControllerInterface):
    """
    The logic in this class exists to translate a pattern from our game engine to the display, which can only
    understand four numbers.
    """
 
    def output_pattern(self, pattern):
        """
        This method sends the specified pattern to the display in a serial way the display can understand. This method
        completely overrides the super method.

        @param pattern The pattern to output to the display.
        """
        self._clear()
        for i, line in enumerate(pattern.split("\n")):
            # for each row in the pattern
            for j, c in enumerate(line):
                # for each cell in that row
                if c == "*":
                    # If the cell is alive, set that cell's coordinates, ready to be drawn.
                    self._set(j, i)
        # Draws to the grid, turning all of the set cells on.
        self._draw()

    def _clear(self):
        """
        This method sends the clear command to the display, turning all of the lights off.
        """
        self._connection.write("0")

    def _set(self, x, y):
        """
        This method sends the set command to the display, giving the coordinates of a cell to turn on.

        @param x The x coordinate of the cell to be set
        @param y The y coordinate of the cell to be set
        """
        self._connection.write("1")
        self._connection.write("%s" % x)
        self._connection.write("%s" % y)

    def _draw(self):
        """
        This method sends the draw command to the display, turning all of the set coordinates on.
        """
        self._connection.write("3") 
