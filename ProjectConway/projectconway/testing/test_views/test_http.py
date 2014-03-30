"""
This module contains logic that tests the HTTP connection of all of the python templates that make up our web
application.
"""

import os
import json
import urllib.request as urllib
import pexpect
URL = "http://127.0.0.1:6543/"


def setup_module(module):
    """
    This function sets up the testing class, initialising shared data that will be needed during testing.
    """
    module.p = pexpect.spawn("/bin/bash", ["-c", "make run"])

    # Wait for the pyramid process to start serving requests
    # There is a time limit of 10 seconds
    module.p.expect("serving on", timeout=10)

def teardown_module(module):
    """
    This function tears down the testing class once testing has been completed. This ensures that the no data
    is maintained after testing that shouldn't be.
    """
    module.p.kill(15)  # Same as sending SIGTERM
    # Using SIGTERM instead of kill(), as kill() does not close all pyramid threads
    module.p.wait()

    '''
    Sets up everything required to shut down each class after testing has been
    completed.
    '''
    os.system("killall pserve")

class TestHomePage(object):
    """
    This class tests the functionality of the home page of our web application.
    """

    def test_home_page(self):
        """
        This method tests that the home page is recognisable over HTTP, and that a response can be retrieved. The
        expected result of this test is for a response to be successfully retrieved.
        """
        url = URL

        request = urllib.Request(url)
        response = urllib.urlopen(request)
        content = response.read().decode("utf-8")

        # Assert that a response has been received.
        assert content


class TestAboutPage(object):
    """
    This class tests the functionality of the about page of our web application.
    """

    def test_about_page(self):
        """
        This method tests that the about page is recognisable over HTTP, and that a response can be retrieved. The
        expected result of this test is for a response to be successfully retrieved.
        """
        url = "%sabout" % URL

        request = urllib.Request(url)
        response = urllib.urlopen(request)
        content = response.read().decode("utf-8")

        # Assert that a response has been retrieved.
        assert content


class TestCreatePage(object):
    """
     This class tests the functionality of the create page of our web application.
    """

    def test_create_page(self):
        """
        This method tests that the create page is recognisable over HTTP, and that a response can be retrieved. The
        expected result of this test is for a response to be successfully retrieved.
        """
        url = "%screate" % URL

        request = urllib.Request(url)
        response = urllib.urlopen(request)
        content = response.read().decode("utf-8")

        # Assert that a response has been retrieved.
        assert content

    def test_pattern_input_receiver_JSON(self):
        """
        This method tests HTTP functionality of the pattern input JSON receiver view on the create page. The expected
        result of this test is for the HTTP response to be retrieved successfully.
        """
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

        # Assert that a response has been received.
        assert content

        # Assert that the response data is correct for the data input to the view.
        res_data = json.loads(content)
        assert res_data["turns"] == 53
        assert res_data["runtime"] == 26.5

    def test_confirmation_receiver_JSON(self):
        """
        This method tests HTTP functionality of the confirmation receiver JSON view on the create page. The expected
        result of this test is for the HTTP response to be retrieved successfully.
        """
        url = "%sconfirm.json" % URL
        headers = {"Content-Type": "application/json"}

        request = urllib.Request(url, headers=headers)
        try:
            response = urllib.urlopen(request)
        except:
            return
        else:
            raise Exception("Url did not return an exception due to lack of cookies")
        content = response.read().decode("utf-8")

        # Assert that a response has been received.
        assert content
