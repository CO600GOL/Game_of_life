'''
Created on 20 Oct 2013

@author: Richard and Michael

This is a module containing the State class and all classes derived from it.
'''

from game.data_structures.states import State


class Alive(State):
    """
    This class represents the 'alive' state.
    """

    def __init__(self):
        """
        Ctor

        Initialises the state of being alive and initialises all the data
        associated with a cell being alive. (Placeholder)
        """
        pass


class Dead(State):
    """
    This class represents the 'dead' state.
    """

    def __init__(self):
        """
        Ctor

        Initialises the state of being dead and initialises all the data
        associated with a cell being dead. (Placeholder)
        """
        pass
