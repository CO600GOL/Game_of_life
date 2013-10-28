'''
Created on 28.10.2013

@author: Michael and Geoff

This module contains and runs all the tests for the game_of_life module.
'''

from game_of_life.data_structures import grid, cell, state
from game_of_life.engine import game_of_life, rule_sets


class TestGameOfLife(object):
    '''
    This class contains and runs the tests for the GameOfLife class in the
    game_of_life module.
    '''
    
    def set_cells(self):
        '''
        Returns a pattern of cells to use in testing.
        '''
        cells = [[cell.Cell(),
                  cell.Cell(state.Alive()),
                  cell.Cell(),
                  cell.Cell(state.Alive())],
                 [cell.Cell(),
                  cell.Cell(),
                  cell.Cell(state.Alive()),
                  cell.Cell()],
                 [cell.Cell(),
                  cell.Cell(state.Alive()),
                  cell.Cell(),
                  cell.Cell()],
                 [cell.Cell(),
                  cell.Cell(),
                  cell.Cell(),
                  cell.Cell()]]
        
        return cells
    
    def test_init(self):
        '''
        Tests initialisation of a GameOfLife object. Also tests that
        the GameOfLife object initialises with the correct rule set.
        '''
        #########################################################
        #     THIS MUST BE REVIEWED BEFORE IMPLEMENTATION       #                 
        #########################################################
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard())
        assert gol
        
        rs = gol._rule_set
        assert isinstance(rs, rule_sets.RuleSetStandard)
    
    def test_set_initial_input(self):
        '''
        Tests that the initial input can be successfully set. Also
        correct object has been set to initial input.
        '''
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard())
        
        # Create a grid and give it a pattern of cells:
        # dada
        # ddad
        # dadd
        # dddd
        gr = grid.Grid(4, 4)
        gr.set_cells(self.set_cells())
        
        # Give the Game of Life this grid as the initial input
        gol.set_initial_input(gr)
        
        # Test the initial input is now not none
        assert gol._initial_input
        
        # Test the initial input has been given the correct pattern
        test_pattern = self.set_cells()
        for x, row in enumerate(gol._initial_input):
            for y, c in enumerate(row):
                assert c.get_state() == test_pattern[x][y].get_state()        
    
    def test_get_initial_input(self):
        '''
        Tests that the initial input can be retrieved from storage
        and that the correct configuration has been retrieved.
        '''
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard())
        
        # Create a grid and give it a pattern of cells:
        # dada
        # ddad
        # dadd
        # dddd
        gr = grid.Grid(4, 4)
        gr.set_cells(self.set_cells())
        
        # Give the Game of Life this grid as the initial input
        gol.set_initial_input(gr)
        
        # Test the initial input can be retrieved
        retrieved_pattern = gol.get_initial_input()
        assert retrieved_pattern
        
        # Test the intial input has been given the correct pattern
        test_pattern = self.set_cells()
        for x, row in enumerate(retrieved_pattern):
            for y, c in enumerate(row):
                assert c.get_state() == test_pattern[x][y].get_state()
                     
        
    
    def test_set_current_generation(self):
        '''
        Tests that the current generation can be stored and tests
        that the correct configuration has been stored.
        '''
        pass
    
    def test_get_current_generation(self):
        '''
        Tests that the current generation can be retrieved from
        storage and that the correct configuration has been
        retrieved.
        '''
        pass
    
    def test_set_next_generation(self):
        '''
        Tests that the next generation can be stored and tests
        that the correct configuration has been stored.
        '''
        pass
    
    def test_get_next_generation(self):
        '''
        Tests that the next generation can be retrieved from
        storage and tests that the correct configuration
        has been retrieved.
        '''
        pass
    
    def test_calculate_next_generation(self):
        '''
        Tests that the next generation of cells has been
        correctly calculated.
        '''
        pass
    
    def test_first_turn(self):
        '''
        Tests that the first turn of the game retrieves
        the correct information from storage and calculates
        the first generation of cells in the correct well.
        '''
        pass
    
    def test_next_turn(self):
        '''
        Tests that the next turn of the game retrieves
        the correct information from storage and calculates
        the next generation of cells in the next way.
        '''
        pass
