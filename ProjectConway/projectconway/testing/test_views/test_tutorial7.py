from pyramid.testing import DummyRequest
from projectconway.views.tutorial7 import tutorial7_view

class TestTutorial7(object):
    '''
    Tests all the views releated to the seventh tutorial page.
    '''

    def test_tutorial7_view(self):
        '''
        Tests the tutorial-7 view to ensure it functions correctly.
        '''
        # Setup
        request = DummyRequest(route='tutorial7')
        response = tutorial7_view(request)

        # Test that a response has been given.
        assert response
        assert response["page"] == "tutorial7page"
        assert response["title"] == "Tutorial7"