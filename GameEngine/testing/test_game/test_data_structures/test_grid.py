"""
This module contains logic that will test the data structure representing a grid game board. These tests must evaluate
whether a grid can be correctly initialised and can function correctly.
"""

from game.data_structures.grid import Grid
from game.data_structures.cell import Cell
from game.data_structures.states import State


class TestGrid(object):
    """
    This method tests the functionality of the Grid data structure.
    """

    def test_grid_init(self):
        """
        This method tests that a Grid object initialises correctly. The expected result of this test is for a Grid
        to be initialised with a number of cells, which are all of state State.
        """
        pattern = [[Cell(),
                    Cell(),
                    Cell(),
                    Cell()],
                   [Cell(),
                    Cell(),
                    Cell(),
                    Cell()],
                   [Cell(),
                    Cell(),
                    Cell(),
                    Cell()],
                   [Cell(),
                    Cell(),
                    Cell(),
                    Cell()]]

        test_grid = Grid(pattern)
        # Assert that the grid has been initialised.
        assert test_grid

        cells = test_grid.get_cells()

        for row in cells:
            # For each row of cells
            for c in row:
                # Assert that the state of a cell is State.
                assert isinstance(c.get_state(), State)

    def test_get_cells(self):
        """
        Tests the ability for the grid to return its collection of cells.

        This method tests the ability of the Grid to retrieve the cells that it contains. The expected result of this
        test is for the correct number of cells to be retrieved.
        """
        test_grid = Grid()

        cells = test_grid.get_cells()
        # Assert that the cells have been retrieved.
        assert cells

    def test_set_cells(self):
        """
        Tests the ability of the grid to store a collection of cells.

        This method tests the ability of the grid to store a collection of cells. The expected result of this test is
        for the correct cells to be set to the Grid.
        """
        test_grid = Grid()

        # Create a collection of cell objects
        # Hard coding the expectation of a 10 x 10 2D array as it will fail
        # if someone changes the keyword parameters
        s = 10
        cells = []
        for x in range(0, s):
            cells.append([])
            for y in range(0, s):
                c = Cell()
                if y % 2 == 0:
                    c.set_state(State())
                cells[x].append(c)

        test_grid.set_cells(cells)
        # Asert that the collection has been correctly stored.
        assert test_grid.get_cells()

        recieved_cells = test_grid.get_cells()
        for x, row in enumerate(recieved_cells):
            # For each row of cells
            for y, _column in enumerate(row):
                # Assert that the expected cell has been stored in this grid 'coordinate'.
                assert recieved_cells[x][y] == cells[x][y]
