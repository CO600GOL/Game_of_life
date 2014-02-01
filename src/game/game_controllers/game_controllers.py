'''
Created on 28.11.2013

@author: Michael and Geoff

This module contains all the logic for the game controls used
by the system.
'''

from game.game import Game

from game_of_life.data_structures.grid import GolGrid
from game_of_life.data_structures.cell import GolCell
from game_of_life.data_structures.states import Alive

from game_of_life.engine.rule_sets import RuleSetStandard
from game_of_life.engine.game_of_life import GameOfLife


class GameController(object):
    '''
    This class represents a skeleton from which game controls
    can inherit. It contains all the shared functionality of
    all game controls.
    '''

    def __init__(self):
        '''
        Ctor - Initialises game controller.
        '''

    def set_up_game(self):
        '''
        Sets up the game to be played by this controller.
        '''
        self._game = Game()

    def get_game(self):
        '''
        Returns the game currently being played.
        '''
        return self._game

    def play_next_turn(self):
        '''
        Plays a single turn of the game.
        '''
        self._game.next_turn()


class GameOfLifeController(GameController):
    '''
    This class represents the controller for the Game of Life.
    This class will act as a bridge between the GoL game engine and
    any output we create, controlling what access the output has
    to the game engine.
    '''

    def __init__(self):
        '''
        Ctor - Initialises the GoL Controller.
        '''
        GameController.__init__(self)

    def set_up_game(self, init_input):
        '''
        Sets the initial input of the Game Of Life.
        '''
        GameController.set_up_game(self)

        # Create the initial input
        cell_pattern = []
        init_input = init_input.split("\n")

        for row in range(0, len(init_input)):
            cell_pattern.append([])
            for i in init_input[row]:
                if i == "*":
                    cell_pattern[row].append(GolCell(Alive()))
                else:
                    cell_pattern[row].append(GolCell())

        initial_input = GolGrid()
        initial_input.set_cells(cell_pattern)

        # Create the Rule Set
        rule_set = RuleSetStandard()

        # Set up game
        self._game = GameOfLife(rule_set, initial_input)

    def play_next_turn(self):
        '''
        Plays a single turn of the Game of Life.
        '''
        if not self.get_game().is_game_forsaken():
            self.get_game().next_turn()

    def get_turn_count(self):
        '''
        Returns the current turn count of the game of life
        '''
        return self._game.get_turn_count()

    def get_current_generation(self):
        '''
        Returns the current generation of the game of life, in the form of a
        Grid object
        '''
        return self._game.get_current_generation()
