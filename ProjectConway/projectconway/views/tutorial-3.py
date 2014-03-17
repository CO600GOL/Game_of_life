from pyramid.view import view_config

@view_config(route_name='tutorial3', renderer='projectconway:templates/tutorial-3.mako')
def tutorial3_view(request):
    '''
    Executes the logic for the third tutorial web page, allowing the user to access the
    third page of the tutorial process.
    '''
    return {'title': 'Tutorial3',
            'page': 'tutorial3page'}