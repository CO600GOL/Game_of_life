from pyramid.testing import DummyRequest
from projectconway.views.tutorial2 import tutorial2_view

class TestTutorial2(object):
    '''
    Tests all the views releated to the second tutorial page.
    '''

    def test_tutorial2_view(self):
        '''
        Tests the tutorial-2 view to ensure it functions correctly.
        '''
        # Setup
        request = DummyRequest(route='tutorial2')
        response = tutorial2_view(request)

        # Test that a response has been given.
        assert response
        assert response["page"] == "tutorial2page"
        assert response["title"] == "Tutorial2"