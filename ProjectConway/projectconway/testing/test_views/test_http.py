import json
import time
import urllib.request as urllib
from subprocess import Popen
'''
This module will test HTTP access to the web application.
'''
URL = "http://127.0.0.1:6543/"


def setup_module(module):
    '''
    Sets up everything required for each test class to function.
    '''
    module.p = Popen(["/bin/bash", "-c", "make run"])
    time.sleep(1)  # Allow server to start


def teardown_module(module):
    '''
    Sets up everything required to shut down each class after testing has been
    completed.
    '''
    module.p.send_signal(15)  # Same as sending SIGTERM
    # Using SIGTERM instead of kill() as it does not close all pyramid threads
    assert module.p.wait()


class TestPatternInputPage(object):
    '''
    This class runs automated HTTP tests on the Pattern Input Page - this
    includes all views used on the page. 
    '''

    def test_pattern_input_receiver_JSON(self):
        '''
        This method tests HTTP functionality on the pattern input JSON receiver
        view.
        '''
        url = "%spattern_receiver.json" % URL
        data = json.dumps("""-*-*-*-*-*
*-*-*-*-*-
-*--------
--*-------
---*------
----*-----
-----*----
*-*-*-*-*-
-*-*-*-*-*
*-*-*-*-*-""").encode('utf-8')
        headers = {"Content-Type": "application/json"}

        request = urllib.Request(url, data, headers)
        response = urllib.urlopen(request)
        content = response.read().decode("utf-8")

        # Ensure we have a response
        assert content
        print("Type", type(content))

        # Assert the values are correct
        res_data = json.loads(content)
        assert res_data["turns"] == 53
        assert res_data["runtime"] == 26.5
