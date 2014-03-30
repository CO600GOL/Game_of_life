"""
This module contains logic for testing the Game of Life engine. These tests must evaluate whether the game engine can
be correctly initialised and can function correctly.
"""

from game_of_life.data_structures.grid import GolGrid
from game_of_life.data_structures.cell import GolCell
from game_of_life.data_structures.states import Alive
from game_of_life.engine import game_of_life, rule_sets

def set_current_generation():
    """
    This function creates a pattern of cells to use as the game engine's 'current generation'.

    @return cells The collection of GoLCells to represent the current generation.
    """
    cells = [[GolCell(),
              GolCell(),
              GolCell(Alive()),
              GolCell()],
             [GolCell(Alive()),
              GolCell(Alive()),
              GolCell(Alive()),
              GolCell()],
             [GolCell(),
              GolCell(),
              GolCell(),
              GolCell()],
             [GolCell(Alive()),
              GolCell(),
              GolCell(Alive()),
              GolCell()]]

    return cells


def set_next_generation():
    """
    This method creates a pattern of cells to use as the game engine's 'next generation'.

    @return cells The collection of GoLCells to represent the next generation.
    """

    cells = [[GolCell(Alive()),
              GolCell(),
              GolCell(Alive()),
              GolCell()],
             [GolCell(),
              GolCell(Alive()),
              GolCell(Alive()),
              GolCell(Alive())],
             [GolCell(Alive()),
              GolCell(),
              GolCell(Alive()),
              GolCell()],
             [GolCell(),
              GolCell(Alive()),
              GolCell(),
              GolCell(Alive())]]

    return cells


