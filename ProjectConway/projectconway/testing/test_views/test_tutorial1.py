from pyramid.testing import DummyRequest
from projectconway.views.tutorial1 import tutorial1_view

class TestTutorial1(object):
    '''
    Tests all the views releated to the first tutorial page.
    '''

    def test_tutorial1_view(self):
        '''
        Tests the tutorial-1 view to ensure it functions correctly.
        '''
        # Setup
        request = DummyRequest(route='tutorial1')
        response = tutorial1_view(request)

        # Test that a response has been given.
        assert response
        assert response["page"] == "tutorial1page"
        assert response["title"] == "Tutorial1"