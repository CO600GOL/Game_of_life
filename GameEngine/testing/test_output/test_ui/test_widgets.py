'''
Created on 7 Nov 2013

@author: Niklas and Richard
'''

from output.ui import widgets
from game_of_life.data_structures.states import Alive


class TestGrid(object):
    '''
    Testing the GridWidget
    '''

    def test_init(self):
        '''
        Testing initialisation of GridWidget
        '''
        assert widgets.GridWidget()

    def test_repaint(self):
        '''
        Testing complete functionality of the repaint method
        '''
        gw = widgets.GridWidget()

        cell_colours = []
        for row in gw.get_cells():
            row_colour = []
            for c in row:
                row_colour.append(c['bg'])
                c.set_state(Alive())
            cell_colours.append(row_colour)

        gw.repaint()

        for x, row in enumerate(gw.get_cells()):
            for y, c in enumerate(row):
                assert c['bg'] != cell_colours[x][y]


class TestCell(object):
    '''
    Testing the CellWidget
    '''

    def test_init(self):
        '''
        Testing initialisation of CellWidget
        '''
        assert widgets.CellWidget()

    def test_repaint(self):
        '''
        Testing complete functionality of the repaint method
        '''
        cw = widgets.CellWidget()
        initial_colour = cw['bg']
        cw.set_state(Alive())
        cw.repaint()

        assert initial_colour != cw['bg']


class TestStartStopButton(object):
    '''
    Testing the start/stop button.
    This button should cause the game of life to toggle running.
    '''

    def test_init(self):
        '''
        Test correct initialisation of the button and it's super classes.
        '''
        assert widgets.StartStopButton()


class TestNextButton(object):
    '''
    Testing the Nextbutton
    This button should cause the game of life to evolve one step.
    '''

    def test_init(self):
        '''
        Test correct initialisation of the button and it's super classes.
        '''
        assert widgets.NextButton()
