"""
This module contains logic that tests the generic game engine. These tests must evaluate whether a game engine can
be correctly initialised and can function correctly.
"""

from game.game import Game


class TestGame(object):
    """
    This class tests the functionality of the Game class.
    """

    def test_init(self):
        """
        Tests the initialisation of a Game object.

        This method tests the initialisation of a Game object. The expected result of this test is for a Game to be
        correctly initialised.
        """
        g = Game()

        # Assert a game has been initialised.
        assert g

        # Assert the game has been initialised with the correct number of turns (will always be zero).
        assert g._turn_count == 0

    def test_next_turn(self):
        """
        This method tests the ability of the game engine to play its next turn. The expected result of this test is for
        the next game turn to be played correctly.
        """
        g = Game()

        g.next_turn()
        # If the next turn has been played, the turn count will be 1 at this point. Assert this is true.
        assert g._turn_count == 1

    def test_get_turn_count(self):
        """
        This method tests the ability of the game engine to retrieve the number of turns that have so far been played.
        The expected result of this test is for the turn count to be correct at all times.
        """
        g = Game()
        g.next_turn()

        # Assert that after the next turn has been played, the retrieved turn count is correct.
        assert g.get_turn_count() == 1
