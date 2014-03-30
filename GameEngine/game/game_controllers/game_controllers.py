"""
This module contains all the logic for a game controller. A game controller is effectively the point of contact for
any other piece of software that makes use of the game controllers. The game can only be accessed through the game
controller, and nothing outside of the controller has any knowledge of its internal functionality.
"""

from game.game import Game

from game_of_life.data_structures.grid import GolGrid
from game_of_life.data_structures.cell import GolCell
from game_of_life.data_structures.states import Alive

from game_of_life.engine.rule_sets import RuleSetStandard
from game_of_life.engine.game_of_life import GameOfLife


class GameController(object):
    """
    This abstract class contains the shared logic for all game controllers. It is not meant to be used in itself, but
    works as a back-bone for all types of game controller.
    """

    def __init__(self):
        """
        Ctor - Initialises game controller.
        """
        pass

    def set_up_game(self):
        """
        This method sets up the game to be played by this controller.
        """
        self._game = Game()

    def get_game(self):
        """
        This method retrieves the game currently being played by the game controller.

        @return The game currently being played.
        """
        return self._game

    def play_next_turn(self):
        """
        This method plays a single turn of the game.
        """
        self._game.next_turn()


class GameOfLifeController(GameController):
    """
    This class represents the controller for the Game of Life. This class will act as a bridge between the GoL game
    engine and any other pieces of software that want to use it, controlling what data the software can access and
    mutate.
    """

    def __init__(self):
        """
        Ctor - Initialises the GoL Controller.
        """
        GameController.__init__(self)

    def set_up_game(self, init_input):
        """
        This method overrides the inherited set_up_game method, setting up the Game of Life with an initial pattern to
        be given to the game engine.

        @param init_input The initial input to give to the GoL game engine.
        """
        GameController.set_up_game(self)

        # Create the initial input
        cell_pattern = []
        init_input = init_input.split("\n")

        for row in range(0, len(init_input)):
            cell_pattern.append([])
            for i in init_input[row]:
                if i == "*":
                    # If the cell is a *, it is meant to be alive, and so set a GoL cell with an alive state.
                    cell_pattern[row].append(GolCell(Alive()))
                else:
                    # Any other character represents death, and so set a GoL cell with a dead state.
                    cell_pattern[row].append(GolCell())

        initial_input = GolGrid()
        initial_input.set_cells(cell_pattern)

        # Create the Rule Set
        rule_set = RuleSetStandard()

        # Set up game
        self._game = GameOfLife(rule_set, initial_input)

    def play_next_turn(self):
        """
        This method plays a single turn of the Game of Life.
        """
        if not self.get_game().is_game_forsaken():
            # If there are still living cells on the grid, the next turn of the GoL is to be played.
            self.get_game().next_turn()

    def get_turn_count(self):
        """
        This method retrieves the number of turns the Game of Life has already been playing for.

        @return The turn count.
        """
        return self._game.get_turn_count()

    def get_current_generation(self, output=False):
        """
        Returns the current generation of the game of life, in the form of a
        Grid object

        This method retrieves the current generation, or the current cell configuration, for the Game of Life.

        @param output Returns true if this method is being called by external software. If output is false, this method
                      returns the configuration as a Grid object. If it is true, the configuration will be returned as
                      a string, because nothing outside of the game engine can know of Grid objects.
        """
        if not output:
            return self._game.get_current_generation()
        else:
            return self._to_string(self._game.get_current_generation())

    def _to_string(self, grid):
        """
        This method translates a Grid object into a string.

        @param grid The Grid object to translate into a string.

        @return string A string representation of the specified Grid object.
        """
        string = ""
        for row in range(0, len(grid.get_cells())):
            for cell in grid.get_cells()[row]:
                if cell.get_state() == Alive():
                    string += '*'
                else:
                    string += '-'

            if row != len(grid.get_cells()) - 1:
                string += '\n'

        return string