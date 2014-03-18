"""
This module tests the functionality of the display controllers, making sure the application
can properly communicate with the display.
"""

from mock import MagicMock, call, patch
from display_adapter.display_driver.display_controllers import DisplayControllerInterface, PrototypeController

@patch("serial.Serial")
class TestDisplayControllerInterface(object):
    """
    This class tests the functionality of the super DisplayController class, making sure all
    shared functionality of the controllers works correctly.
    """

    def test_init(self, serial_mock):
        """
        Tests initialisation of the display controller. Main function is to test proper and correct serial
        communication with the display.
        """
        dc = DisplayControllerInterface(0, 9600)

        assert dc
        assert hasattr(dc, "_connection")

    def test_output_pattern(self, serial_mock):
        """
        Tests the display controller's ability to correctly output a pattern to the display.
        """
        dc = DisplayControllerInterface(0, 9600)

        try:
            dc.output_pattern("")
        except:
            return

        raise Exception("output_pattern did not return NotImplementedError")


@patch("serial.Serial")
class TestPrototypeController(object):
    """
    This class tests the functionality of the prototype display controller.
    """

    def test_output_pattern(self, serial_mock):
        """
        This method ensures the prototype display controller can correctly output a pattern to the prototype display.
        """
        pc = PrototypeController(0, 9600)
        pc._connection = MagicMock()

        pc._clear = MagicMock()
        pc._set = MagicMock()
        pc._draw = MagicMock()

        pc.output_pattern("-*-\n-*-\n-*-")

        # Ensure clear and draw were called once
        pc._clear.assert_called_once_with()
        pc._draw.assert_called_once_with()

        # Test the set calls
        pc._set.assert_has_calls([
            call(1, 0),
            call(1, 1),
            call(1, 2)
        ])

    def test__clear(self, serial_mock):
        """
        Test the private clear function of ProrotypeController
        """
        serial = MagicMock()
        serial.write = MagicMock()

        pc = PrototypeController(0, 9600)
        pc._connection = serial

        pc._clear()
        serial.write.assert_called_once_with("clr\n")

    def test__set(self, serial_mock):
        """
        Test the private set function of ProrotypeController
        """
        serial = MagicMock()
        serial.write = MagicMock()

        pc = PrototypeController(0, 9600)
        pc._connection = serial

        pc._set(0, 0)
        serial.write.assert_called_once_with("set 0 0\n")

    def test__draw(self, serial_mock):
        """
        Test the private set function of ProrotypeController
        """
        serial = MagicMock()
        serial.write = MagicMock()

        pc = PrototypeController(0, 9600)
        pc._connection = serial

        pc._draw()
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
