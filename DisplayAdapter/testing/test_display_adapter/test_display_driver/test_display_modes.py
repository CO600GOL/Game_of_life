"""
This module tests the logic responsible for deciding what the display will do with the run it is set to show, namely
the display mode.
"""

from display_adapter.display_driver.display_modes import DisplayMode


class TestDisplayMode(object):
    """
    This class tests the super-class mode, to test shared functionality of all the display modes.
    """

    def test_init(self):
        """
        Test the creation of the DisplayMode object.
        This object is not expected to act as a class, but to be
        inherited by other classes.
        """
        dm = DisplayMode("-*-\n-*-\n-*-")

        assert dm
        assert hasattr(dm, "_game_of_life")

    def test_is_active(self):
        """
        This method tests the shared functionality of the is_active class.
        """
        dm = DisplayMode("-*-\n-*-\n-*-")

        assert dm.is_active()

    def test_is_active_fails(self):
        """
        This method tests the shared functionality of the is_active class.
        """
        dm = DisplayMode("---\n---\n---")

        assert dm.is_active() == False

    def test_get_display_pattern(self):
        """
        This method tests the ability of the display mode to correctly communicate with the game engine and return
        the correct next generation.
        """
        dm = DisplayMode("-*-\n-*-\n-*-")

        assert dm.get_display_pattern() == "-*-\n-*-\n-*-"
        assert dm.get_display_pattern() == "***\n***\n***"
