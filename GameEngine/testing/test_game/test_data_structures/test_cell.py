"""
This module contains logic that will test the data structure representing a game board cell. These tests must evaluate
whether a cell can be correctly initialised and can correctly function.
"""

from game.data_structures.cell import Cell
from game.data_structures.states import State


def initialise_cell():
    """
    Abstracted initialisation as it was being repeated

    This function abstracts the initialisation of a Cell object, in order to avoid repeating unnecessary code.
    """
    return Cell()


class TestCell(object):
    """
    This class tests the functionality of the Cell data structure.
    """

    def test_cell_init(self):
        """
        This method tests whether a Cell object is being correctly initialised. The expected result of this test is for
        the Cell to be correctly initialised.
        """
        # Assert that a cell is initialised correctly.
        assert initialise_cell()

    def test_get_state(self):
        """
        This method tests the ability of the Cell to retrieve its current state. The expected result of this test is for
        the correct current state to be retrieved.
        """
        c = initialise_cell()
        s = c.get_state()
        # Assert a state has been retrieved.
        assert s
        # Make sure the retrieved state was of the correct type.
        assert isinstance(s, State)

    def test_set_state(self):
        """
        This method tests the ability of the Cell to change its current state. The expected result of this test is for
        the correct state to be set to the Cell.
        """
        c = initialise_cell()
        c.set_state(State())
        s = c.get_state()
        # Ensure that a state was set.
        assert s
        # Ensure that state was set to the correct type.
        assert isinstance(s, State)
