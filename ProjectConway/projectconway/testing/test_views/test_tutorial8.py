from pyramid.testing import DummyRequest
from projectconway.views.tutorial8 import tutorial8_view

class TestTutorial8(object):
    '''
    Tests all the views releated to the eighth tutorial page.
    '''

    def test_tutorial8_view(self):
        '''
        Tests the tutorial-8 view to ensure it functions correctly.
        '''
        # Setup
        request = DummyRequest(route='tutorial8')
        response = tutorial8_view(request)

        # Test that a response has been given.
        assert response
        assert response["page"] == "tutorial8page"
        assert response["title"] == "Tutorial8"