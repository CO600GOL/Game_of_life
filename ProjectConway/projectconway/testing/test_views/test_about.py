from pyramid.testing import DummyRequest
from projectconway.views.about import about_view


class TestAbout(object):
    """
    Tests all the views related to the About page.
    """

    def test_about_view(self):
        """
        Tests the about view to ensure that it works correctly.
        """
        # Setup
        request = DummyRequest(route='/about')

        response = about_view(request)

        # Test that a response has been given.
        assert response
        assert response["page"] == "aboutpage"
        assert response["title"] == "About"