'''
Created on 23 Oct 2013

@author: Richard and Michael

The module containing the Grid class and any derivatives of it
'''
from game_of_life.data_structures import cell

def create_empty_grid():
    '''
    Creates an empty ten-by-ten grid of cells for use in the initialisation
    of a grid object.
    
    Returns the cell collection
    '''
    cells = []
    for x in range(0, 10):
        cells.append([])
        for _y in range(0, 10):
            cells[x].append(cell.Cell())
    
    return cells

class Grid(object):
    '''
    This class represents the board on which the Game of Life will be played.
    The grid contains a number of "square" cells that have one state at any
    possible point.
    '''

    def __init__(self, grid_size=(10, 10), cell_pattern=create_empty_grid()):
        '''
        Ctor

        Initialises the grid as a two-dimensional array of "dead" cells.
        '''
        if grid_size:
            self._cells = []
            for x in range(0, grid_size[0]):
                self._cells.append([])
                for _y in range(0, grid_size[1]):
                    self._cells[x].append(cell.Cell())
                    
        if cell_pattern:
            self._cells = cell_pattern            

    def get_cells(self):
        '''
        Return the cells within the grid
        '''
        return self._cells

    def set_cells(self, cells):
        '''
        Gives the grid a collection of cells.

        Arguments:
        cells - a collection of cell objects
        '''
        self._cells = cells
