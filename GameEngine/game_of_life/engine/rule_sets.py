"""
This module contains the logic for the rule sets with which the Game of Life is run. A GoL Rule Set contains two values;
the number of living neighbours a cell needs to become born and the number of living neighbours a cell needs to stay
alive.
"""


class RuleSet(object):
    """
    This class represents the rules by which cells are born
    and continue to live.

    This class represents the rules by which Game of Life cells are born and continue to live. It contains the shared
    functionality of all rule sets.
    """

    def __init__(self, born, alive):
        """
        Ctor - initialises the two parameters that define how the Game of Life will run. The first is how many living
        neighbours a cell needs to be born and the second is how many living neighbours a cell needs to stay alive.

        @param born The number of living neighbours a cell needs to been born.
        @param alive The number of living neighbours a cell needs to stay alive.
        """
        self._born = born
        self._alive = alive

    def get_born_var(self):
        """
        @returns The parameter describing how many living neighbours a cell needs in order to be born.
        """
        return self._born

    def get_stay_var(self):
        """
        @returns The parameter describing how many living neighbours a cell needs in order to stay alive.
        """
        return self._alive


class RuleSetStandard(RuleSet):
    """
    This class represents the standard rules with which Conway first defined the original Game of Life.
    """

    def __init__(self):
        """
        Ctor - Initialises the standard rule set for the Game of Life. This is B3/S23, which means a cell is born with
        exactly three living neighbours and stays alive with either two or three living neighbours.
        """
        RuleSet.__init__(self, 3, (2, 3))
