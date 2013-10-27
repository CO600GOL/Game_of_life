'''
Created on 27.10.2013

@author: Michael and Geoff

This module contains the test framework for the
timer module.
'''

from game_of_life.engine import timer


class TestTimer(object):
    '''
    This class contains the test framework for
    the timer class.
    '''
 
    def test_init(self):
        '''
        Test the initialisation of timer objects.
        '''
        t = timer.Timer()
        assert t
    
    def test_start_timer(self):
        '''
        Test that the timer starts correctly.
        '''
        t = timer.Timer()
        t.start_timer()
        
        remaining_seconds = t.get_remaining_time()
        assert remaining_seconds < 300
    
    def test_stop_timer(self):
        '''
        Test that the timer stops correctly.
        '''
        t = timer.Timer()
        t.start_timer()
        
        assert t.stop_timer()
    
    def test_get_remaining_time(self):
        '''
        Test that the timer returns the 
        remaining time. Also tests that a
        timer is initialised at three
        hundred seconds.
        '''
        t = timer.Timer()
        secs = t.get_remaining_time()
        
        # Asserts that a valid time has been returned.
        assert isinstance(secs, int)
        
        # Asserts the correct amount of time is remaining
        assert t.get_remaining_time() == 300
    