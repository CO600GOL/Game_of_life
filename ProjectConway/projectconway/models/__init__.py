"""
This module contains the logic for initialising the server-side SQL database session.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DBSession = scoped_session(sessionmaker())
Base = declarative_base()

def initialize_sql(engine):
    """
    This function initialises the database and binds it to the specified engine.

    @param engine The SQL engine with which to bind the database and its session.
    """
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
