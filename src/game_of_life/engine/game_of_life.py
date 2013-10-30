'''
Created on 28.10.2013

@author: Michael and Geoff

This module contains the logic and functionality for the Game of Life.
It works as the complete engine for the game.
'''


class GameOfLife(object):
    '''
    This class represents the Game of Life with a defined, persistent
    rule set. 
    '''

    def __init__(self):
        '''
        Ctor - Initialises the Game of Life with a rule set defined by
        the user.
        '''
        pass
    
    def _set_current_generation(self):
        '''
        Stores the current generation of cells for use later on.
        '''
        pass
    
    def get_current_generation(self):
        '''
        Returns the current generation of cells from storage.
        '''
        pass
    
    def _set_next_generation(self):
        '''
        Stores the next generation of cells calculated by the
        calculator for use later on.
        '''
        pass
    
    def get_next_generation(self):
        '''
        Returns the next generation of cells from storage for
        further use.
        '''
    
    def _calculate_next_generation(self):
        '''
        Calculates the next generations of cells depending on the
        collection of cells given to it.
        '''
        pass
    
    def next_turn(self):
        '''
        Runs the next turn in the Game of life.
        '''
        # Takes the current generation and passes to calculator
        # Calculator calculates the next generation and passes it back
        # Stores next generation in self._next_generation
        # Passes current generation back to Game Control to be shown on
        # the GUI.
        # The state in of the next generation is stored as the current
        # generation
        pass
