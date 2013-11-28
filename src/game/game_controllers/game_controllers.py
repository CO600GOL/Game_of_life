'''
Created on 28.11.2013

@author: Michael and Geoff

This module contains all the logic for the game controls used
by the system.
'''

from game.game import Game
from utilities.timer import Timer


class GameController(object):
    '''
    This class represents a skeleton from which game controls
    can inherit. It contains all the shared functionality of
    all game controls.
    '''

    def __init__(self, time=300):
        '''
        Ctor - Initialises game controller.
        '''
        self._game = Game()
        self._timer = Timer(time)

    def get_game(self):
        '''
        Returns the game currently being played.
        '''
        return self._game

    def get_time_remaining(self):
        '''
        Returns the timer being used on this game controller.
        '''
        return self._timer.get_time_remaining()

    def play_next_turn(self):
        '''
        Plays a single turn of the game.
        '''
        self._game.next_turn()
