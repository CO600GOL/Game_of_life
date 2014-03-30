"""
This module contains logic for testing the rule sets used in the Game of Life engine.
"""

from game_of_life.engine import rule_sets


class TestRuleSet(object):
    """
    This class tests the functionality of the RuleSet class.
    """

    def test_init(self):
        """
        This method tests the initialisation of a rule set. The expected result of this test is for the rule set to be
        correctly initialised
        """
        rs = rule_sets.RuleSet(3, (2, 3))
        # Assert the rule set has been initialised.
        assert rs

    def test_get_born_var(self):
        """
        This method tests the ability of the rule set to retrieve the parameter used for the number of living
        neighbours needed for a cell to be born. The expected result of this test is for the parameter to be retrieved
        correctly.
        """
        rs = rule_sets.RuleSet(3, (2, 3))
        b = rs.get_born_var()
        # Assert the parameter has been retrieved.
        assert b
        # Assert the parameter is correct.
        assert b == 3

    def test_get_stay_var(self):
        """
        This method tests the ability of the rule set to retrieve the parameter used for the number of living neighbours
        needed for a cell to stay alive. The expected result of this test is for the parameter to be retrieved correctly.
        """
        rs = rule_sets.RuleSet(3, (2, 3))
        s = rs.get_stay_var()
        # Assert the parameter has been retrieved.
        assert s
        # Assert the parameter is correct.
        assert s == (2, 3)


class TestRuleSetStandard(object):
    """
    This class tests the functionality of the RuleSetStandard class.
    """

    def test_init(self):
        """
        This method tests the initialisation of a standard rule set. The expected result of this test is for the
        parameters for the number of living cells needed for a cell to be born and stay alive to be set correctly.
        """
        srs = rule_sets.RuleSetStandard()
        # Assert the standard rule set has been initialised.
        assert srs

    def test_get_born_var(self):
        """
        This method tests the ability of the standard rule set to retrieve the parameter used for the number of living
        neighbours needed for a cell to be born. The expected result of this test is for the parameter to be retrieved
        as three.
        """
        srs = rule_sets.RuleSetStandard()
        born = srs.get_born_var()
        # Assert that the parameter has been retrieved as three.
        assert born == 3

    def test_get_stay_var(self):
        """
        This method tests the ability of the standard rule set to retrieve the parameter used for the number of living
        neighbours needed for a cell to stay alive. The expected result of this test is for the parameter to be
        retrieved as two and three.
        """
        srs = rule_sets.RuleSetStandard()
        stay = srs.get_stay_var()
        # Assert that the parameters have been retrieved as two or three.
        assert stay == (2, 3)
