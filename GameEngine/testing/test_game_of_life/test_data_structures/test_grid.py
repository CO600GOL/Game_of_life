"""
This module contains logic to test the data structure representing a Game of Life grid board. These tests should
evaluate whether the GoLGrid can be initialised correctly and can function correctly.
"""

from game_of_life.data_structures.grid import GolGrid
from game_of_life.data_structures.cell import GolCell
from game_of_life.data_structures.states import Alive, Dead


class TestGrid(object):
    """
    This class tests the functionality of the GoLGrid module.
    """

    def test_grid_init(self):
        """
        This method tests the initialisation of a GoLGrid object. The expected result of this test is that the GolGrid
        should be initialised with a number of GoLCells, which are all dead.
        """
        pattern = [[GolCell(),
                    GolCell(),
                    GolCell(),
                    GolCell()],
                   [GolCell(),
                    GolCell(),
                    GolCell(),
                    GolCell()],
                   [GolCell(),
                    GolCell(),
                    GolCell(),
                    GolCell()],
                   [GolCell(),
                    GolCell(),
                    GolCell(),
                    GolCell()]]

        test_grid = GolGrid(pattern)
        # Assert that the GoLGrid has been initialised.
        assert test_grid

        cells = test_grid.get_cells()

        for row in cells:
            # For each row of cells.
            for c in row:
                # Assert that the state of each cell is dead, as it should be.
                assert isinstance(c.get_state(), Dead)

    def test_get_cells(self):
        """
        This method tests the ability of the GoLGrid to retrieve all of its GoLCells. The expected result of this
        test is that the GoLCells are correctly retrieved.
        """
        test_grid = GolGrid()

        cells = test_grid.get_cells()
        # Assert that a collection of cells has been correctly retrieved.
        assert cells

    def test_set_cells(self):
        """
        This method tests the ability of the GoLGrid to store a collection of GoLCells. The expected result of this
        tests is that a collection of GoLCells can be correctly set.
        """
        test_grid = GolGrid()

        # Create a collection of GolCell objects
        # Hard coding the expectation of a 10 x 10 2D array as it will fail
        # if someone changes the keyword parameters
        s = 10
        cells = []
        for x in range(0, s):
            cells.append([])
            for y in range(0, s):
                c = GolCell()
                if y % 2 == 0:
                    c.set_state(Alive())
                cells[x].append(c)

        test_grid.set_cells(cells)
        # Assert that the collection of GoLCells has been set correctly.
        assert test_grid.get_cells()

        recieved_cells = test_grid.get_cells()
        for x, row in enumerate(recieved_cells):
            # For each row of cells.
            for y, _column in enumerate(row):
                # Assert that the GoLCell at these 'coordinates' is the correct GoLCell.
                assert recieved_cells[x][y] == cells[x][y]

    def test_get_no_alive_cells(self):
        """
        Tests the ability of the grid to retrieve the number of living cells.

        This method tests the ability of the GoLGrid to retrieve the number of living GoLCells it currently has.
        """
        test_grid = GolGrid()
        alive_cells = test_grid.get_no_alive_cells()
        # At this point, none of the GoLCells should be alive. Assert this is true.
        assert alive_cells == 0

        # Create another set of cells, half of which are alive.
        s = 10
        cells = []
        for x in range(0, s):
            cells.append([])
            for y in range(0, s):
                c = GolCell()
                if y % 2 == 0:
                    # Make every second cell alive.
                    c.set_state(Alive())
                cells[x].append(c)

        test_grid = GolGrid(cells)
        alive_cells = test_grid.get_no_alive_cells()
        # Assert that the correct number of cells have been retrieved.
        assert alive_cells == (s * s) / 2
