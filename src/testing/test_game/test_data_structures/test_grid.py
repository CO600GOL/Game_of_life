'''
Created on 23 Oct 2013

@author: Richard and Michael

A module for testing the grid module.
'''

from game.data_structures.grid import Grid
from game.data_structures.cell import Cell
from game.data_structures.states import State


class TestGrid(object):
    '''
    Tests the functionality of the grid module.
    '''

    def test_grid_init(self):
        '''
        Tests correct initialisation of grid objects. Objects should initialise
        with a number of cells that are all dead.
        '''
        pattern = [[Cell(),
                    Cell(),
                    Cell(),
                    Cell()],
                   [Cell(),
                    Cell(),
                    Cell(),
                    Cell()],
                   [Cell(),
                    Cell(),
                    Cell(),
                    Cell()],
                   [Cell(),
                    Cell(),
                    Cell(),
                    Cell()]]

        test_grid = Grid(pattern)
        assert test_grid

        cells = test_grid.get_cells()

        for row in cells:
            for c in row:
                assert isinstance(c.get_state(), State)

    def test_get_cells(self):
        '''
        Tests the ability for the grid to return its collection of cells.
        '''
        test_grid = Grid()

        cells = test_grid.get_cells()
        assert cells

    def test_set_cells(self):
        '''
        Tests the ability of the grid to store a collection of cells.
        '''
        test_grid = Grid()

        # Create a collection of cell objects
        # Hard coding the expectation of a 10 x 10 2D array as it will fail
        # if someone changes the keyword parameters
        s = 10
        cells = []
        for x in range(0, s):
            cells.append([])
            for y in range(0, s):
                c = Cell()
                if y % 2 == 0:
                    c.set_state(State())
                cells[x].append(c)

        # Write a test to check that the collection has been stored
        test_grid.set_cells(cells)
        assert test_grid.get_cells()

        # Write a test to check that the correct collection has been stored
        recieved_cells = test_grid.get_cells()
        for x, row in enumerate(recieved_cells):
            for y, _column in enumerate(row):
                assert recieved_cells[x][y] == cells[x][y]
