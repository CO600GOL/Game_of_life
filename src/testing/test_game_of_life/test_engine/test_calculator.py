'''
Created on 23 Oct 2013

@author: Richard and Michael

This module contains the tests required for the calculator module.
'''

import math

from game_of_life.data_structures.grid import GolGrid
from game_of_life.data_structures.cell import GolCell
from game_of_life.data_structures.states import Alive, Dead
from game_of_life.engine import calculator, rule_sets

GRID_ROW_LEN = 4
GRID_COL_LEN = 4


def get_rule_set():
    '''
    Creates and returns a rule set standard to Conway's Game of Life
    '''
    return rule_sets.RuleSet(3, (2, 3))


def get_grid():
    '''
    Creates and returns a grid to use for testing purposes.
    '''
    return GolGrid([[GolCell() for _col in range(0, GRID_COL_LEN)]
                                   for _row in range(0, GRID_ROW_LEN)])


class TestCalculator(object):
    '''
    This class runs all the tests for the calculator module.
    '''

    def test_init(self):
        '''
        Tests initialisation of a calculator object.
        '''
        rs = get_rule_set()
        calc = calculator.Calculator(rs)
        assert calc

    def test_find_neighbour_set(self):
        '''
        Tests the calculator's ability to find a set of neighbours when given
        the coordinates of a cell
        '''
        rs = get_rule_set()
        calc = calculator.Calculator(rs)

        gr = get_grid()
        cells = gr.get_cells()
        for x in range(0, GRID_ROW_LEN):
            for y in range(0, GRID_COL_LEN):
                neighbour_cells = calc._find_neighbour_set(gr, x, y)

                #======================================================================
                # Loops through the cells that should not be returned as neighbours
                # and checks that they have not been returned as neighbours.
                # Warning: This test may break if a grid of more than 4 x 4 is used for
                # testing. The development team will work on this.
                #======================================================================
                inter_x = (x + math.ceil(GRID_ROW_LEN / 2)) % GRID_ROW_LEN
                inter_y = (y + math.ceil(GRID_COL_LEN / 2)) % GRID_COL_LEN

                for x in range(0, GRID_ROW_LEN):
                    for x_not_in in range(0, GRID_ROW_LEN):
                        assert cells[x_not_in][inter_y] not in neighbour_cells

                for y in range(0, GRID_COL_LEN):
                    for y_not_in in range(0, GRID_COL_LEN):
                        assert cells[inter_x][y_not_in] not in neighbour_cells

    def test_next_state(self):
        '''
        Tests the ability of the calculator to calculate the next state of a
        given cell.
        '''
        # Finds the state of the cell to be tested.
        # Finds the no. of alive cells within its neighbours.
        # Checks the rule set to see how it reacts.
        # Change state accordingly.
        rs = get_rule_set()
        calc = calculator.Calculator(rs)

        checked_cell = GolCell()
        #======================================================================
        # 1. Collection of 8 neighbours and one being checked. Test Starvation
        #     - Should result in dead
        #======================================================================
        checked_cell.set_state(Alive())
        neighbours = [GolCell(),
                      GolCell(Alive()),
                      GolCell(),
                      GolCell(),
                      GolCell(),
                      GolCell(),
                      GolCell(),
                      GolCell()]

        next_state = calc._next_state(checked_cell, neighbours)
        assert isinstance(next_state, Dead)

        #======================================================================
        # 2. Collection of 8 neighbours and one being checked. Test stay alive
        #     - Should result in alive
        #======================================================================
        checked_cell.set_state(Alive())
        neighbours = [GolCell(),
                      GolCell(Alive()),
                      GolCell(),
                      GolCell(Alive()),
                      GolCell(),
                      GolCell(),
                      GolCell(),
                      GolCell()]

        next_state = calc._next_state(checked_cell, neighbours)
        assert isinstance(next_state, Alive)

        #======================================================================
        # 3. Collection of 8 neighbours and one being checked.
        # Test over-population
        #    - Should result in dead
        #======================================================================
        checked_cell.set_state(Alive())
        neighbours = [GolCell(),
                      GolCell(Alive()),
                      GolCell(),
                      GolCell(Alive()),
                      GolCell(Alive()),
                      GolCell(),
                      GolCell(Alive()),
                      GolCell()]

        next_state = calc._next_state(checked_cell, neighbours)
        assert isinstance(next_state, Dead)

        #======================================================================
        # 4. Collection of 8 neighbours and one being checked. Test born
        #     - Should result in alive
        #======================================================================
        checked_cell.set_state(Dead())
        neighbours = [GolCell(),
                      GolCell(Alive()),
                      GolCell(),
                      GolCell(),
                      GolCell(Alive()),
                      GolCell(),
                      GolCell(Alive()),
                      GolCell()]

        next_state = calc._next_state(checked_cell, neighbours)
        assert isinstance(next_state, Alive)

    def test_calculate_generation(self):
        '''
        Tests the ability of the calculator to calculate the whole next
        generation of a grid full of cells.
        '''
        rs = get_rule_set()
        calc = calculator.Calculator(rs)
        gr = get_grid()

        # Make grid with pattern: (d=dead, a=alive)
        # dada
        # ddad
        # dadd
        # dddd
        test_pattern = [[GolCell(),
                         GolCell(Alive()),
                         GolCell(),
                         GolCell(Alive())],
                        [GolCell(),
                         GolCell(),
                         GolCell(Alive()),
                         GolCell()],
                        [GolCell(),
                         GolCell(Alive()),
                         GolCell(),
                         GolCell()],
                        [GolCell(),
                         GolCell(),
                         GolCell(),
                         GolCell()]]

        gr.set_cells(test_pattern)

        # Make grid with pattern: (d=dead, a=alive)
        # ddad
        # aaad
        # dddd
        # adad
        check_pattern = [[GolCell(),
                          GolCell(),
                          GolCell(Alive()),
                          GolCell()],
                         [GolCell(Alive()),
                          GolCell(Alive()),
                          GolCell(Alive()),
                          GolCell()],
                         [GolCell(),
                          GolCell(),
                          GolCell(),
                          GolCell()],
                         [GolCell(Alive()),
                          GolCell(),
                          GolCell(Alive()),
                          GolCell()]]

        # Compare the resulting pattern with the expected pattern.
        result_pattern = calc.calculate_generation(gr)
        for x, row in enumerate(result_pattern):
            for y, c in enumerate(row):
                assert c.get_state() == check_pattern[x][y].get_state()
