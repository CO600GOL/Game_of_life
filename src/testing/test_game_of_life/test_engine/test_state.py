'''
Created on 20 Oct 2013

@author: Richard & Michael

Test module for test module
'''

from game_of_life.engine import state


class TestState(object):
    '''
    Tests the state module
    '''

    def test_alive_init(self):
        '''
        Tests the initialisation of Alive state
        '''
        a = state.Alive()
        # Makes sure the state is initialised
        assert a
        # Makes sure a is a subclass of State
        assert isinstance(a, state.State)

    def test_dead_init(self):
        '''
        Tests the initialisation of Dead state
        '''
        d = state.Dead()
        # Makes sure the state is initialised
        assert d
        # Makes sure d is a subclass of State
        assert isinstance(d, state.State)
