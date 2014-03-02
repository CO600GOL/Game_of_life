"""
This module tests the functionality of the display controllers, making sure the application
can properly communicate with the display.
"""

class TestDisplayControllerInterface(object):
    """
    This class tests the functionality of the super DisplayController class, making sure all
    shared functionality of the controllers works correctly.
    """

    def test_init(self):
        """
        Tests initialisation of the display controller. Main function is to test proper and correct serial
        communication with the display.
        """
        pass

    def test_output_pattern(self):
        """
        Tests the display controller's ability to correctly output a pattern to the display.
        """
        pass

    def test_del(self):
        """
        Tests the destruction of the display controller, ensuring proper closure of the serial connection.
        """
        pass


class TestPrototypeController(object):
    """
    This class tests the functionality of the prototype display controller.
    """

    def test_init(self):
        """
        This class tests initialisation of the prototype display controller.
        """
        pass

    def test_output_pattern(self):
        """
        This method ensures the prototype display controller can correctly output a pattern to the prototype display.
        """
        pass


class TestDisplayController(object):
    """
    This class tests the functionality of the display controller used on the Project Conway display, ensuring the
    raspberry pi can connect to the device properly and correctly.
    """

    def test_init(self):
        """
        This method tests initialisation of the display controller used for the Project Conway display.
        """
        pass

    def test_output_pattern(self):
        """
        This method ensures the display controller can correctly output a pattern to the prototype display.
        """
        pass
