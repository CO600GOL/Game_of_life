'''
Created on 20 Oct 2013

@author: Richard & Michael

Test module for test module
'''

from game_of_life.data_structures.states import Alive, Dead


class TestAlive(object):
    '''
    Tests the alive state module.
    '''

    def test_init(self):
        '''
        Tests the initialisation of an Alive state
        '''
        assert Alive()

    def test_eq_(self):
        '''
        Tests that two Alive states are equal
        '''
        one = Alive()
        two = Alive()
        assert one == two

    def test_ne_(self):
        '''
        Tests that two Alive states are not equal
        '''
        one = Alive()
        two = Alive()
        assert not (one != two)


class TestDead(object):
    '''
    Tests the dead state module.
    '''

    def test_init(self):
        '''
        Tests the initialisation of a Dead state.
        '''
        assert Dead()

    def test_eq_(self):
        '''
        Tests that two Dead states are equal.
        '''
        one = Dead()
        two = Dead()
        assert one == two

    def test_ne_(self):
        '''
        Tests that two Dead states are not equal.
        '''
        one = Dead()
        two = Dead()
        assert not (one != two)