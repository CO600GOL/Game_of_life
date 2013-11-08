'''
Created on 7 Nov 2013

@author: Niklas and Richard
'''

from game_of_life.display.ui import widgets
from game_of_life.data_structures import state


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
        cw.set_state(state.Alive())
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
