from pyramid.view import view_config

@view_config(route_name='about', renderer='projectconway:templates/about.mako')
def about_view(request):
    '''
    Executes the logic for the 'about' web page, allowing the user
    to access general information about the project and the people who created
    it.
    '''
    return {'title': 'About',
            'page': 'aboutpage'}