'''
Created on 28.11.2013

@author: Michael and Geoff

This module contains the automated tests for all the system's
game controllers.
'''

from game.game_controllers.game_controllers import GameController
from game.game import Game


class TestGameController(object):
    '''
    This class tests the logic written in the GameController class.
    '''

    def test_init_(self):
        '''
        Tests initialisation of a GameController.
        '''
        gc = GameController()
        assert gc

    def test_set_game(self):
        '''
        Tests a game object can be set to the game controller.
        '''
        gc = GameController()
        g = Game()

        # test logic works
        gc.set_game(g)
        assert gc._game

        # Test logic works as expected
        assert gc._game == g

    def test_get_game(self):
        '''
        Tests the game currently being played can be retrieved.
        '''
        gc = GameController()
        g = Game()
        gc.set_game(g)

        returned_game = gc.get_game()
        assert returned_game == g

    def test_get_time_remaining(self):
        '''
        Tests the remaining time on the controller can be retrieved.
        '''
        gc = GameController(500)
        assert gc.get_time_remaining() == 500

    def test_play_next_turn(self):
        '''
        Tests a single turn of the game can be played.
        '''
        pass

    def test_play_game(self):
        '''
        Tests the game can be played through to the end.
        '''
        pass
