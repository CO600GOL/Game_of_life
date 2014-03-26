from pyramid.view import view_config

@view_config(route_name='tutorial6', renderer='projectconway:templates/tutorial-6.mako')
def tutorial6_view(request):
    '''
    Executes the logic for the sixth tutorial web page, allowing the user to access the
    sixth page of the tutorial process.
    '''
    return {'title': 'Tutorial6',
            'page': 'tutorial6page'}