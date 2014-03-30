"""
This module contains logic that tests the game controllers. These tests must evaluate wether the controllers can be
correctly initialised and can function correctly. To some extent, they must also check that external software is not
receiving any data it shouldn't.
"""

from game.game_controllers.game_controllers import GameController
from game.game_controllers.game_controllers import GameOfLifeController
from game.game import Game
from game_of_life.engine.game_of_life import GameOfLife
from game_of_life.data_structures.states import Alive, Dead
from game_of_life.data_structures.grid import GolGrid


def create_initial_input():
    """
    This function abstracts the creation of a string object that can act as initial input, as it would be input by
    a user or an external piece of software.
    """
    init_input = """\
-*-*-*-*-*
*-*-*-*-*-
-*--------
--*-------
---*------
----*-----
-----*----
*-*-*-*-*-
-*-*-*-*-*
*-*-*-*-*-"""

    return init_input


class TestGameController(object):
    """
    This class tests the functionality of the GameController class.
    """

    def test_init_(self):
        """
        This method tests initialisation of a GameController. The expected result of this test is for the GameController
        to be correctly initialised.
        """
        gc = GameController()
        # Assert that the GameController has been initialised.
        assert gc

    def test_set_up_game(self):
        """
        This method tests whether the GameController can correctly set up the game it is meant to be playing. The
        expected result of this test is for the GameController's game to be set up correctly.
        """
        gc = GameController()
        gc.set_up_game()

        # Assert that the GameController's game has been initialised, and that it has been initialised as the right
        # type of game.
        assert isinstance(gc._game, Game)

    def test_get_game(self):
        """
        This method tests the ability of the GameController to retrieve the game it is currently playing. The expected
        result of this test is for the GameController's game to be correctly retrieved.
        """
        gc = GameController()
        gc.set_up_game()

        # Assert that the game has been retrieved.
        assert gc.get_game()

    def test_play_next_turn(self):
        """
        This method tests the ability of the GameController to play a single turn of its current game. The expected
        result of this test is for the GameController to correclty play one turn of its current game.
        """
        gc = GameController()
        gc.set_up_game()

        gc.play_next_turn()

        # If the next turn has been played, the turn count should now be 1. Assert this is true.
        assert gc.get_game().get_turn_count() == 1


class TestGameOfLifeController(object):
    """
    This class tests the functionality of the GameOfLifeController class.
    """

    def test_init_(self):
        """
        This method tests initialisation of a GameOfLifeController. The expected result of this test is for a
        GameOfLifeController to be correctly initialised.
        """
        golc = GameOfLifeController()

        # Assert that the Controller has been initialised.
        assert golc

    def test_set_up_game(self):
        """
        This method tests that the GameOfLife controller can correctly set up a Game of Life. The expected result of
        this test is for a Game of Life to be correctly prepared.
        """
        golc = GameOfLifeController()

        # Set up initial input
        init_input = create_initial_input()

        # Set up the Game of Life
        golc.set_up_game(init_input)

        # Assert that the Controller's game has been initialised, and that it has been initialised as a Game of Life.
        assert isinstance(golc._game, GameOfLife)

        # We should also test that the Game Controller has correctly translated the initial input into something only
        # it can understand.
        init_input = init_input.split("\n")
        for x, row in enumerate(init_input):
            # For each row of cells.
            for y, _col in enumerate(row):
                if init_input[x][y] == "*":
                    # Assert that the cell at these 'coordinates' is alive.
                    assert golc.get_game().get_current_generation().get_cells()[x][y].get_state() == Alive()
                else:
                    # Assert that the cell at these 'coordinates' is dead.
                    assert golc.get_game().get_current_generation().get_cells()[x][y].get_state() == Dead()

    def test_play_next_turn(self):
        """
        This method tests that the Controller can correctly play one turn of the Game of Life. The expected result of
        this test is for the next turn of the Game of Life to be correctly played.
        """
        golc = GameOfLifeController()
        golc.set_up_game(create_initial_input())
        golc.play_next_turn()

        # Assert first that the turn count has been increased to 1.
        assert golc.get_game().get_turn_count() == 1

        # Write a simulation grid object to test the next generation in our given test.
        next_gen = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # Test that it matches the calculated pattern.
        for x, row in enumerate(next_gen):
            # For each row in a cell
            for y, _col in enumerate(row):
                if next_gen[x][y] == 0:
                    # Assert that the cell at these 'coordinates' is dead.
                    assert golc.get_game().get_current_generation().get_cells()[x][y].get_state() == Dead()
                else:
                    # Assert that the cell at these 'coordinates' is alive.
                    assert golc.get_game().get_current_generation().get_cells()[x][y].get_state() == Alive()

    def test_get_turn_count(self):
        """
        This method tests the ability of the Controller to retrieve the number of turns that have been played so far.
        The expected result of this test is for the correct turn count to be retrieved at all times.
        """
        golc = GameOfLifeController()
        golc.set_up_game(create_initial_input())

        for i in range(0, 9):
            # For each turn, assert that the turn count is correct (starts at 0)
            assert golc.get_turn_count() == i
            golc.play_next_turn()

    def test_get_current_generation(self):
        """
        This method tests the ability of the Controller to retrieve the Game of Life's current generation. The
        expected result of this test is for the Game of Life's current generation to be correctly retrieved as a
        GolGrid object.
        """
        golc = GameOfLifeController()
        golc.set_up_game(create_initial_input())

        current_gen = golc.get_current_generation()
        # Assert that the current generation has been retrieved, and that it has been retrieved as the correct Grid
        # type.
        assert current_gen and isinstance(current_gen, GolGrid)

    def test_get_current_generation_output(self):
        """
        Tests the game controller's ability to output the current
        generation as a string.

        This method tests the Controller's ability to retrieve the Game of Life#s current generation. The expected
        result of this test is for the Game of Life's current generation to be correctly retrieved as a string object.
        """
        golc = GameOfLifeController()
        golc.set_up_game(create_initial_input())

        current_gen = golc.get_current_generation(output=True)
        # Assert that the current generation has been retrieved, and that it has been retrieved as the correct string
        # type.
        assert current_gen and isinstance(current_gen, str)