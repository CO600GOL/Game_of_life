from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from projectconway.models import DBSession

@view_config(route_name='pattern_input')
def pattern_input_view(request):
    '''
    Executes the logic for the Pattern Input web page, allowing the user
    to input a pattern to the website - the application must then input
    that pattern to a session for persistance across pages.
    '''
    return Response('pass')
    