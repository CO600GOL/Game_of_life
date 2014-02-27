'''
Created on 20 Oct 2013

@author: Michael and Richard
'''

from game.data_structures.cell import Cell
from game.data_structures.states import State


def initialise_cell():
    '''
    Abstracted initialisation as it was being repeated
    '''
    return Cell()


class TestCell(object):
    '''
    Tests the functionality of the cell module
    '''

    def test_cell_init(self):
        '''
        Test initialisation of Cell object
        '''
        assert initialise_cell()

    def test_get_state(self):
        '''
        Test correct functionality of Cell's accessor method
        '''
        c = initialise_cell()
        s = c.get_state()
        # Make sure it returned a state
        assert s
        # Make sure the state was State
        assert isinstance(s, State)

    def test_set_state(self):
        '''
        Test correct functionality of Cell's mutator method
        '''
        c = initialise_cell()
        c.set_state(State())
        s = c.get_state()
        # Ensure that a state was set correct
        assert s
        # Ensure that state was set as State
        assert isinstance(s, State)
