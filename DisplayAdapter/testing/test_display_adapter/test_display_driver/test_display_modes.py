"""
This module tests the logic responsible for deciding what the display will do with the run it is set to show, namely
the display mode.
"""

from display_adapter.display_modes import DisplayMode


class TestDisplayMode(object):
    """
    This class tests the super-class mode, to test shared functionality of all the display modes.
    """

    def test_is_active(self):
        """
        This method tests the shared functionality of the is_active class.
        """
        pass

    def test_get_next_pattern(self):
        """
        This method tests the ability of the display mode to correctly communicate with the game engine and return
        the correct next generation.
        """
        pass
