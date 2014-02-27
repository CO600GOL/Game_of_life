'''
Created on 20 Oct 2013

@author: Richard and Michael

This is a module containing the State class and all classes derived from it.
'''


class State(object):
    """
    This class represents the state of a cell at any given time.
    NOTE: This class is abstract.
    """

    def __init__(self):
        """
        Ctor (Constructor)

        Initialises a state, readying all state data for use by the game
        engine. (Placeholder)
        """
        pass

    def __eq__(self, other):
        '''
        Allow boolean equality comparison of state object.
        Returns true if objects are the same class.
        '''
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        '''
        Allow boolean equality comparison of state object.
        Returns true if two objects are not the same class.
        '''
        return not isinstance(other, self.__class__)
