'''
Created on 28.11.2013

@author: Michael and Geoff

This module contains all the logic for the game controls used
by the system.
'''


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
        pass

    def set_game(self, game):
        '''
        Sets a game to be played to the game controller.
        '''
        pass

    def get_game(self):
        '''
        Returns the game currently being played.
        '''
        pass

    def get_time_remaining(self):
        '''
        Returns the timer being used on this game controller.
        '''

    def play_next_turn(self):
        '''
        Plays a single turn of the game.
        '''
        pass

    def play_game(self):
        '''
        Plays the game until its end.
        '''
        pass
