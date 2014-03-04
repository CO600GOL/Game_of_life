"""
This view is responsible for the logic that trasmits currently unsent patterns on the server
to the raspberry pi controlloing the display.
"""

from pyramid.view import view_config

@view_config(route_name='home', renderer='homepage.mako')
def run_transmitter_view(request):
    """
    Executes the transmission of unsent server patterns to the display.
    """
    pass