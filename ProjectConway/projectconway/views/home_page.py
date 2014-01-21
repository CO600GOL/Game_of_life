from pyramid.view import view_config

@view_config(route_name='home', renderer='projectconway:templates/homepage.mako')
def home_page_view(request):
    '''
    Executes the logic for the index (home) web page, allowing the user
    to access Project Conway.
    '''
    return {'title': 'Home',
            'page': 'homepage'}