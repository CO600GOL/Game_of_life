from pyramid.view import view_config

@view_config(route_name='tutorial8', renderer='projectconway:templates/tutorial-8.mako')
def tutorial8_view(request):
    '''
    Executes the logic for the eighth tutorial web page, allowing the user to access the
    eighth page of the tutorial process.
    '''
    return {'title': 'Tutorial8',
            'page': 'tutorial8page'}