class TestGameOfLife(object):
    """
    This class tests the functionality of the GameOfLife class.
    """

    def test_init(self):
        """
        Tests initialisation of a GameOfLife object. Also tests that
        the GameOfLife object initialises with the correct rule set.

        This method tests the initialisation of a GameOfLife object. The expected result of this test is for the
        game engine to be correctly initialised, with the correct game engine.
        """
        ini_gr = GolGrid()
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard(), ini_gr)
        # Assert the game engine has been initialised.
        assert gol

        rs = gol._rule_set
        # Assert the game engine's rule set has been correctly initialised.
        assert isinstance(rs, rule_sets.RuleSetStandard)

    def test_set_current_generation(self):
        """
        This method tests the ability of the game engine to set the Game of Life's current generation. The expected
        result of this test is for the current generation to be correctly set.
        """
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard(), GolGrid())

        # Create a grid and give it a pattern of cells:
        # ddad
        # aaad
        # dddd
        # adad
        gr = GolGrid(set_current_generation())

        gol._set_current_generation(gr)

        # Assert the Game of Life's current generation has been set.
        assert gol._current_generation

        test_pattern = set_current_generation()
        for x, row in enumerate(gol._current_generation.get_cells()):
            # For each row of cells.
            for y, c in enumerate(row):
                # Assert that a cell's state is the correct state.
                assert c.get_state() == test_pattern[x][y].get_state()

    def test_get_current_generation(self):
        """
        This method tests the ability of the game engine to retrieve the Game of Life's current generation. The expected
        result of this test is for the current generation to be correctly set.
        """
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard(), GolGrid())

        # Create a grid and give it a pattern of cells:
        # ddad
        # aaad
        # dddd
        # adad
        gr = GolGrid(set_current_generation())

        gol._set_current_generation(gr)

        retrieved_pattern = gol.get_current_generation()
        # Assert the current generation has been correctly retrieved.
        assert retrieved_pattern

        test_pattern = set_current_generation()
        for x, row in enumerate(retrieved_pattern.get_cells()):
            # For each row of cells.
            for y, c in enumerate(row):
                # Assert that a cell's state is the correct state.
                assert c.get_state() == test_pattern[x][y].get_state()

    def test_set_next_generation(self):
        """
        This method tests the ability of the game engine to set the Game of Life's next generation. The expected
        result of this test is for the next generation to be correctly set.
        """
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard(), GolGrid())

        # Create a grid and give it a pattern of cells:
        # adad
        # daaa
        # adad
        # dada
        gr = GolGrid(set_next_generation())

        gol._set_next_generation(gr)

        # Assert the that the Game of Life's next generation has been correctly set.
        assert gol._next_generation

        test_pattern = set_next_generation()
        for x, row in enumerate(gol._next_generation.get_cells()):
            # For each row of cells.
            for y, c in enumerate(row):
                # Assert a cell's state is the correct state.
                assert c.get_state() == test_pattern[x][y].get_state()

    def test_get_next_generation(self):
        """
        This method tests the ability of the game engine to retrieve the Game of Life's next generation. The expected
        result of this test is for the next generation to be correctly set.
        """
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard(), GolGrid())

        # Create a grid and give it a pattern of cells:
        # adad
        # daaa
        # adad
        # dada
        gr = GolGrid(set_next_generation())

        gol._set_next_generation(gr)

        retrieved_pattern = gol.get_next_generation()
        # Assert that the Game of Life's next generation has been correctly retrieved.
        assert retrieved_pattern

        test_pattern = set_next_generation()
        for x, row in enumerate(retrieved_pattern.get_cells()):
            # For each row of cells.
            for y, c in enumerate(row):
                # Assert a cell's state is the correct state.
                assert c.get_state() == test_pattern[x][y].get_state()

    def test_calculate_next_generation(self):
        """
        This method tests the ability of the game engine to calculate the next generation of the Game of Life. The
        expected result of this test is for the next generation to be correctly calculated.
        """
        # Create a grid and give it a pattern of cells:
        # ddad
        # aaad
        # dddd
        # adad
        # Represents the 'current generation'
        cur_gen = GolGrid(set_current_generation())

        # Create a grid and give it a pattern of cells:
        # adad
        # daaa
        # adad
        # dada
        # Represents the correct 'next generation'
        nex_gen = GolGrid(set_next_generation())

        # Give the Game of Life the first grid as the current generation
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard(), cur_gen)

        res = gol._calculate_next_generation(cur_gen)
        # Assert that the game engine has calculated a new pattern.
        assert res

        for x, row in enumerate(res.get_cells()):
            # For each row of cells.
            for y, c in enumerate(row):
                # Assert that a cell has the correct state.
                assert c.get_state() == nex_gen.get_cells()[x][y].get_state()

    def test_next_turn(self):
        """
        This method tests the ability of the game engine to play the next turn of the Game of Life. The expected
        result of this test is for the next turn to be played correctly, with the next generation of cells to be
        correct.
        """
        # Create a grid and give it a pattern of cells:
        # ddad
        # aaad
        # dddd
        # adad
        # Represents the 'current generation'
        cur_gen = GolGrid(set_current_generation())

        # Create a grid and give it a pattern of cells:
        # adad
        # daaa
        # adad
        # dada
        # Represents the correct 'next' generation
        nex_gen = GolGrid(set_next_generation())

        # Give the Game of life the first table as the current generation
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard(), cur_gen)

        # Run the next turn of the game.
        gol.next_turn()

        retrieved_pattern = gol.get_current_generation()
        for x, row in enumerate(retrieved_pattern.get_cells()):
            # For each row of cells.
            for y, c in enumerate(row):
                # Assert that a cell has the right state.
                assert c.get_state() == nex_gen.get_cells()[x][y].get_state()

    def test_get_turn_count(self):
        """
        This method tests the ability of the game engine to retrieve the number of turns that have been played. The
        expeted result of this test is for the correct number of turns to be retrieved.
        """
        cur_gen = GolGrid(set_current_generation())
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard(), cur_gen)

        for _x in range(0, 3):
            gol.next_turn()

        # After three turns, assert that the turn count is 3.
        assert gol.get_turn_count() == 3

    def test_is_game_forsaken(self):
        """
        This method tests the game engine's ability to evaluate the the Game of Life is over because all cells are
        dead.
        """
        cell_pattern = [[GolCell(Alive())]]
        cur_gen = GolGrid(cell_pattern)

        # Give the Game of Life the grid as the current generation
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard(), cur_gen)

        # Assert that the game has not finished because not all cells are dead.
        assert not gol.is_game_forsaken()

        # Run next turn (cell should die)
        gol.next_turn()

        # Assert that the game has ended because all cells are dead.
        assert gol.is_game_forsaken()
