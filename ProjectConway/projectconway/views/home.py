"""
This module contains logic for the home page of the web application, from which the user can visit any page of the
application.
"""

from pyramid.view import view_config

@view_config(route_name='home', renderer='homepage.mako')
<<<<<<< HEAD:ProjectConway/projectconway/views/home_page.py
def home_page_view(request):
    """
    This function executes the logic for the home page, allowing the user to access Project Conway.

    @param request The request sent to this page of the web application.
    """
=======
def home_view(request):
    '''
    Executes the logic for the index (home) web page, allowing the user
    to access Project Conway.
    '''
>>>>>>> 1d5db25e9f79e1673e0e1503cfe0183f5ab5553a:ProjectConway/projectconway/views/home.py
    return {'title': 'Home',
            'page': 'homepage'}