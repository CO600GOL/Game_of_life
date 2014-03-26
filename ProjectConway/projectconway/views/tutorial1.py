from pyramid.view import view_config

@view_config(route_name='tutorial1', renderer='projectconway:templates/tutorial-1.mako')
def tutorial1_view(request):
    '''
    Executes the logic for the first tutorial web page, allowing the user to access the
    first page of the tutorial process.
    '''
    return {'title': 'Tutorial1',
            'page': 'tutorial1page'}