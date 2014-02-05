from pyramid.view import view_config

@view_config(route_name='rules', renderer='projectconway:templates/rules.mako')
def home_page_view(request):
    '''
    Executes the rules page allowing the user to learn the rules of the game
    of life. 
    '''
    return {'title': 'Rules',
            'page': 'rulespage'}