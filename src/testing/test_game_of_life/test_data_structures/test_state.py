'''
Created on 20 Oct 2013

@author: Richard & Michael

Test module for test module
'''

from game_of_life.data_structures import state


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

    def test_eq__(self):
        '''
        Tests the overriding of the __eq__ method for the State class.
        '''
        # create two state objects with the state Alive
        # compare them using the boolean comparison ==
        # should assert true
        one = state.Alive()
        two = state.Alive()
        assert one == two

    def test_ne__(self):
        '''
        Tests the overriding of the __ne__ method for the State class.
        '''
        # create two state objects, one with the state Alive and one with the
        # state Dead
        # compare them using the boolean comparison !=
        # should assert true
        a = state.Alive()
        d = state.Dead()
        assert a != d
