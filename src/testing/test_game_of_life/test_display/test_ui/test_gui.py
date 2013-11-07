'''
Created on 7 Nov 2013

@author: richard
'''

from game_of_life.display.ui import gui


class TestGui(object):
    '''
    classdocs
    '''

    def test_init(self):
        '''
        Test that the GUI can be corrected initialised.
        '''
        display = gui.Gui()
        assert display

    def test_next_step_button_listener(self):
        '''
        Testing functionality of the next step button listener
        '''
        pass

    def test_start_button_listener(self):
        '''
        Testing functionality of the start step button listener
        '''
        pass

    def test_stop_button_listener(self):
        '''
        Testing functionality of the stop button listener
        '''
        pass
