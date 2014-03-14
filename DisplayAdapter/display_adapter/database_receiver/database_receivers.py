"""
This module contains the logic for the raspberry pi's database receiver. The database receiver serves as client-side
communication for the display controller, pulling in data from the web server and writing it to the pi's internal
database. The data being pulled consists of users' patterns and the datetime at which they are to be run.
"""

import time
import json
import sqlite3
import datetime
import logging
from urllib import error, request
from display_adapter import db_receiver_url, db_name, db_receiver_polling_period

class DatabaseReceiver(object):
    """
    This class is responsible for retrieving data from the web server and writing it to the pi's internal database.
    """

    logger = logging.getLogger("display")

    def __init__(self, db_name=db_name):
        """
        Ctor - initialises the database receiver with the given name.

        @param db_name The name the database is to be given.
        """
        self.db_name = db_name

    def start(self):
        """
        This method starts up the database receiver. This entails constantly pulling information in from the server
        and writes it to the internal database.
        """

        while True:
            current_time = datetime.datetime.now()

            try:
                # Attempt to pull runs from the server-side database.
                runs = self._pull_runs()
            except (error.URLError, error.HTTPError) as e:
                # If the pi is unable to communicate with the server, there will have been a URL error or a HTTP
                # error
                self.logger.error("Failed to gather runs: %s" % e)
            else:
                # Else the data can be written to the internal database.
                self._write_runs(runs)
                self.logger.warn("Added runs to internal database")

            # Wait for the polling period until running the loop again.
            sleep_until_time = current_time + datetime.timedelta(minutes=db_receiver_polling_period)
            time.sleep((sleep_until_time - datetime.datetime.now()).seconds)

    def _pull_runs(self):
        """
        This is a helper method that pulls data from the server-side database.

        @return string A string representing the URL request response, which will contain data concerning users'
                       patterns and the datetime at which they are to run.
        """
        data = "min_time=%s" % datetime.datetime.now().isoformat()
        data = data.encode('utf-8')

        res = request.urlopen(db_receiver_url, data)

        return json.loads(res.read().decode('utf-8'))

    def _write_runs(self, runs):
        """
        This is a helper method that writes the information received by _pull_runs to the raspberry pi's internal
        database.

        @param runs The runs received, to be written to the database.
        """
        # Connect to the client-side database
        con = sqlite3.connect(self.db_name, timeout=30, check_same_thread=False)

        for run in runs:
            # Format the time of each run correctly for the database
            time = datetime.datetime.strptime(run["time_slot"], "%Y-%m-%dT%H:%M:%S")

            # This is the SQL statement, written for SQLite 3.
            statement = """
INSERT INTO runs values (%s, "%s", "%s", "")
""" % (run["id"], run["input_pattern"].replace("\\n", "\n"), time.strftime("%Y-%m-%d %H:%M:00.000000"))

            con.execute(statement)

        # Once all the runs have been added to the database, commit the changes and close the connection.
        con.commit()
        con.close()


if __name__ == "__main__":
    # Start the database receiver if this module is called from the command line.
    DatabaseReceiver().start()