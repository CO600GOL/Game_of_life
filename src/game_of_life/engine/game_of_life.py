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
    
    def _set_rule_set(self):
        '''
        Defines a rule set for one run through of the Game of Life
        '''
        pass

    def __init__(self):
        '''
        Ctor - Initialises the Game of Life with a rule set defined by
        the user.
        '''
        pass
    
    def set_initial_input(self):
        '''
        Stores the initial pattern input by the user.
        '''
        pass
    
    def get_initial_input(self):
        '''
        Returns the initial input from storage for further usage.
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
    
    def calculate_next_generation(self):
        '''
        Calculates the next generations of cells depending on the
        collection of cells given to it.
        '''
        pass
    
    def first_turn(self):
        '''
        Runs the first turn in the Game of Life.
        '''
        # Take initial input and passes it to the calculator
        # Calculator calculates first generation and passes it back
        # The first generation is stored in self._current_generation
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
