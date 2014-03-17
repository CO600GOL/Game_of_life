"""
This module contains logic that will test the data structure representing a cell state. These tests must evaluate
whether a state can be correctly initialised and can function correctly.
"""

from game.data_structures.states import State


class TestState(object):
    """
    This class tests the functionality of the state data structure.
    """

    def test_init(self):
        """
        This method tests the initialisation of a state. The expected result of this test is for the state to be
        initialised correctly.
        """

        # Assert the state has been correctly initialised.
        assert State()

    def test_eq_(self):
        """
        This method tests the functionality of the state's equality check. The expected result of this test is for two
        states to been seen as equal.
        """
        one = State()
        two = State()
        # Assert that the first state is 'equal to' the second state.
        assert one == two

    def test_ne_(self):
        """
        Tests the overriding of the __ne__ method for the State class.

        This method tests the functionality of the state's negative equality state. The expected result of this test is
        for two states to be seen as equal.
        """
        one = State()
        two = State()
        # Assert that the != check does return true (meaning the two objects are equal). This makes sure the != check
        # is working correctly.
        assert not (one != two)
