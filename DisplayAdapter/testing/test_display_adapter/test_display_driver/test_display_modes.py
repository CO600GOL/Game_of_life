"""
This module contains the testing logic for the different display modes available to the display driver. The tests
should make sure the different modes correctly handle the data given to them.
"""

from display_adapter import runmode_config
from display_adapter.display_driver.display_modes import DisplayMode, RunMode, ScreensaverMode


class TestDisplayMode(object):
    """
    This class tests shared functionality of all display modes, making sure their backbone is correctly implemented.
    """

    def test_init(self):
        """
        Tests the initialisation of a DisplayMode object. This is to check shared object data is correctly set - the
        object itself is not meant to be used.
        """
        dm = DisplayMode("-*-\n-*-\n-*-")

        # Assert the display mode has been initialised.
        assert dm
        # Assert the display mode's game engine has been initialised correctly.
        assert DisplayMode._game_engine
        # Assert the display mode's game engine has access to the right pattern.
        assert DisplayMode._game_engine.get_current_generation(output=True) == "-*-\n-*-\n-*-"

    def test_is_active(self):
        """
        This method tests the functionality of the over-arching is_active method. The expected result of this test
        is for the display mode to be active.
        """
        dm = DisplayMode("-*-\n-*-\n-*-")

        # Assert that the display mode is active.
        assert dm.is_active()

    def test_is_active_fails(self):
        """
        This method tests the functionality of the over-arching is_active method. The expected result of this test
        is for the display mode to be inactive.
        """
        dm = DisplayMode("---\n---\n---")

        # Assert that the display mode is inactive.
        assert dm.is_active() == False

    def test_get_display_pattern(self):
        """
        This method tests the ability of the display mode to communicate with the game engine. The expected result of
        this test is for the get_display_pattern method to first of all return its given pattern, and then the correctly
        calculated next generation of the Game of life.
        """
        dm = DisplayMode("-*-\n-*-\n-*-")

        # Assert the display mode can return its given pattern.
        assert dm.get_display_pattern() == "-*-\n-*-\n-*-"
        # Assert the display mode can use the game engine to return the next calculated pattern.
        assert dm.get_display_pattern() == "***\n***\n***"


class TestRunMode(object):
    """
    This class tests the display's 'run mode' in order to test the working logic of the display when showing a player's
    pattern.
    """

    def test_init(self):
        """
        Tests initialisation of the display's Run mode. The expected result of this test is to make sure the correct
        data has been saved on initialisation.
        """
        rm = RunMode("---\n---\n---")

        # Assert the 'run mode' has been initialised.
        assert rm
        # Assert that the mode has been initialised with the right pattern.
        assert hasattr(rm, "_pattern")

    def test_is_active(self):
        """
        This method tests that 'run mode' is still active, especially in it's presentation state. The expected result
        of this test is for the check to show the mode is still active.
        """
        rm = RunMode("-*-\n-*-\n-*-")

        for _ in range(0, runmode_config["iterations"]):
            # For each iteration of the mode's presentation state.
            for _ in range(0, runmode_config["full_frames"]):
                # For each time presentation state shows a full light display.

                # Assert the mode is still active.
                assert rm.is_active()
                rm.get_display_pattern()

            for _ in range(0, runmode_config["pattern_frames"]):
                # For each time presentation state shows the user's pattern

                # Assert the mode is still active
                assert rm.is_active()
                rm.get_display_pattern()

        # Once presentation state, assert the mode is still active.
        assert rm.is_active()
        rm.get_display_pattern()
        # Assert the mode is still active once the user's pattern has started running.
        assert rm.is_active()

    def test_is_active_fails(self):
        """
        This method tests that 'run mode' activity does change. The expected result of this test is that the
        is_active method returns inactivity.
        """
        rm = RunMode("---\n---\n---")

        for _ in range(0, runmode_config["iterations"]):
            # For each iteration of the mode's presentation state
            for _ in range(0, runmode_config["full_frames"]):
                # For each time presentation state shows a full light display.

                # Assert the mode is active.
                assert rm.is_active()
                rm.get_display_pattern()

            for _ in range(0, runmode_config["pattern_frames"]):
                # For each time presentation state shows the user's pattern.

                # Assert the mode is still active.
                assert rm.is_active()
                rm.get_display_pattern()

        # Assert the mode is no longer active.
        assert not rm.is_active()

    def test_get_display_pattern(self):
        """
        This method tests that the mode is, under all circumstances, returning the correct pattern to be displayed.
        The circumstances are as follows:
            - Two patterns during presentation state; a full light display, and the cells of the user's pattern.
            - Once presentation state has finished, the player's pattern as it plays out on the display.
        """
        input = "-*-\n-*-\n-*-"
        rm = RunMode(input)

        for _ in range(0, runmode_config["iterations"]):
            # For each iteration of the mode's presentation state
            for _ in range(0, runmode_config["full_frames"]):
                # For each time the presentation state shows a full light display
                # Assert that the presentation state is showing a full light display
                assert rm.get_display_pattern() == "***\n***\n***"

            for _ in range(0, runmode_config["pattern_frames"]):
                # For each time the presentation state shows the user's pattern.
                # Assert that the presentation state is showing the user's pattern
                assert rm.get_display_pattern() == input

        # Assert that the mode is showing the user's pattern
        assert rm.get_display_pattern() == input


