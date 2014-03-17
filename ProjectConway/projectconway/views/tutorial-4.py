from pyramid.view import view_config

@view_config(route_name='tutorial4', renderer='projectconway:templates/tutorial-4.mako')
def tutorial4_view(request):
    '''
    Executes the logic for the fourth tutorial web page, allowing the user to access the
    fourth page of the tutorial process.
    '''
    return {'title': 'Tutorial4',
            'page': 'tutorial4page'}