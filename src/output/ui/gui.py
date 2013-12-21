'''
Created on 7 Nov 2013

@author: Michael and Richard
@author: Niklas and Richard
'''

from tkinter import Frame, Tk
from game_of_life.data_structures.states import Alive, Dead
from game_of_life.engine.game_of_life import GameOfLife
from game_of_life.engine.rule_sets import RuleSetStandard
from output.ui.widgets import GridWidget, NextButton

X_SIZE = 10
Y_SIZE = 10


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
        # Encasing frame
        tk = Tk()
        Frame.__init__(self, master=tk)

        # Grid frame
        self._grid = GridWidget(self, X_SIZE, Y_SIZE)
        for row in self._grid.get_cells():
            for cell in row:
                cell.bind('<Button-1>', self._cell_listener)

        # buttons
        self._next_button = NextButton(master=self)
        self._next_button.bind('<Button-1>', self._next_step_button_listener)

        # Set layout
        self._grid.grid(row=0, column=0)
        self._next_button.grid(row=0, column=1)

        # Game of life
        self._gol = GameOfLife(RuleSetStandard(), self._grid)

        self.pack()
        self._grid.pack()
        self._next_button.pack()

    def _cell_listener(self, event):
        '''
        Event listener for the cells

        Event: an object created when the cell is clicked
        '''
        cell = event.widget
        a = Alive()
        if cell.get_state() == a:
            cell.set_state(Dead())
        else:
            cell.set_state(a)

        cell.repaint()

    def _next_step_button_listener(self, event):
        '''
        Event listener for the next step button

        Event: event object from the tkinter object
        '''
        self._gol.next_turn()
        self._grid.repaint()

    def _start_stop_button_listener(self, event):
        '''
        Event listener for the start button

        Event: event object from the tkinter object
        '''
        pass