class TestScreensaverMode(object):
    """
    This class tests the display's 'sceensaver mode' in order to test the working logic of the display when not showing
    a player's pattern.
    """

    def test_init(self):
        """
<<<<<<< HEAD
        This method tests the initialisation of the display's screensaver mode. The expected result of this tests is
        to make sure the correct data has been saved on initialisation.
=======
        Tests initialisation of the display's Screensaver mode.
>>>>>>> 1d5db25e9f79e1673e0e1503cfe0183f5ab5553a
        """
        sm = ScreensaverMode("---\n---\n---", "---\n---\n---")

        # Assert the mode has been initialised.
        assert sm
        # Assert the mode's previous pattern has been correctly set.
        assert sm._previous_pattern == "---\n---\n---"

    def test_init_from_startup(self):
        """
        This method tests the initialisation of the display's Screensaver mode when the device starts up for the first
        time. This means that there won't be a previous pattern which which the mode can work.
        """

        sm = ScreensaverMode("---\n---\n---")

        # Assert that the screensaver mode has been initialised.
        assert sm
        # Assert that the previous pattern has been correctly set to an empty grid.
        assert sm._previous_pattern == "---\n---\n---"

    def test_is_active(self):
        """
        This method tests that 'screensaver mode' is still active, especially in its clearing state. The expected
        result of this tests is for the check to show the mode is still active.
        """
        input = "-*-\n-*-\n-*-"
        previous = "---\n---\n---"
        sm = ScreensaverMode(input, previous)

        for _ in range(0, 3):
            # For each frame of the pause

            # Assert the mode is still active.
            assert sm.is_active()
            sm.get_display_pattern()

        for i, _ in enumerate(previous.split("\n")):
            # For each cell in the previous pattern

            # Assert the mode is still active.
            assert sm.is_active()
            # Calculate the next pattern to be displayed.
            sm.get_display_pattern()
            # Assert the mode is still active.
            assert sm.is_active()

        # Calculate the next pattern to be displayed.
        sm.get_display_pattern()
        # Assert the mode is still active.
        assert sm.is_active()

    def test_is_active_fails(self):
        """
        This method tests that 'screensaver mode' activity does change. The expected result of the test is that the
        is_active method returns inactivity.
        """
        input = "---\n---\n---"
        previous = "---\n---\n---"
        sm = ScreensaverMode(input, previous)

        for _ in range(0, 3):
            # For each frame of the pause

            # Assert the mode is still active.
            assert sm.is_active()
            sm.get_display_pattern()

        for i, _ in enumerate(previous.split("\n")):
            # For each cell in the previous pattern.

            # Assert the mode is still active.
            assert sm.is_active()
            # Calculate the next pattern to be displayed.
            sm.get_display_pattern()

        # Assert that the mode is no longer active.
        assert not sm.is_active()

    def test_get_display_pattern(self):
        """
        This method tests that the mode is, under all circumstances, returning the correct pattern to be displayed.
        The circumstances are as follows:
            - A pause on the frame the display was showing when it entered screensaver mode.
            - The correct number of clearing frames when running in clearing state.
            - Once clearing state has finished, the correct frames for a screensaver pattern.
        """
        input = "-*-\n-*-\n-*-"
        previous = "---\n---\n---"
        sm = ScreensaverMode(input, previous)

        for _ in range(0, 3):
            # For each frame of the pause.

            # Assert the mode is returning the correct pattern at this point.
            assert sm.get_display_pattern() == previous

        for i, _ in enumerate(previous.split("\n")):
            # For each cell of the previous pattern

            # Assert that the mode is still calculating a pattern at this point.
            assert sm.get_display_pattern()

        # Assert that the mode is returning the input pattern at this point.
        assert sm.get_display_pattern() == input
