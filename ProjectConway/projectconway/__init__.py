import datetime
from pyramid.config import Configurator
from pyramid.renderers import JSON
from sqlalchemy import engine_from_config
from .models import initialize_sql
from pyramid.session import UnencryptedCookieSessionFactoryConfig

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings,
                          session_factory=
                          UnencryptedCookieSessionFactoryConfig(secret='projectconway',
                                                                cookie_name='projectconway'))
    config.scan('projectconway.models')

    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)

    # Template engines
    config.include('pyramid_mako')
    config.add_renderer("conway_json", JSON(indent=4))

    # View setups
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('create', '/create')
    config.add_route('pattern_input_receiver', '/pattern_receiver.json')
    config.add_route('pattern_input_clearer', '/pattern_clearer.json')
    config.add_route('time_slot_receiver', '/scheduler.json')
    config.add_route('confirmation_receiver', '/confirm.json')
    config.add_route('run_transmitter', '/run_transmitter.json')
    config.add_route('about', '/about')
    config.add_route('tutorial1', '/tutorial-1')
    config.scan()

    return config.make_wsgi_app()

display_location = {
    "name": "Beany House of Art and Knowledge",
    "address": """Beany House of Art and Knowledge,
18 High Street,
Canterbury,
Kent,
CT1 2RA""",
    "link": "www.canterbury.co.uk/Beaney",
    "picture": "/static/images/#"
}

project_config = {
    # Starting hour, difference from midnight
    "starting_hour": datetime.timedelta(hours=6),
    # Closing hour, deifference from midnight
    "closing_hour": datetime.timedelta(hours=21),
    # Minimum date, should really be now
    "minimum_date": datetime.timedelta(),
    # Maximum_date, the max date the user can book
    "maximum_date": datetime.timedelta(weeks=3)
}