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
        pass

    def get_born_var(self):
        '''
        Returns the variable representing how many live
        neighbours a cell must have to be born.
        '''
        pass

    def get_stay_var(self):
        '''
        Returns the variable representing how many live
        neighbours a cell must have to remain alive.
        '''
        pass
