'''
Created on 23 Oct 2013

@author: Richard and Michael
'''

import copy
from game_of_life.data_structures.states import Alive, Dead


class Calculator(object):
    '''
    This class represents the calculation engine for the Game of Life
    simulation
    '''

    def __init__(self, rule_set):
        '''
        Constructor
        '''
        self._rule_set = rule_set

    def _find_neighbour_set(self, grid, x, y):
        '''
        Returns a collection of a cells neighbours
        '''
        grid_cells = grid.get_cells()
        grid_row_length = len(grid_cells)
        grid_col_length = len(grid_cells[0])

        neighbour_cells = []

        for x_diff in range(-1, 2):
            for y_diff in range(-1, 2):
                if x_diff != 0 or y_diff != 0:
                    xx = (x + x_diff) % grid_row_length
                    yy = (y + y_diff) % grid_col_length

                    neighbour_cells.append(grid_cells[xx][yy])

        return neighbour_cells

    def _next_state(self, cell, neighbour_cells):
        '''
        Returns the next state of the cell after calculation according to the
        rule set.
        '''
        # checks the state of the cell being calculated.
        # cycles through the neighbouring cells to find the no. of alive ones.
        # checks the rule set to see which rule is applied.
        # returns the correct state of the cell in the next generation.
        born = self._rule_set.get_born_var()
        stay_one, stay_two = self._rule_set.get_stay_var()

        alive = 0
        for neighbour in neighbour_cells:
            if neighbour.get_state() == Alive():
                alive += 1

        if alive == born and (cell.get_state() == Dead()):
            return Alive()
        elif cell.get_state() == Alive() and \
                    (alive == stay_one or alive == stay_two):
            return Alive()
        else:
            return Dead()

    def calculate_generation(self, grid):
        '''
        Calculates the next generation of cells in a given grid.
        Returns the collection of cells holding the next generation.
        '''
        returned_cells = []

        for x, row in enumerate(grid.get_cells()):
            returned_cells.append([])
            for y, c in enumerate(row):
                neighbours = self._find_neighbour_set(grid, x, y)
                c = copy.copy(c)
                c.set_state(self._next_state(c, neighbours))
                returned_cells[x].append(c)

        return returned_cells
