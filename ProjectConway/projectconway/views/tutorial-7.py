from pyramid.view import view_config

@view_config(route_name='tutorial7', renderer='projectconway:templates/tutorial-7.mako')
def tutorial7_view(request):
    '''
    Executes the logic for the seventh tutorial web page, allowing the user to access the
    seventh page of the tutorial process.
    '''
    return {'title': 'Tutorial7',
            'page': 'tutorial7page'}