"""
This module contains logic that tests the data structure representing a Game of Life board cell. These tests must
evaluate whether a cell can be correctly initialised and can function correctly.
"""

from game_of_life.data_structures.cell import GolCell
from game_of_life.data_structures.states import Alive, Dead


def initialise_cell():
    """
    This function abstracts the initialisation of a GoLCell, to stop unnecessary repeated code.
    """
    return GolCell()


class TestCell(object):
    """
    This class tests the functionality of the GoLCell class.
    """

    def test_cell_init(self):
        """
        This method tests the initialisation of a GoLCell. The expected result of this test is for the cell to be
        correctly initialised.
        """
        # Assert that the cell has been initialised.
        assert initialise_cell()

    def test_get_state(self):
        """
        This method tests the ability of the GoLCell to retrieve its current state. The expected result of this test
        is for the cell's current state to be correctly retrieved.
        """
        c = initialise_cell()
        s = c.get_state()
        # Assert that the cell's state has been retrieved.
        assert s
        # Assert that the cell's state is correct (at this point it will be Dead).
        assert isinstance(s, Dead)

    def test_is_alive(self):
        """
        This method tests the ability of the GolCell to evaluate whether or not it is alive. The expected result of this
        test is for the evaluation to be successful.
        """
        c = GolCell(Alive())
        # Assert that the GolCell can evaluate itself as alive.
        assert c.is_alive()

        c = initialise_cell()
        # Assert that the GolCell can evaulate itself as dead.
        assert not c.is_alive()

    def test_set_state(self):
        """
        This method tests the ability of the GolCell to set its new state. The expected result of this test is for a
        new state to be correctly set.
        """
        c = initialise_cell()
        c.set_state(Alive())
        s = c.get_state()
        # Assert that the state has been set.
        assert s
        # Assert that the state has been set to Alive.
        assert isinstance(s, Alive)
