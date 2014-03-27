from pyramid.testing import DummyRequest
from projectconway.views.tutorial3 import tutorial3_view

class TestTutorial3(object):
    '''
    Tests all the views releated to the third tutorial page.
    '''

    def test_tutorial3_view(self):
        '''
        Tests the tutorial-3 view to ensure it functions correctly.
        '''
        # Setup
        request = DummyRequest(route='tutorial3')
        response = tutorial3_view(request)

        # Test that a response has been given.
        assert response
        assert response["page"] == "tutorial3page"
        assert response["title"] == "Tutorial3"