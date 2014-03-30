from pyramid.testing import DummyRequest
from projectconway.views.tutorial4 import tutorial4_view

class TestTutorial4(object):
    '''
    Tests all the views releated to the fourth tutorial page.
    '''

    def test_tutorial4_view(self):
        '''
        Tests the tutorial-4 view to ensure it functions correctly.
        '''
        # Setup
        request = DummyRequest(route='tutorial4')
        response = tutorial4_view(request)

        # Test that a response has been given.
        assert response
        assert response["page"] == "tutorial4page"
        assert response["title"] == "Tutorial4"