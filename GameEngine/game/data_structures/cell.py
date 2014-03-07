'''
Created on 20 Oct 2013

@author: Richard, Michael & Geoff.

This is a module containing the Cell class.
'''

from game.data_structures.states import State


class Cell(object):
    '''
    Cell represents a single cell on a Conway's Game of Life board. It can be
    either alive or dead at an one time.
    '''

    def __init__(self, state=State()):
        '''
        Sets the initial state of the cell to dead.

        Keyword arguments:
        state -- Initial state of cell. Defaults to Dead
        '''
        self._state = state

    def get_state(self):
        """
        Returns the current state of the cell
        """
        return self._state

    def set_state(self, state):
        """
        Assign new state to cell object.

        Arguments:
        state -- new state to assign
        """
        self._state = state
