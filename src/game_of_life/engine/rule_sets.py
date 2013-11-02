'''
Created on 25 Oct 2013

@author: Michael and Richard

This module contains the rule sets with which the Game of
Life is run.
'''


class RuleSet(object):
    '''
    This class represents the rules by which cells are born
    and continue to live.
    '''

    def __init__(self, born, alive):
        '''
        Ctor - initialises two parameters that state the
        conditions in which a dead cell will be born and an
        alive cell will stay alive
        '''
        self._born = born
        self._alive = alive

    def get_born_var(self):
        '''
        Returns the variable representing how many live
        neighbours a cell must have to be born.
        '''
        return self._born

    def get_stay_var(self):
        '''
        Returns the variable representing how many live
        neighbours a cell must have to remain alive.
        '''
        return self._alive


class RuleSetStandard(RuleSet):
    '''
    The class represents the rules with which Conway
    defined the original Game of Life.
    '''

    def __init__(self):
        '''
        Ctor - initialises the standard rule set for
        Game of Life. This is B3/S23 which means a
        cell is born with exactly three neighbours
        and stays alive with either two or three
        living neighbours.
        '''
        RuleSet.__init__(self, 3, (2, 3))
