'''
Created on 20 Oct 2013

@author: Richard and Michael

Simple python module to show the simplest use of the pytest module
Under usual circustance the logic being testing should be imported in this
module, built in an appropriate way and tested as such.
'''


def increment(x):
    return x + 1


def test_increment():
    assert increment(1) == 2
