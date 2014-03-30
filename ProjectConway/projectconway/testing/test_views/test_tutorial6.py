from pyramid.testing import DummyRequest
from projectconway.views.tutorial6 import tutorial6_view

class TestTutorial6(object):
    '''
    Tests all the views releated to the sixth tutorial page.
    '''

    def test_tutorial6_view(self):
        '''
        Tests the tutorial-6 view to ensure it functions correctly.
        '''
        # Setup
        request = DummyRequest(route='tutorial6')
        response = tutorial6_view(request)

        # Test that a response has been given.
        assert response
        assert response["page"] == "tutorial6page"
        assert response["title"] == "Tutorial6"