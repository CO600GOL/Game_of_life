'''
Created on 20 Oct 2013

@author: Richard, Michael & Geoff

This is a module containing the Cell class.
'''

from game.data_structures.cell import Cell
from game_of_life.data_structures.states import Alive, Dead


class GolCell(Cell):
    '''
    Cell represents a single cell on a Conway's Game of Life board. It can be
    either alive or dead at an one time.
    '''

    def __init__(self, state=Dead()):
        '''
        Sets the initial state of the cell to dead.

        Keyword arguments:
        state -- Initial state of cell. Defaults to Dead
        '''
        Cell.__init__(self, state)

    def is_alive(self):
        '''
        Returns True if cell state has an alive state.
        '''
        return isinstance(self._state, Alive)
