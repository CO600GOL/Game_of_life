'''
Created on 23 Oct 2013

@author: Richard and Michael
'''


class Calculator(object):
    '''
    This class represents the calculation engine for the Game of Life
    simulation
    '''

    def __init__(self, rule_set):
        '''
        Constructor
        '''
        pass

    def _find_neighbour_set(self, x, y):
        '''
        Returns a collection of a cells neighbours
        '''
        pass

    def _next_state(self, cells):
        '''
        Returns the next state of the cell after calculation according to the
        rule set.
        '''
        pass

    def calculate_generation(self, grid):
        '''
        Calculates the next generation of cells in a given grid.
        '''
        pass
