from pyramid.view import view_config

@view_config(route_name='home', renderer='../templates/index.pt')
def home_page_view(request):
    '''
    Executes the logic for the index (home) web page, allowing the user
    to access Project Conway.
    '''
    return {'name': 'Project Conway'}