'''
Created on 27.11.2013

@author: Michael and Richard

This module contains the logic behind the over-arching Game class.
A Game object can never be instantiated, but is abstracted by
more specific sub-classes.
'''


class Game(object):
    '''
    The Game class acts as a skeleton for all games that can
    be played on the display.
    '''

    def __init__(self):
        '''
        Ctor - Intitialises a game object.
        '''
        self._turn_count = 0

    def next_turn(self):
        '''
        Runs the next turn of the game.
        '''
        self._turn_count += 1

    def get_turn_count(self):
        '''
        Returns the number of turns that have so far passed
        in the game.
        '''
        return self._turn_count
