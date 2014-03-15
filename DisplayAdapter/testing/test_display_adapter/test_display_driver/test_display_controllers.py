"""
This module contains testing logic for the display driver's display controller. The tests should make sure the
controller can correctly communicate with the serial interface, sending it the right data.
"""

from mock import MagicMock, call
from display_adapter.display_driver.display_controllers import DisplayControllerInterface, PrototypeController

class TestDisplayControllerInterface(object):
    """
    This class tests the functionality of the super DisplayController class, making sure all
    shared functionality of the controllers works correctly.
    """

    def test_init(self):
        """
        Tests initialisation of the display controller. The expected result of this test is correct initialisation of
        the display controller, with proper serial connectivity.
        """
        dc = DisplayControllerInterface(0, 9600)

        # Assert that the display controller has been initialised.
        assert dc
        # Assert that the controller's serial connection has been set up properly.
        assert hasattr(dc, "_connection")

    def test_output_pattern(self):
        """
        Tests the display controller's ability to correctly output a pattern to the display.
        """
        dc = DisplayControllerInterface(0, 9600)

        try:
            dc.output_pattern("")
        except:
            return

        # If the code has reached this point, output_pattern has been implemented and the test should fail
        raise Exception("output_pattern did not return NotImplementedError")


class TestPrototypeController(object):
    """
    This class tests the functionality of the prototype display controller.
    """

    def test_output_pattern(self):
        """
        This method ensures the prototype display controller can correctly output a pattern to the prototype display.
        """
        pc = PrototypeController(0, 9600)
        # Mock the connection
        pc._connection = MagicMock()

        pc._clear = MagicMock()
        pc._set = MagicMock()
        pc._draw = MagicMock()

        pc.output_pattern("-*-\n-*-\n-*-")

        # Ensure clear and draw were called once.
        pc._clear.assert_called_once_with()
        pc._draw.assert_called_once_with()

        # Test the set calls.
        pc._set.assert_has_calls([
            call(1, 0),
            call(1, 1),
            call(1, 2)
        ])

    def test__clear(self):
        """
        Test the private clear function of ProrotypeController
        """
        serial = MagicMock()
        serial.write = MagicMock()

        pc = PrototypeController(0, 9600)
        pc._connection = serial

        pc._clear()
        # Assert that the correct call to the display interface has been made.
        serial.write.assert_called_once_with("clr\n")

    def test__set(self):
        """
        Test the private set function of ProrotypeController
        """
        serial = MagicMock()
        serial.write = MagicMock()

        pc = PrototypeController(0, 9600)
        pc._connection = serial

        pc._set(0, 0)
        # Assert that the correct call to the display interface has been made.
        serial.write.assert_called_once_with("set 0 0\n")

    def test__draw(self):
        """
        Test the private set function of ProrotypeController
        """
        serial = MagicMock()
        serial.write = MagicMock()

        pc = PrototypeController(0, 9600)
        pc._connection = serial

        pc._draw()
        # Assert that the correct call to the display interface has been made.
        serial.write.assert_called_once_with("drw\n")


class TestDisplayController(object):
    """
    This class tests the functionality of the display controller used on the Project Conway display, ensuring the
    raspberry pi can connect to the device properly and correctly.
    """

    def test_output_pattern(self):
        """
        This method ensures the display controller can correctly output a pattern to the prototype display.
        """
        pass
