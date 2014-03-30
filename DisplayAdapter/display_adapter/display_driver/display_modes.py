"""
This module contains the logic for the display modes, controlling how the display driver handles the data being given
to it. Currently there are two modes, screensaver and run mode.
"""

from display_adapter import screensaver_config, runmode_config
from game.game_controllers.game_controllers import GameOfLifeController


class DisplayMode(object):
    """
    This interface class contains the shared functionality of all display modes, giving each inheriting class a
    backbone.
    """
    _game_engine = GameOfLifeController()

    def __init__(self, pattern):
        """
        Ctor - initialises the Mode with the correct information. Main function is to set up the game engine used for
        the pattern.

        @param pattern The next pattern to be shown on the display.
        """
        # Start up the game engine to calculate the next generation of the pattern.
        DisplayMode._game_engine.set_up_game(pattern)

    def is_active(self):
        """
        This method calculates whether or not it has any more patterns to pass back to the display driver.

        @return True if there is still a pattern to be shown, otherwise False.
        """
        # There are still patterns to be printed if any of the cells on the grid are seen as 'alive'.
        return not DisplayMode._game_engine.get_game().is_game_forsaken()

    def get_display_pattern(self):
        """
        This pattern returns the next pattern from the game engine as a string.

        @return The next generation to be shown on the display.
        """
        temp = DisplayMode._game_engine.get_current_generation(output=True)
        DisplayMode._game_engine.play_next_turn()
        return temp


class RunMode(DisplayMode):
    """
    This class represents the mode in which the display runs when it is showing a user's input pattern. This mode is
    shown to the user by presenting the pattern, followed by every light being flashed. This is done three times
    before the pattern is run with the game engine.
    """

    def __init__(self, pattern):
        """
        Ctor - initialises the Run mode with the correct information. Main function is
        to set up the game engine used for the specified pattern.

        @param pattern The pattern to be run through the game engine.
        """
        DisplayMode.__init__(self, pattern)
        self._pattern = pattern

        # Set up the number of times the display will switch between the user's pattern and the full light display.
        self._iterations = runmode_config["iterations"]
        # Set up the number of frames for which the full light display will be shown on display.
        self._full_frames = runmode_config["full_frames"]
        # Set up the number of frames for which the user's pattern will be shown on the display.
        self._pattern_frames = runmode_config["pattern_frames"]

    def is_active(self):
        """
        This method calculates whether or not it has any more patterns to pass back to the display driver.

        @return True if there are still iterations to be played on the 'start up' or if there are generations from
                the user's pattern to be played, otherwise false.
        """
        if self._iterations > 0:
            return True
        else:
            return not DisplayMode._game_engine.get_game().is_game_forsaken()

    def get_display_pattern(self):
        """
        This method calculates the next pattern to be displayed as a string. Usually this will be the next pattern
        from the game engine, but if on start up, it will enter a 'presentation state' to let the user know that
        their pattern is being run.

        @return The next pattern to be shown on the display.
        """
        if self._iterations > 0:
            if self._full_frames > 0:
                self._full_frames -= 1
                # In the presentation state, set all the cells to alive on every second configuration
                return self._pattern.replace("-", "*")

            elif self._pattern_frames > 0:
                self._pattern_frames -= 1

                if self._full_frames == 0 and self._pattern_frames == 0:
                    self._iterations -= 1
                    self._full_frames = runmode_config["full_frames"]
                    self._pattern_frames = runmode_config["pattern_frames"]

                # Return the next pattern in presentation mode
                return self._pattern
        else:
            # If presentation mode has finished, show the next generation
            return DisplayMode.get_display_pattern(self)


class ScreensaverMode(DisplayMode):
    """
    This class represents the mode in which the display runs when it is showing a screensaver pattern. This mode is
    shown to the user by all the lights turning on, row by row, and clearing away what was on the display before
    hand.
    """

    def __init__(self, pattern, previous_frame=None):
        """
        Ctor - initialises the Screensaver mode with the correct information. Main function is
        to set up the game engine used for the specified pattern.

        @param pattern The pattern with which to start the screensaver mode
        @param previous_frame The pattern that was on screen before screensaver mode began.
        """
        DisplayMode.__init__(self, pattern)
        if not previous_frame:
            # If there was no 'previous' pattern, just use an empty frame (all cells dead)
            previous_frame = pattern.replace("*", "-")
        self._previous_pattern = previous_frame

        self._pause_frames = screensaver_config["pause_frames"]
        self._clear_frames = len(previous_frame.split("\n"))

    def is_active(self):
        """
        This method calculates whether or not the mode has any more patterns to pass back to the display driver.

        @return True if there are frames in the startup 'clear' state remaining, or if there are generations in the
                user's pattern to be played, otherwise false.
        """
        if self._pause_frames > 0 or self._clear_frames > 0:
            return True
        else:
            return not DisplayMode._game_engine.get_game().is_game_forsaken()

    def get_display_pattern(self):
        """
        This method calculates the next pattern to be displayed as a string. Usually this will be the next pattern from
        the game engine, but if on start up, it will enter a 'clear state' where it wipes whatever was on the display
        away to let the users know it is entering screensaver mode.
        """
        if self._pause_frames > 0:
            self._pause_frames -= 1
            return self._previous_pattern
        elif self._clear_frames > 0:
            split = self._previous_pattern.split("\n")
            cols = len(split[0])

            #line 1: Build a string with the number of full rows
            #line 2: If any of the original pattern is used, add a new line char
            #line 3: If any of the original pattern is to be used, extract it and add to the first rows
            pattern = "\n".join(("*" * cols) for _ in range(0, (cols + 1) - self._clear_frames)) + \
                      ("\n" if (self._clear_frames-1 > 0) else "") + \
                      ("\n".join(split[(self._clear_frames-1)*-1:]) if (self._clear_frames-1 > 0) else "")

            self._clear_frames -= 1
            return pattern
        else:
            # Once the mode has left the 'clearing' state, start calculating the next actual generation to be shown
            # on the display
            return DisplayMode.get_display_pattern(self)
