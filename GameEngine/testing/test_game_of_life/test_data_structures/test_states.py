"""
This module contains logic to test the data structure representing the Game of Life cell states. These tests must
evaluate that the states can be correctly initialised and that they can function correctly.
"""

from game_of_life.data_structures.states import Alive, Dead


class TestAlive(object):
    """
    This class tests the functionality of the Alive class.
    """

    def test_init(self):
        """
        This method tests the initialisation of an Alive state. The expected result of this test is for the state
        to be correctly initialised.
        """
        # Assert the alive state has been initialised.
        assert Alive()

    def test_eq_(self):
        """
        This method tests the functionality of the alive state's equality check. The expected result of this test is for
        two alive states to be seen as equal.
        """
        one = Alive()
        two = Alive()
        # Assert that the two states are seen as equal.
        assert one == two

    def test_ne_(self):
        """
        This method tests the functionality of the alive state's negative equality check. The expected result of this
        test is for two alive states to be not seen as unequal.
        """
        one = Alive()
        two = Alive()
        # Assert that != check returns true, which means the two states are equal. This also asserts that the two
        # objects are not unequal.
        assert not (one != two)


class TestDead(object):
    """
    This class tests the functionality of the Dead class.
    """

    def test_init(self):
        """
        This method tests the initialisation of a Dead state. The expected result of this test is that the state can be
        correctly initialised.
        """
        # Assert the Dead state has been correctly initialised.
        assert Dead()

    def test_eq_(self):
        """
        This method tests the functionality of the dead state's equality check. The expected result of this test is that
        two Dead states are seen as equal.
        """
        one = Dead()
        two = Dead()
        # Assert that two Dead states are seen as equal.
        assert one == two

    def test_ne_(self):
        """
        This method tests the functionality of the dead state's negative equality check. The expected result of this
        test is for two dead states to be not seen as unequal.
        """
        one = Dead()
        two = Dead()
        # Assert that != check returns true, which means the two states are equal. This also asserts that the two
        # objects are not unequal.
        assert not (one != two)