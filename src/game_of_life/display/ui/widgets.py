'''
Created on 7 Nov 2013

@author: Niklas and Richard
'''

from tkinter import Frame, Canvas, Button
from game_of_life.data_structures.cell import Cell
from game_of_life.data_structures.grid import Grid
from game_of_life.data_structures import state

X_MAX = 10
Y_MAX = 10
CELL_SIZE = 15
ALIVE_COLOUR = "black"
DEAD_COLOUR = "white"


class GridWidget(Frame, Grid):
    '''
    Grid widget, contains a collection of cell widgets which reflect the state
    of the game of life cell and the cells it contains.
    '''

    def __init__(self, root=None):
        '''
        Constructor

        root - reference to the wdiget containing this widget
        '''
        Frame.__init__(self, root)

        cells = []
        for x in range(0, X_MAX):
            cols = []
            for y in range(0, Y_MAX):
                cell = CellWidget(master=self, width=CELL_SIZE, height=CELL_SIZE)
                cell.grid(row=x, column=y)
                cols.append(cell)
            cells.append(cols)

        Grid.__init__(self, cells)

    def repaint(self):
        '''
        Calls repaint method of its CellWidgets
        '''
        cells = self.get_cells()
        for row in cells:
            for c in row:
                c.repaint()


class CellWidget(Canvas, Cell):
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
        Cell.__init__(self)

    def repaint(self):
        '''
        Checks game of life cell and changes the colour dependent
        on the game of life state
        '''
        if self.get_state() == state.Alive():
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
