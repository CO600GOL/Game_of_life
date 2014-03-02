"""
This module contains the logic for any display controllers; helper classes for the display driver that take on
the serial communication with the display itself.
"""


class DisplayControllerInterface(object):
    """
    This class represents a back-bone for all display controllers, taking on all shared functionality.
    """

    def __init__(self, serial_name):
        """
        Ctor - Initialises the display controller with the correct serial communication data.
        """
        pass

    def output_pattern(self, pattern):
        """
        Outputs the specified pattern to the display.
        """
        pass

    def __del__(self):
        """
        Dtor - Closes the serial connection between the application and the display.
        """
        pass

class PrototypeController(DisplayControllerInterface):
    """
    This class represents the display controller used for the CO600 Computing Project prototype display.
    """

    def __init__(self, serial_name):
        """
        Ctor - Initialises the prototype display controller, ensuring the correct serial connectivity.
        """
        pass

    def output_pattern(self, pattern):
        """
        Outputs the specified pattern to the display.

        N.B. Completely overrides the super method.
        """
        pass


class DisplayContoller(DisplayControllerInterface):
    """
    This class represents the display controller used for Project Conway
    """

    def __init__(self):
        """
        Ctor - Initialises the display controller, ensuring the correct serial connectivity.
        """
        pass

    def output_pattern(self, pattern):
        """
        Outputs the specified pattern to the display.

        N.B. Completely overrides the super method.
        """
        pass
