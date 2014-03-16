"""
This module contains the logic for any game to be played with the laid out data structures. These are games that are
played on a grid board of square cells.
"""


class Game(object):
    """
    The Game class acts as a skeleton for all games that can
    be played on the display.

    This class contains the shared functionality of all games to be played with the given data structure. A Game object
    itself is never instantiated, but works as a backbone for other games, such as the Game of Life.
    """

    def __init__(self):
        """
        Ctor - Intitialises a game object.
        """
        self._turn_count = 0

    def next_turn(self):
        """
        This method plays the next turn of the game.
        """
        self._turn_count += 1

    def get_turn_count(self):
        """
        This method retrieves the number of turns that have have been played in the game so far.

        @return the turn count for the current game.
        """
        return self._turn_count
