'''
Created on 20 Oct 2013

@author: Richard & Michael

This is a module containing the Cell class.
'''

from game_of_life.data_structures import state


class Cell(object):
    '''
    Cell represents a single cell on a Conway's Game of Life board. It can be
    either alive or dead at an one time.
    '''

    def __init__(self, state=state.Dead()):
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

    def is_alive(self):
        '''
        Returns True if cell state has an alive state.
        '''
        return isinstance(self._state, state.Alive)

    def set_state(self, state):
        """
        Assign new state to cell object.

        Arguments:
        state -- new state to assign
        """
        self._state = state
