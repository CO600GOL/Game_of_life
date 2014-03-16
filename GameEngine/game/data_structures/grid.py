"""
This module contains the logic representing the grid on which a game is played. A grid, in this sense, is simply a
collection cells set into rows and columns. The cells can, for the purposes of the project, only be square.
"""
from game.data_structures.cell import Cell


def create_empty_grid():
    """
    This function creates an empty ten-by-ten grid for use in initialisation of a grid object.

    @return The collection of cells to use in a grid.
    """
    cells = []
    for x in range(0, 10):
        cells.append([])
        for _y in range(0, 10):
            cells[x].append(Cell())

    # Cells is a 2-dimensional array
    return cells


class Grid(object):
    """
    This class represents a grid board on which a game can be played. The grid contains a number of cells that have
    one state at any possible point.
    """

    def __init__(self, cell_pattern=create_empty_grid()):
        """
        Ctor - Initialises the grid, with a two-dimensional array of cells.

        @param cell_pattern If the a cell pattern is input as a parameter, it is that cell pattern that is set. If not
                            all the cells are set to dead.
        """
        self.set_cells(cell_pattern)

    def get_cells(self):
        """
        This pattern retrieves the cells contained within this grid.

        @return The grid cells.
        """
        return self._cells

    def set_cells(self, cells):
        """
        This method sets the cells inside the grid to the given configuration.

        @param cells The cell configuration to give to the grid.
        """
        self._cells = cells
