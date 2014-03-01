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
        # Assert the display mode's game engine has access to the right pattern?
        assert DisplayMode._game_engine
        assert DisplayMode._game_engine.get_current_generation(output=True) == "-*-\n-*-\n-*-"

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


class TestRunMode(object):
    """
    This class tests the display's Run mode in order to test the working logic of the display when showing a player's
    pattern.
    """

    def test_init(self):
        """
        Tests initialisation of the display's Run mode.
        """
        pass

    def test_is_active(self):
        """
        Ensuring that the run is still active, especially in it's presentation state.
        """
        pass

    def test_is_active_fails(self):
        """
        Ensuring that the run is not active after the mode leaves it's presentation state.
        """
        pass

    def test_get_display_pattern(self):
        """
        Ensuring that the mode is, under all circumstances, returning the correct pattern to be displayed.
        The circumstances are as follows:
            - Two patterns during presentation state; all lights on and pattern lights on.
            - Once presentation state has finished, the player's pattern at the beginning of their cycle.
        """
        pass


class TestScreensaverMode(object):
    """
    This class tests the display's Screensaver mode in order to test the working logic of the display when not showing
    a player's pattern.
    """

    def test_init(self):
        """
        Tests initialisation of the display's Run mode.
        """
        pass

    def test_is_active(self):
        """
        Ensuring that the run is still active, especially in it's clear state.
        """
        pass

    def test_is_active_fails(self):
        """
        Ensuring that the run is not active after the mode leaves it's clear state.
        """
        pass

    def test_get_display_pattern(self):
        """
        Ensuring that the mode is, under all circumstances, returning the correct pattern to be displayed.
        The circumstances are as follows:
            - A pause of the frame on the display when it entered screensaver mode.
            - The correct number of clear frames when running in clear state.
            - Once clear state has finished, the correct frames for a screensaver pattern.
        """
        pass
