'''
Created on 23 Oct 2013

@author: Richard and Michael

The module containing the Grid class and any derivatives of it
'''
from game_of_life.engine import cell


class Grid(object):
    '''
    This class represents the board on which the Game of Life will be played.
    The grid contains a number of "square" cells that have one state at any
    possible point.
    '''

    def __init__(self, row_length=10, col_length=10):
        '''
        Ctor

        Initialises the grid as a two-dimensional array of "dead" cells.
        '''
        self._cells = []
        for x in range(0, row_length):
            self._cells.append([])
            for _y in range(0, col_length):
                self._cells[x].append(cell.Cell())

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
