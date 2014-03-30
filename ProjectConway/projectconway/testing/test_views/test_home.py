"""
This module contains the logic to test the home page view, linking the python template to the Pyramid framework. These
tests must evaluate the communication through the view, making sure the correct responses are being retrieved.
"""

from pyramid.testing import DummyRequest
from projectconway.views.home import home_view


class TestHome(object):
    """
    This class tests the home page view.
    """

    def test_home_view(self):
        """
        This method tests the functionality of the home view. The expected result of this test is for the correct
        page information to be stored in the response dictionary.
        """

        request = DummyRequest(route='/')
        response = home_view(request)

        # Assert that a response has been given
        assert response

        # Assert that the correct page information has been stored in the response
        assert response["title"] == 'Home'
        assert response["page"] == 'homepage'

