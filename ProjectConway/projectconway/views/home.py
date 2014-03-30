"""
This module contains logic for the home page of the web application, from which the user can visit any page of the
application.
"""

from pyramid.view import view_config

@view_config(route_name='home', renderer='homepage.mako')
def home_view(request):
    """
    This function executes the logic for the home page, allowing the user to access Project Conway.

    @param request The request sent to this page of the web application.
    """
    return {'title': 'Home',
            'page': 'homepage'}