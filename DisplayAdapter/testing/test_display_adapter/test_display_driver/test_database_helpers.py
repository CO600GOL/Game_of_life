"""
This module tests all the logic involved in the display driver's
(indirect) communication with the Raspberry Pi's internal database.
"""
import os
import sqlite3
from display_adapter import test_db_name
from display_adapter.scripts.init_db import init_db
from display_adapter.display_driver.database_helpers import DatabaseHelper


class TestDatabaseHelper(object):
    """
    This class tests the logic contained in the DatabaseHelper helper class
    for the display driver.
    """

    def setup_class(self):
        """
        Sets up the class for testing.
        """
        try:
            init_db(test_db_name)
        except sqlite3.OperationalError:
            pass

    def test_init(self):
        """
        Tests the initialisation of the DatabaseHelper
        """
        # Assert that initialisation works correctly
        database_helper = DatabaseHelper(db_name=test_db_name)
        assert database_helper

        # Assert the connection to the internal database has been made
        assert database_helper._db_connection

    def test_get_run_for_time(self):
        """
        Tests the ability of the database helper to retrieve a run for a specified time from the internal database.
        """
        # Set up a database helper for testing:
        #   - Put a run in the test database to be pulled out
        #   - Create a datetime object to be passed to the testing method
        database_helper = DatabaseHelper(db_name=test_db_name)
        con = database_helper._db_connection
        time = "2014-02-28 21:20:00.000000"
        con.execute("INSERT INTO runs VALUES (0, 'TEST','%s','');" % time)
        con.commit()

        # Run tests
        assert database_helper.get_run_for_time(time) == "TEST"
        assert not con.execute("SELECT * FROM runs WHERE time_slot='%s'" % time).fetchone()

    def test_get_random_screensaver(self):
        """
        Tests the ability of the database helper to retrieve a random screen saver from the internal database.
        """
        database_helper = DatabaseHelper(db_name=test_db_name)
        con = database_helper._db_connection

        con.execute("INSERT INTO screensavers VALUES ('TEST');")
        con.execute("INSERT INTO screensavers VALUES ('TEST1');")
        con.execute("INSERT INTO screensavers VALUES ('TEST2');")
        con.commit()

        assert database_helper.get_random_screensaver()

    def teardown_class(self):
        """
        Remove the internal database
        """
        os.system("rm %s" % test_db_name)