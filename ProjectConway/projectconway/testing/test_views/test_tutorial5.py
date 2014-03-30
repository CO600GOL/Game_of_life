from pyramid.testing import DummyRequest
from projectconway.views.tutorial5 import tutorial5_view

class TestTutorial5(object):
    '''
    Tests all the views releated to the fifth tutorial page.
    '''

    def test_tutorial5_view(self):
        '''
        Tests the tutorial-5 view to ensure it functions correctly.
        '''
        # Setup
        request = DummyRequest(route='tutorial5')
        response = tutorial5_view(request)

        # Test that a response has been given.
        assert response
        assert response["page"] == "tutorial5page"
        assert response["title"] == "Tutorial5"