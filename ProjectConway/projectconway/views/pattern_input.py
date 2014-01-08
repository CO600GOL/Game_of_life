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


@view_config(route_name="pattern_input_receive")
def pattern_input_receiver_JSON(request):
    '''
    This view receives a customers pattern input in the form of a JSON 
    string. We then run a gameoflife for that pattern and return the number 
    of seconds and turns it will run for, taking into consideration the 5 minute
    run time and delays. 
    '''
    pass
