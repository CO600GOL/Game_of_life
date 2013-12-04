'''
Created on 27.11.2013

@author: Michael and Richard

This module contains the logic for testing the game
module.
'''

from game.game import Game


class TestGame(object):
    '''
    This class acts to represent automated tests for the
    Game class.
    '''

    def test_init(self):
        '''
        Tests the initialisation of a Game object.
        '''
        g = Game()

        # Assert logic works
        assert g

        # Assert logic works as expected
        assert g._turn_count == 0

    def test_next_turn(self):
        '''
        Tests whether the Game.next_turn() method functions correctly.
        '''
        g = Game()

        g.next_turn()
        assert g._turn_count == 1

    def test_get_turn_count(self):
        '''
        Tests whether the get_turn_count() method functions correctly.
        '''
        g = Game()
        g.next_turn()

        assert g.get_turn_count() == 1
