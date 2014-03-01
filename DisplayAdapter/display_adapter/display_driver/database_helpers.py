"""
This module contains the logic for any helper classes
that support the display driver in interacting with the
Raspberry Pi's internal database.
"""

import sqlite3
from display_adapter import db_name


class DatabaseHelper(object):
    """
    This class is a helper for the DisplayDriver, taking all responsibility for communication with the database
    away from the driver itself.
    """

    def __init__(self, db_name=db_name):
        """
        Ctor - constructs the database helper, linking to the database with the given name
        """
        self._db_connection = sqlite3.connect(db_name, timeout=5)

    def get_run_for_time(self, time):
        """
        This method queries the internal database for the run to be played at the specified time.
        """
        statement = """
SELECT * FROM runs
WHERE runs.time_slot = '%s'""" % time
        delete_statement = """
DELETE FROM runs
WHERE id=%s"""

        patern = ""
        run = self._db_connection.execute(statement).fetchone()
        if run:
            (_id, pattern, _, _) = run
            self._db_connection.execute(delete_statement%_id)

        return pattern

    def get_random_screensaver(self):
        """
        This method queries the internal database for a random screen saver to display.
        """
        statement = """
SELECT * FROM screensavers ORDER BY RANDOM() LIMIT 1;
        """

        return self._db_connection.execute(statement).fetchone()

    def __del__(self):
        """
        Called when the object is destructd
        """
        self._db_connection.close()