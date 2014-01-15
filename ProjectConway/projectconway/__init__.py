from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import initialize_sql
from pyramid.session import UnencryptedCookieSessionFactoryConfig


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings,
                          session_factory=UnencryptedCookieSessionFactoryConfig(secret='projectconway', cookie_name='projectconway'))
    config.scan('projectconway.models')
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('pattern_input', '/create')
    config.add_route('pattern_input_receiver', '/pattern_receiver.json')
    config.add_route('about', '/about')
    config.scan()
    return config.make_wsgi_app()
