import json
import urllib.request as urllib
import pexpect
'''
This module will test HTTP access to the web application.
'''
URL = "http://127.0.0.1:6543/"


def setup_module(module):
    '''
    Sets up everything required for each test class to function.
    '''
    module.p = pexpect.spawn("/bin/bash", ["-c", "make run"])

    # Wait for the pyramid process to start serving requests
    # There is a time limit of 10 seconds
    module.p.expect("serving on", timeout=10)

def teardown_module(module):
    '''
    Sets up everything required to shut down each class after testing has been
    completed.
    '''
    module.p.kill(15)  # Same as sending SIGTERM
    # Using SIGTERM instead of kill() as it does not close all pyramid threads
    module.p.wait()


class TestHomePage(object):
    '''
    This class runs automated HTTP tests on the Homepage - this
    includes all views used on the page.
    '''

    def test_home_page(self):
        '''
        This method ensures that
        '''
        url = URL

        request = urllib.Request(url)
        response = urllib.urlopen(request)
        content = response.read().decode("utf-8")

        # Ensure we have a response
        assert content


class TestAboutPage(object):
    '''
    This class runs automated HTTP tests on the About page - this
    includes all views used on the page.
    '''

    def test_about_page(self):
        '''
        This method ensures that
        '''
        url = "%sabout" % URL

        request = urllib.Request(url)
        response = urllib.urlopen(request)
        content = response.read().decode("utf-8")

        # Ensure we have a response
        assert content


class TestCreatePage(object):
    '''
    This class runs automated HTTP tests on the Pattern Input Page - this
    includes all views used on the page. 
    '''

    def test_create_page(self):
        '''
        This method ensures that the create route is working
        '''
        url = "%screate" % URL

        request = urllib.Request(url)
        response = urllib.urlopen(request)
        content = response.read().decode("utf-8")

        # Ensure we have a response
        assert content

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

    def test_confirmation_receiver_JSON(self):
        """
        This method tests HTTP functionality on the confirmation
        receiver JSON view.
        """
        url = "%sconfirm.json" % URL
        headers = {"Content-Type": "application/json"}

        request = urllib.Request(url, headers=headers)
        # TODO: Make this test support cookies so that the try/catch can be removed
        try:
            response = urllib.urlopen(request)
        except:
            return
        else:
            raise Exception("Url did not return an exception due to lack of cookies")
        content = response.read().decode("utf-8")

        # Ensure we have a response
        assert content


class TestRulesPage(object):
    '''
    This class runs automated HTTP tests on the Rules page - this
    includes all views on this page
    '''
    
    def test_rules_page(self):
        '''
        This method ensures that
        '''
        url = "%srules" % URL
        request = urllib.Request(url)
        response = urllib.urlopen(request)
        content = response.read().decode("utf-8")
        
        #Ensure we have a response
        assert content
