from pyramid.testing import DummyRequest
from projectconway.views.about import about_view


class TestRules(object):
    """
    Tests all the views related to the Rules page.
    """

    def test_rules_view(self):
        """
        Tests the rules view to ensure that it works correctly.
        """
        # Setup
        request = DummyRequest(route='/rules')

        response = rules_view(request)

        # Test that a response has been given.
        assert response
        assert response["page"] == "rulespage"
        assert response["title"] == "Rules"