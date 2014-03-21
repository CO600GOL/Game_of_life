"""
This module contains the logic for the About page of the web application, where the user can access information
about the people who built the project.
"""

from pyramid.view import view_config

@view_config(route_name='about', renderer='projectconway:templates/about.mako')
def about_view(request):
    """
    This function executes the logic for the about page.

    @param request The request sent to this page of the web application.
    """
    return {'title': 'About',
            'page': 'aboutpage'}