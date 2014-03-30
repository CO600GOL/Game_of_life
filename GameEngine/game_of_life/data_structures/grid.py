"""
This class contains the logic for the Game of Life grid, the board on which the Game of Life is played. A GoL grid is
simply a collection of GoL cells.
"""
from game.data_structures.grid import Grid
from game_of_life.data_structures.cell import GolCell


def create_empty_grid():
    """
    This function creates an empty 10x10 grid of 'dead' cells for use in initialisation of a Grid object.

    @returns The collection of cells to be given to the Grid object.
    """
    cells = []
    for x in range(0, 10):
        cells.append([])
        for _y in range(0, 10):
            cells[x].append(GolCell())

    # cells is a two-dimensional array of GoLCells.
    return cells


class GolGrid(object):
    """
    This class represents the board on which the Game of Life will be played. The grid contains a number of "square"
    cells that have one state at any possible point.
    """

    def __init__(self, cell_pattern=create_empty_grid()):
        """
        Ctor - initialises the grid as a two-dimensional array of GoLCells.

        @param cell_pattern If the cell pattern is given to this method as a parameter, it is used as the initial
                            cell configuration for the grid, otherwise, all the cells in the grid are set to dead.
        """
        Grid.__init__(self, cell_pattern)

    def get_cells(self):
        """
        This method retrieves the cells that make up this grid.

        @return The cell collection for the grid.
        """
        return self._cells

    def set_cells(self, cells):
        """
        This method sets the grid to have the specified cell collection.

        @param cells The new collection of cells to be set to the grid.
        """
        Grid.set_cells(self, cells)

        self._no_alive_cells = 0
        for row in self._cells:
            for cell in row:
                if cell.is_alive():
                    self._no_alive_cells += 1

    def get_no_alive_cells(self):
        """"
        This method retrieves the number of cells that currently hold the 'alive' state.

        @return The number of living cells.
        """
        return self._no_alive_cells
