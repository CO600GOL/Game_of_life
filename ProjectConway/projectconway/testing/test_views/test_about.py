"""
This module contains logic that tests the view linking the about page to the Pyramid application.
"""

from pyramid.testing import DummyRequest
from projectconway.views.about import about_view


class TestAbout(object):
    """
    This class tests the functionality of the About view.
    """

    def test_about_view(self):
        """
        This method tests the functionality of the About view.
        """
        # Setup
        request = DummyRequest(route='/about')

        response = about_view(request)

        # Assert that a response has been given.
        assert response
        # Assert that the response data is correct.
        assert response["page"] == "aboutpage"
        assert response["title"] == "About"