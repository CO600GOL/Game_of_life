'''
Created on 23 Oct 2013

@author: Richard and Michael

This module contains the tests required for the calculator module.
'''

from game_of_life.engine import calculator


class TestCalculator(object):
    '''
    This class runs all the tests for the calculator module.
    '''

    def test_init(self):
        '''
        Tests initialisation of a calculator object.
        '''
        calc = calculator.Calculator()
        assert calc

    def test_find_neighbour_set(self):
        '''
        Tests the calculator's ability to find a set of neighbours when given
        the coordinates of a cell
        '''
        pass

    def test_next_state(self):
        '''
        Tests the ability of the calculator to calculate the next state of a
        given cell.
        '''
        pass

    def test_calculate_generation(self):
        '''
        Tests the ability of the calculator to calculate the whole next
        generation of a grid full of cells.
        '''
        pass
