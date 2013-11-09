'''
Created on 7 Nov 2013

@author: Niklas and Richard
'''

from game_of_life.display.ui import gui
from game_of_life.data_structures import state


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
        g = gui.Gui()
        grid = g.grid()
        cells = grid.get_cells()

        for row in cells:
            for c in row:
                c.generate_event('<Button-1>')
                assert c.get_state() == state.Alive()

    def test_next_step_button_listener(self):
        '''
        Testing functionality of the next step button listener.

        This test first says that all cells are alive then emulates
        a click on the next button and ensures that each cell is dead.
        '''
        g = gui.Gui()
        grid = g.grid()
        cells = grid.get_cells()

        for row in cells:
            for c in row:
                c.generate_event('<Button-1>')

        self.next_button.generate_event('<Button-1>')

        for row in cells:
            for c in row:
                assert c.get_state() == state.Dead()

    def test_start_stop_button_listener(self):
        '''
        Testing functionality of the start step button listener
        '''
        pass
