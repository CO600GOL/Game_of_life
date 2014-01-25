import json
from pyramid.testing import DummyRequest
from game_of_life import TIME_DELAY
from projectconway.views.pattern_input import pattern_input_view
from projectconway.views.pattern_input import pattern_input_receiver_JSON


def create_input_pattern():
    '''
    Create an initial input to represent the data being saved
    to the database.
    '''
    return """\
-*-*-*-*-*
*-*-*-*-*-
-*--------
--*-------
---*------
----*-----
-----*----
*-*-*-*-*-
-*-*-*-*-*
*-*-*-*-*-"""


class TestPatternInput(object):
    '''
    Tests all of the views linked to the Pattern Input web page.
    '''

    def test_pattern_input_view(self):
        '''
        Tests the pattern input view, emulating when the user is visiting
        the page for the first time and there is currently no pattern
        waiting in the session.
        '''
        request = DummyRequest(route='/create')

        response = pattern_input_view(request)

        # Test there was a response
        assert response

        # Test the correct presentational values are returned
        assert response["page"] == "patternpage"
        assert response["title"] == "Create Pattern"
        assert "pattern" not in response.keys()

    def test_pattern_input_view_pattern(self):
        '''
        Tests the pattern input view, emulating when the user is re-visiting
        the page and a pattern they have already created is waiting for them
        in the session.
        '''
        request = DummyRequest(route='/create')
        input = create_input_pattern()
        request.session["pattern"] = input

        response = pattern_input_view(request)

        # Test there was a response
        assert response

        # Test the correct presentational values are returned
        assert response["page"] == "patternpage"
        assert response["title"] == "Create Pattern"
        assert response["pattern"] == input.replace('\n', "\\n")

    def test_pattern_input_receiver_JSON(self):
        '''
        Tests the JSON receiver view linked to the Pattern Input web page.
        '''
        # Setup
        request = DummyRequest(route='/pattern_receiver.json')
        input = create_input_pattern()
        request.body = json.dumps(input)
        request.content_type = "application/json"

        request.json_body = input

        response = pattern_input_receiver_JSON(request)

        # Test correct input has been given to session
        assert request.session["pattern"] == input

        responseDict = response
        # Test correct number of turns has passed
        assert responseDict["turns"] == 53

        # Test correct time has been calculated
        assert responseDict["runtime"] == TIME_DELAY * 53
