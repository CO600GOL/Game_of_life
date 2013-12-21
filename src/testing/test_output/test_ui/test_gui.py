'''
Created on 7 Nov 2013

@author: Niklas and Richard
'''

from output.ui import gui
from game_of_life.data_structures.states import Alive, Dead


class TestGui(object):
    '''
    Tests the Gui object.
    '''

    def test_init(self):
        '''
        Test that the GUI can be correctly initialised.
        '''
        display = gui.Gui()
        assert display

    def test_cell_listener(self):
        '''
        Testing functionality of the cell listener.

        This test emulates a click on all of the cells (which should be dead at
        this point) and ensures that have changed to alive.
        '''
#        g = gui.Gui()
#        grid = g._grid
#        cells = grid.get_cells()
#
#        g.wait_visibility()
#
#        for row in cells:
#            for c in row:
#                c.event_generate('<Button-1>')
#                assert c.get_state() == Alive()
        pass 
        #@todo: Replace this with better testing, probably using
        #something like Mock

    def test_next_step_button_listener(self):
        '''
        Testing functionality of the next step button listener.

        This test first says that all cells are alive then emulates
        a click on the next button and ensures that each cell is dead.
        '''
#        g = gui.Gui()
#        grid = g._grid
#        cells = grid.get_cells()
#
#        g.wait_visibility()
#
#        for row in cells:
#            for c in row:
#                c.event_generate('<Button-1>')
#                assert c.get_state() == state.Alive()
#
#        g._next_button.event_generate('<Button-1>')
#
#        for row in cells:
#            for c in row:
#                assert c.get_state() == Dead()
        pass 
        #@todo: Replace this with better testing, probably using
        #something like Mock

    def test_start_stop_button_listener(self):
        '''
        Testing functionality of the start step button listener
        '''
        pass
