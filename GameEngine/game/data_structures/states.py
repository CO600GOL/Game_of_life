"""
This module contains the logic representing the cell states available during a game. A state may hold information about
what the cell it belongs to should do while remaining in that state.
"""


class State(object):
    """
    This abstract class represents the state of a cell at any given time. It acts as a backbone for all states,
    implementing all shared functionality.
    """

    def __init__(self):
        """
        Ctor - Initialises a state, storing all state data for use.
        """
        pass

    def __eq__(self, other):
        """
        This method overrides the object.__eq__ method to allow boolean equality comparison for state objects.

        @return True If two objects are of the same class.
        """
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        """
        This method overrides the object.__ne__ method to allow boolean equality comparison for state objects.

        @return True if two objects are not of the same class.
        """
        return not isinstance(other, self.__class__)
