"""
This module contains logic for testing the Game of Life engine's calculator. These tests must evaluate whether the
calculator can be correctly initialised and can function correctly.
"""

import math

from game_of_life.data_structures.grid import GolGrid
from game_of_life.data_structures.cell import GolCell
from game_of_life.data_structures.states import Alive, Dead
from game_of_life.engine import calculator, rule_sets

# For the sake of testing, make the grid a 4x4
GRID_ROW_LEN = 4
GRID_COL_LEN = 4


def get_rule_set():
    """
    This function creates the standard Game of Life rule set.
    """
    return rule_sets.RuleSet(3, (2, 3))


def get_grid():
    """
    This function creates a grid for use during tests.
    """
    return GolGrid([[GolCell() for _col in range(0, GRID_COL_LEN)]
                                   for _row in range(0, GRID_ROW_LEN)])


class TestCalculator(object):
    """
    This class tests the functionality of the Calculator class.
    """

    def test_init(self):
        """
        This method tests initialisation of a Calculator object. The expected result of this test is for the
        calculator to be initialised correctly.
        """
        rs = get_rule_set()
        calc = calculator.Calculator(rs)

        # Assert the Calculator has been initialised.
        assert calc

    def test_find_neighbour_set(self):
        """
        This method tests the ability of the calculator to calculate the set of neighbours around a given cell. The
        expected result of this method is for the calculator to be able to evaluate the neighbours correctly.
        """
        rs = get_rule_set()
        calc = calculator.Calculator(rs)

        gr = get_grid()
        cells = gr.get_cells()
        for x in range(0, GRID_ROW_LEN):
            for y in range(0, GRID_COL_LEN):
                # Adds the neighbours of the cell at these 'coordinates' to the collectopn.
                neighbour_cells = calc._find_neighbour_set(gr, x, y)

                #======================================================================
                # Loops through the cells that should not be returned as neighbours and checks that they have not been
                # returned as neighbours.
                # Warning: This test may break if a grid of more than 4 x 4 is used for testing. The development team
                # may work on this.
                #======================================================================
                inter_x = (x + math.ceil(GRID_ROW_LEN / 2)) % GRID_ROW_LEN
                inter_y = (y + math.ceil(GRID_COL_LEN / 2)) % GRID_COL_LEN

                for x in range(0, GRID_ROW_LEN):
                    for x_not_in in range(0, GRID_ROW_LEN):
                        # Assert that the given cell from the 2D array is not a neighbour of the cell being tested.
                        assert cells[x_not_in][inter_y] not in neighbour_cells

                for y in range(0, GRID_COL_LEN):
                    for y_not_in in range(0, GRID_COL_LEN):
                        # Assert that the given cell from the 2D array is not a neighbour of the cell being tested.
                        assert cells[inter_x][y_not_in] not in neighbour_cells

    def test_next_state(self):
        """
        This method tests the ability of the calculator to calculate the next state of a given cell. The expected
        result of this test is for the cell's next state to be correctly calculated.
        """
        rs = get_rule_set()
        calc = calculator.Calculator(rs)

        checked_cell = GolCell()
        #======================================================================
        # 1. Collection of 8 neighbours and one being checked. Test Starvation
        #     - Should result in dead
        #======================================================================
        checked_cell.set_state(Alive())
        neighbours = [GolCell(),
                      GolCell(Alive()),
                      GolCell(),
                      GolCell(),
                      GolCell(),
                      GolCell(),
                      GolCell(),
                      GolCell()]

        next_state = calc._next_state(checked_cell, neighbours)
        # Assert that the cell's next state is dead.
        assert isinstance(next_state, Dead)

        #======================================================================
        # 2. Collection of 8 neighbours and one being checked. Test stay alive
        #     - Should result in alive
        #======================================================================
        checked_cell.set_state(Alive())
        neighbours = [GolCell(),
                      GolCell(Alive()),
                      GolCell(),
                      GolCell(Alive()),
                      GolCell(),
                      GolCell(),
                      GolCell(),
                      GolCell()]

        next_state = calc._next_state(checked_cell, neighbours)
        # Assert that the cell's next state is alive.
        assert isinstance(next_state, Alive)

        #======================================================================
        # 3. Collection of 8 neighbours and one being checked.
        # Test over-population
        #    - Should result in dead
        #======================================================================
        checked_cell.set_state(Alive())
        neighbours = [GolCell(),
                      GolCell(Alive()),
                      GolCell(),
                      GolCell(Alive()),
                      GolCell(Alive()),
                      GolCell(),
                      GolCell(Alive()),
                      GolCell()]

        next_state = calc._next_state(checked_cell, neighbours)
        # Assert that the cell's next state is dead.
        assert isinstance(next_state, Dead)

        #======================================================================
        # 4. Collection of 8 neighbours and one being checked. Test born
        #     - Should result in alive
        #======================================================================
        checked_cell.set_state(Dead())
        neighbours = [GolCell(),
                      GolCell(Alive()),
                      GolCell(),
                      GolCell(),
                      GolCell(Alive()),
                      GolCell(),
                      GolCell(Alive()),
                      GolCell()]

        next_state = calc._next_state(checked_cell, neighbours)
        # Assert that the cell's next state is alive.
        assert isinstance(next_state, Alive)

    def test_calculate_generation(self):
        """
        This method tests the ability of the calculator to calculate the next state of every cell in a grid. The
        expected result of this test is for the next generation to be correctly calculated.
        """
        rs = get_rule_set()
        calc = calculator.Calculator(rs)
        gr = get_grid()

        # Make grid with pattern: (d=dead, a=alive)
        # dada
        # ddad
        # dadd
        # dddd
        test_pattern = [[GolCell(),
                         GolCell(Alive()),
                         GolCell(),
                         GolCell(Alive())],
                        [GolCell(),
                         GolCell(),
                         GolCell(Alive()),
                         GolCell()],
                        [GolCell(),
                         GolCell(Alive()),
                         GolCell(),
                         GolCell()],
                        [GolCell(),
                         GolCell(),
                         GolCell(),
                         GolCell()]]

        gr.set_cells(test_pattern)

        # Make grid with pattern: (d=dead, a=alive)
        # ddad
        # aaad
        # dddd
        # adad
        check_pattern = [[GolCell(),
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

        # Compare the resulting pattern with the expected pattern.
        result_pattern = calc.calculate_generation(gr)
        for x, row in enumerate(result_pattern):
            # For each row in the grid.
            for y, c in enumerate(row):
                # Assert a cell has the correct cell when checked against the testing grid.
                assert c.get_state() == check_pattern[x][y].get_state()
