"""
The module encapsulates "screen modes".
We invisidge there being two modes, screensaver mode and run mode.
Screensaver mode:
    - This mode takes a pattern that is to be "wiped away" and the screen saver pattern
    - The screen will then "wipe"
        - A line of lights will come down over the "wiped away" pattern
        - When the screen is filled, the new screen saver pattern will start
    - Creates a GameOfLife object with the screensaver pattern
    - The class then return the next generation of this pattern when asked
Run mode:
    - The pattern to be "displayed" is passed to the object
    - The class will then alternate between displaying a "full" screen and the pattern for
        - TODO: finalise the pattern in which they alternate
        - This is in order to seperate this "run" from other "runs"
    - Creates a GameOfLife object with this pattern
    - Then returns the next generation of this pattern when asked
"""

from display_adapter import screensaver_config, runmode_config
from game.game_controllers.game_controllers import GameOfLifeController


class DisplayMode(object):
    """
    This class represents a back-bone for all display modes, serving as a place for shared functionality.
    """
    _game_engine = GameOfLifeController()

    def __init__(self, pattern):
        """
        Ctor - initialises the Mode with the correct information. Main function
        is to set up the game engine used for the pattern.
        """
        DisplayMode._game_engine.set_up_game(pattern)

    def is_active(self):
        """
        This method returns whether or not it has any more patterns to pass back to the display driver.
        """
        return not DisplayMode._game_engine.get_game().is_game_forsaken()

    def get_display_pattern(self):
        """
        This pattern returns the next pattern from the game engine as a string.
        """
        temp = DisplayMode._game_engine.get_current_generation(output=True)
        DisplayMode._game_engine.play_next_turn()
        return temp


class RunMode(DisplayMode):
    """
    This class represents the mode in which the display runs when it is showing a user's input pattern.
    """

    def __init__(self, pattern):
        """
        Ctor - initialises the Run mode with the correct information. Main function is
        to set up the game engine used for the specified pattern.
        """
        DisplayMode.__init__(self, pattern)
        self._pattern = pattern

        self._iterations = runmode_config["iterations"]
        self._full_frames = runmode_config["full_frames"]
        self._pattern_frames = runmode_config["pattern_frames"]

    def is_active(self):
        """
        This method returns whether or not it has any more patterns to pass back to the display driver.
        """
        if self._iterations > 0:
            return True
        else:
            return not DisplayMode._game_engine.get_game().is_game_forsaken()

    def get_display_pattern(self):
        """
        This method returns the next pattern to be displayed as a string. Usually this will be the next pattern
        from the game engine, but if on start up, it will enter a 'presentation state' to let the user know that
        their pattern is being run.
        """
        if self._iterations > 0:
            if self._full_frames > 0:
                self._full_frames -= 1
                return self._pattern.replace("-", "*")

            elif self._pattern_frames > 0:
                self._pattern_frames -= 1

                if self._full_frames == 0 and self._pattern_frames == 0:
                    self._iterations -= 1
                    self._full_frames = runmode_config["full_frames"]
                    self._pattern_frames = runmode_config["pattern_frames"]

                return self._pattern
        else:
            return DisplayMode.get_display_pattern(self)


class ScreensaverMode(DisplayMode):
    """
    This class represents the mode in which the display runs when it is not showing a user's input pattern.
    """

    def __init__(self, pattern, previous_frame):
        """
        Ctor - initialises the Screensaver mode with the correct information. Main function is
        to set up the game engine used for the specified pattern.
        """
        DisplayMode.__init__(self, pattern)
        self._previous_pattern = previous_frame

        self._pause_frames = screensaver_config["pause_frames"]
        self._clear_frames = len(previous_frame.split("\n"))

    def is_active(self):
        """
        This method returns whether or not the mode has any more patterns to pass back to the display driver.
        """
        if self._pause_frames > 0 or self._clear_frames > 0:
            return True
        else:
            return not DisplayMode._game_engine.get_game().is_game_forsaken()

    def get_display_pattern(self):
        """
        This method returns the next pattern to be displayed as a string. Usually this will be the next pattern from
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
            return DisplayMode.get_display_pattern(self)
