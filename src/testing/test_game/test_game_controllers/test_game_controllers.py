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

    def test_get_game(self):
        '''
        Tests the game currently being played can be retrieved.
        '''
        gc = GameController()

        assert isinstance(gc.get_game(), Game)

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
        gc = GameController()
        gc.play_next_turn()

        assert gc.get_game().get_turn_count() == 1
