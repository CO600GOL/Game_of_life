from pyramid.view import view_config

@view_config(route_name='tutorial2', renderer='projectconway:templates/tutorial-2.mako')
def tutorial2_view(request):
    '''
    Executes the logic for the second tutorial web page, allowing the user to access the
    second page of the tutorial process.
    '''
    return {'title': 'Tutorial2',
            'page': 'tutorial2page'}