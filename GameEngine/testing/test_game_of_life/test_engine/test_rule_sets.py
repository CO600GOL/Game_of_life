'''
Created on 25 Oct 2013

@author: Michael, Richard and Geoff

This module contains the tests for the rulesets module
'''

from game_of_life.engine import rule_sets


class TestRuleSet(object):
    '''
    This class contains and runs all the tests for the top
    rule set class
    '''

    def test_init(self):
        '''
        Tests the initialisation of a rule set for use by the
        game of life.
        '''
        rs = rule_sets.RuleSet(3, (2, 3))
        assert rs

    def test_get_born_var(self):
        '''
        Tests that a rule set can find this specific rule.
        '''
        rs = rule_sets.RuleSet(3, (2, 3))
        b = rs.get_born_var()
        assert b
        assert b == 3

    def test_get_stay_var(self):
        '''
        Tests that a rule set can find this specific rule.
        '''
        rs = rule_sets.RuleSet(3, (2, 3))
        s = rs.get_stay_var()
        assert s
        assert s == (2, 3)


class TestRuleSetStandard(object):
    '''
    This class contains and runs all the tests for the
    standard Game of Life rule set.
    '''

    def test_init(self):
        '''
        Test initialisation of standard rule set.
        Test that the correct values have been given
        to the standard rule set.
        '''
        srs = rule_sets.RuleSetStandard()
        assert srs

    def test_get_born_var(self):
        '''
        Test that the born variable is equal to three.
        '''
        srs = rule_sets.RuleSetStandard()
        born = srs.get_born_var()
        assert born == 3

    def test_get_stay_var(self):
        '''
        Test that the stay variable is equal to (2, 3)
        '''
        srs = rule_sets.RuleSetStandard()
        stay = srs.get_stay_var()
        assert stay == (2, 3)
