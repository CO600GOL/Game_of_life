"""
This module contains the logic representing board cells. It controls the state of an individual cell, storing any
data important to that state.
"""

from game.data_structures.states import State


class Cell(object):
    """
    This class represents a single cell on a game board. A cell has a state, which controls whether the light is on,
    and possibly in the future, things such as the colour and intensity of the light.
    """

    def __init__(self, state=State()):
        """
        Ctor - initialises the cell and its state.

        @param state The initial state of the cell. Defaults to 'dead' for the purposes of the Game of Life.
        """
        self._state = state

    def get_state(self):
        """
        This method retrieves the current state of the cell.

        @return the current state of the cell.
        """
        return self._state

    def set_state(self, state):
        """
        This method assigns a new state to the cell.

        @param state the new state with which to assign the cell.
        """
        self._state = state
