'''
Created on 10.11.2013

@author: Michael, Geoff and Richard

This module contains the logic behind the timer to be used by the system.
'''

from threading import Thread, Event


class Timer(Thread):
    '''
    The timer class represents a timer that can be used to help run any game
    played by the system.
    '''

    def __init__(self, no_of_secs):
        '''
        Ctor - Initialises the Timer with a number of seconds for which
        it will run.
        '''
        Thread.__init__(self)
        self._time_remaining = no_of_secs
        self._event = Event()

    def run(self):
        '''
        Starts the timer
        '''
        while self._time_remaining > 0 and not self._event.is_set():
            self._time_remaining -= 1
            self._event.wait(1)
        self.stop()

    def stop(self):
        '''
        Stops the timer
        '''
        self._event.set()

    def get_time_remaining(self):
        '''
        Returns the time remaining on the timer.
        '''
        return self._time_remaining
