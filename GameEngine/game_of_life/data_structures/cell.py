"""
This module contains the logic for the Game of Life cell, an 'intelligent' game cell that can, at the moment, be either
dead or alive.
"""

from game.data_structures.cell import Cell
from game_of_life.data_structures.states import Alive, Dead


class GolCell(Cell):
    """
    This class represents a single cell on a Conway's Game of Life board. It can either be dead or alive at any one
    time.
    """

    def __init__(self, state=Dead()):
        """
        Ctor - Initialises the cell with a state in which it can start the game of life.

        @param state The initial state of the cell. If no argument is given, defaults to dead.
        """
        Cell.__init__(self, state)

    def is_alive(self):
        """
        @return True if the cell is currently 'alive'.
        """
        return isinstance(self._state, Alive)
