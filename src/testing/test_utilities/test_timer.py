'''
Created on 10.11.2013

@author: Michael and Geoff

This module contains the logic for the automated testing of the timer
used by the Game Control system.
'''

import time
from utilities import timer


class TestTimer(object):
    '''
    This class tests the Timer class used by the Game Control system.
    '''

    def test_init(self):
        '''
        Tests the initialisation of the timer.
        '''
        # Test that the timer can be successfully initialised.
        t = timer.Timer(2)
        assert t

        # Test that correct number of seconds has been set.
        assert t._time_remaining == 2

    def test_start(self):
        '''
        Tests whether the timer can be successfully started.
        '''
        current = time.time()
        t = timer.Timer(2)

        t.start()
        while not t._event.is_set():
            pass

        assert (time.time() - current) % 1000 >= 2

    def test_stop(self):
        '''
        Tests whether the timer can be successfully stopped.
        '''
        t = timer.Timer(2)
        t.start()
        t.stop()
        assert t._event.is_set()

    def test_get_time_remaining(self):
        '''
        Tests whether the remaining time on the timer can be
        correctly retrieved.
        '''
        t = timer.Timer(2)
        assert t.get_time_remaining() == 2
