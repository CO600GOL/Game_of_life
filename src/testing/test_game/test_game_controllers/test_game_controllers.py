'''
Created on 28.11.2013

@author: Michael and Geoff

This module contains the automated tests for all the system's
game controllers.
'''

from game.game_controllers.game_controllers import GameController
from game.game_controllers.game_controllers import GameOfLifeController
from game.game import Game
from game_of_life.engine.game_of_life import GameOfLife
from game_of_life.data_structures.states import Alive, Dead


def create_initial_input():
    '''
    Abstracted method that creates an array of integer arrays
    to act as the initial input given by the user.
    '''
    # Eventually, output will store the given input as an array
    # of integer arrays. This can be turned into a grid object by the
    # GameOfLifeController.
    init_input = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]

    return init_input


class TestGameController(object):
    '''
    This class tests the logic written in the GameController class.
    '''

    def test_init_(self):
        '''
        Tests initialisation of a GameController.
        '''
        gc = GameController(300)
        assert gc

    def test_set_up_game(self):
        '''
        Tests whether the game to be played can be correctly set up.
        '''
        gc = GameController(300)
        gc.set_up_game()

        assert isinstance(gc._game, Game)

    def test_get_game(self):
        '''
        Tests the game currently being played can be retrieved.
        '''
        gc = GameController(300)
        gc.set_up_game()

        assert isinstance(gc.get_game(), Game)

    def test_get_time_remaining(self):
        '''
        Tests the remaining time on the controller can be retrieved.
        '''
        gc = GameController(300)

        assert gc.get_time_remaining() == 300

    def test_play_next_turn(self):
        '''
        Tests a single turn of the game can be played.
        '''
        gc = GameController(300)
        gc.set_up_game()

        gc.play_next_turn()

        assert gc.get_game().get_turn_count() == 1


class TestGameOfLifeController(object):
    '''
    This class tests the logic written in the GameOfLifeController class.
    '''

    def test_init_(self):
        '''
        Tests initialisation of a GameOfLifeController.
        '''
        golc = GameOfLifeController()

        # Test the logic
        assert golc

    def test_set_up_game(self):
        '''
        Tests that an initial input can be given to the Game of Life.
        '''
        golc = GameOfLifeController()

        # Set up initial input
        init_input = create_initial_input()

        # Set up the Game of Life
        golc.set_up_game(init_input)

        # Test the _game variable is set correctly.
        assert isinstance(golc._game, GameOfLife)

        # Test the input has been set correctly.
        for x, row in enumerate(init_input):
            for y, _col in enumerate(row):
                if init_input[x][y] == 0:
                    assert golc.get_game().get_current_generation()\
                    .get_cells()[x][y].get_state() == Dead()
                else:
                    assert golc.get_game().get_current_generation()\
                    .get_cells()[x][y].get_state() == Alive()

    def test_play_next_turn(self):
        '''
        Tests a single turn of the Game of Life can be played.
        '''
        golc = GameOfLifeController()
        golc.set_up_game(create_initial_input())
        golc.play_next_turn()

        assert golc.get_game().get_turn_count() == 1

        # Write a simulation grid object to test the next generation in our
        # given test.
        next_gen = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # Test that it matches the calculated pattern.
        for x, row in enumerate(next_gen):
            for y, _col in enumerate(row):
                if next_gen[x][y] == 0:
                    assert golc.get_game().get_current_generation()\
                    .get_cells()[x][y].get_state() == Dead()
                else:
                    assert golc.get_game().get_current_generation()\
                    .get_cells()[x][y].get_state() == Alive()

    def test_play_game(self):
        '''
        Tests an entire Game of Life can be played to its end.
        '''
        golc = GameOfLifeController()
        golc.set_up_game(create_initial_input())
        golc.play_game()

        # According to http://www.julianpulgarin.com/canvaslife/, this pattern
        # dies before the time limit of 5 minutes is hit.
        assert golc.get_game().is_game_forsaken()

        # According to http://www.julianpulgarin.com/canvaslife/, the initial
        # pattern should take 53 turns to die.
        assert golc.get_game().get_turn_count() == 53
