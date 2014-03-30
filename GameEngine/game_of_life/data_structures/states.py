"""
This module contains the logic for the possible cell states during a Game of Life.
"""

from game.data_structures.states import State


class Alive(State):
    """
    This cleass represents the cell state of being alive. It hold all information specific to this state.
    """

    def __init__(self):
        """
        Ctor - Initialises the state of being alive, which means storing all the data associated with a GoLCell being
        alive.
        """
        pass


class Dead(State):
    """
    This class represents the cell state of being dead. It hold all information specific to this state.
    """

    def __init__(self):
        """
        Ctor - Initialises the state of being dead, which means storing all the data associated with a GoLCell being
        dead.
        """
        pass
