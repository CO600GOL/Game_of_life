"""
This module contains logic that tests the view linking the rules page to the Pyramid application.
"""

from pyramid.testing import DummyRequest
from projectconway.views.rules import rules_view


class TestRules(object):
    """
    This class tests the functionality of the Rules view.
    """

    def test_rules_view(self):
        """
        This method tests the functionality of the Rules view.
        """
        # Setup
        request = DummyRequest(route='/rules')

        response = rules_view(request)

        # Assert that a response has been given.
        assert response
        # Assert that the correct response data has been retrieved.
        assert response["page"] == "rulespage"
        assert response["title"] == "Rules"