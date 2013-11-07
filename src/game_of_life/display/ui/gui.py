'''
Created on 7 Nov 2013

@author: Michael and Richard
'''

from tkinter import Frame


class Gui(Frame):
    '''
    Gui object for the game of life engine.

    Simple functionality:
        - Enter pattern into grid
        - Start simulation button
        - Stop simulation button
        - Next step button
    '''

    def __init__(self):
        '''
        Constructor

        Initialise GameOfLife object
        Build the gui, bind events and initialise the display
        '''
        pass

    def _next_step_button_listener(self, event):
        '''
        Event listener for the next step button

        Event: event object from the tkinter object
        '''
        pass

    def _start_button_listener(self, event):
        '''
        Event listener for the start button

        Event: event object from the tkinter object
        '''
        pass

    def _stop_button_listener(self, event):
        '''
        Event listener for the stop button

        Event: event object from the tkinter object
        '''
        pass
