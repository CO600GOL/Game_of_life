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

        :TODO - Think about having one static GameOfLifeController or a new controller built every time a new mode is
                created
        """
        # Fields
        #   self._game_of_life = GameOfLifeController()
        pass

    def is_active(self):
        """
        This method returns whether or not it has any more patterns to pass back to the display driver.
        """
        pass

    def get_display_pattern(self):
        """
        This pattern returns the next pattern from the game engine as a string.
        """
        pass
