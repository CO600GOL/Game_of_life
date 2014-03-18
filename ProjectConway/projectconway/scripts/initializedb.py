"""
This module initialises the server-side database for the Pyramid application.
"""

import os
import sys
import transaction

from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings, setup_logging
from pyramid.scripts.common import parse_vars
from projectconway.models import Base, DBSession

def usage(argv):
    """
    This method prints the usage of the module to the command line if it is called there.

    @param argv The command line arguments.
    """
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    """
    Initialise the database if this module is called from the command line or external software.

    @param argv The system arguments from the command line or external software.
    """
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        pass
