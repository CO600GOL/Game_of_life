"""
This module contains the logic that takes care of the display driver's communication with the Raspberry Pi's internal
database, pulling data from it. The data can be a user's pattern, from the database's runs table, or a random
'screensaver' pattern, from the screensavers table.
"""

import sqlite3
from display_adapter import db_name


class DatabaseHelper(object):
    """
    This class takes responsibility for communication with the internal database away from the DisplayDriver,
    retrieving users' patterns and screensaver patterns.
    """

    def __init__(self, db_name=db_name):
        """
        Ctor - initialises the DatabaseHelper, linking the DisplayDriver to the database with the given name.

        @param db_name The name of the database with which the driver will be linked.
        """
        # Connect to the internal database with the given name. Should the connection fail, wait 30 seconds before
        # timeout, and don't check whether the connection is on the same thread as another database connection
        self._db_connection = sqlite3.connect(db_name, timeout=30, check_same_thread=False)

    def get_run_for_time(self, time):
        """
        This method retrieves a run for the given time from the internal database.

        @param time The time slot for which this helper queries the database, receiving a run.

        @return pattern The pattern to be shown at the specified time slot.
        """
        # The statement for the database, written for SQLite 3, to query the database for a run given at the specified
        # time.
        statement = """
SELECT * FROM runs
WHERE runs.time_slot = '%s'""" % time
        delete_statement = """
DELETE FROM runs
WHERE id=%s"""

        pattern = ""
        run = self._db_connection.execute(statement).fetchone()
        if run:
            # If a run has been successfully retrieved, save its ID and the pattern saved to it to local variables
            # and delete the run from the database.
            (_id, pattern, _, _) = run
            self._db_connection.execute(delete_statement%_id)

        # Commit the changes to the database
        self._db_connection.commit()

        return pattern

    def get_random_screensaver(self):
        """
        This method queries the internal database for a random screen saver to display.

        @return A screensaver pattern from the internal database.
        """
        # The statement for the database, written for SQLite 3, to query the database for a random screensaver pattern.
        statement = """
SELECT * FROM screensavers ORDER BY RANDOM() LIMIT 1;
        """

        # Execute the statement and return the query result
        return self._db_connection.execute(statement).fetchone()[0]

    def __del__(self):
        """
        Dtor - deconstructs an object of this class, closing the database connection.
        """
        self._db_connection.close()