'''
Created on 7 Nov 2013

@author: Niklas and Richard
'''

from tkinter import Frame, Canvas, Button
from game_of_life.data_structures.cell import GolCell
from game_of_life.data_structures.grid import GolGrid
from game_of_life.data_structures.states import Alive

C_SIZE = 15
ALIVE_COLOUR = "black"
DEAD_COLOUR = "white"


class GridWidget(Frame, GolGrid):
    '''
    Grid widget, contains a collection of cell widgets which reflect the state
    of the game of life cell and the cells it contains.
    '''

    def __init__(self, root=None, X_MAX=10, Y_MAX=10):
        '''
        Constructor

        root - reference to the wdiget containing this widget
        '''
        Frame.__init__(self, root)

        cells = []
        for x in range(0, X_MAX):
            cols = []
            for y in range(0, Y_MAX):
                cell = CellWidget(master=self, width=C_SIZE, height=C_SIZE)
                cell.grid(row=x, column=y)
                cols.append(cell)
            cells.append(cols)

        GolGrid.__init__(self, cells)

    def repaint(self):
        '''
        Calls repaint method of its CellWidgets
        '''
        cells = self.get_cells()
        for row in cells:
            for c in row:
                c.repaint()


class CellWidget(Canvas, GolCell):
    '''
    Cell widget, a version of the game of life cell, that is capable of being
    displayed in a gui.
    '''

    def __init__(self, **kwargs):
        '''
        Constructor

        root - reference to the widget containing this widget
        '''
        Canvas.__init__(self, **kwargs)
        self['bg'] = DEAD_COLOUR
        GolCell.__init__(self)

    def repaint(self):
        '''
        Checks game of life cell and changes the colour dependent
        on the game of life state
        '''
        if self.get_state() == Alive():
            self["bg"] = ALIVE_COLOUR
        else:
            self["bg"] = DEAD_COLOUR


class StartStopButton(Button):
    '''
    Start/Stop button, a button that will toggle whether the game of life is
    running.

    root - reference to the wdiget containing this widget
    '''

    def __init__(self, **kwargs):
        '''
        Constructor

        root - reference to the wdiget containing this widget
        '''
        Button.__init__(self, **kwargs)
        self["text"] = "Start/Stop"


class NextButton(Button):
    '''
    Next button, a button that will cause the game of life to evolve one step.
    '''

    def __init__(self, **kwargs):
        '''
        Constructor

        root - reference to the wdiget containing this widget
        '''
        Button.__init__(self, **kwargs)
        self["text"] = "Next"
