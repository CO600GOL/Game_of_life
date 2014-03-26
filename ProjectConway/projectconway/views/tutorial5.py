from pyramid.view import view_config

@view_config(route_name='tutorial5', renderer='projectconway:templates/tutorial-5.mako')
def tutorial5_view(request):
    '''
    Executes the logic for the fifth tutorial web page, allowing the user to access the
    fifth page of the tutorial process.
    '''
    return {'title': 'Tutorial5',
            'page': 'tutorial5page'}