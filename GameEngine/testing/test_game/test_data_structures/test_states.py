'''
Created on 20 Oct 2013

@author: Richard & Michael

Test module for test module
'''

from game.data_structures.states import State


class TestState(object):
    '''
    Tests the state module
    '''

    def test_init(self):
        '''
        Tests the initialisation of a state.
        '''
        assert State()

    def test_eq_(self):
        '''
        Tests the overriding of the __eq__ method for the State class.
        '''
        # create two state objects
        # compare them using the boolean comparison ==
        # should assert true
        one = State()
        two = State()
        assert one == two

    def test_ne_(self):
        '''
        Tests the overriding of the __ne__ method for the State class.
        '''
        # create two state objects
        # compare them using the boolean comparison !=
        # should assert true
        one = State()
        two = State()
        assert not (one != two)
