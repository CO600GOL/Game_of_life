"""
This module contains the client-side logic for the raspberry pi's database receiver, pulling user's patterns from the
server into the pi's internal database.
"""

import time
import json
import sqlite3
import datetime
import logging
from urllib import request
from display_adapter import db_receiver_url, db_name, db_receiver_polling_period

class DatabaseReceiver(object):
    """
    This class is responsible for retrieving data from the web server and writing it to the pi's internal server.
    """

    logger = logging.getLogger("display")

    def __init__(self, db_name=db_name):
        """
        Init for the DatabaseReciever
        """
        self.db_name = db_name

    def start(self):
        """
        This is ths method in which the database does its work.
        """

        while True:
            current_time = datetime.datetime.now()

            runs = self._pull_runs()
            self._write_runs(runs)

            sleep_until_time = current_time + datetime.timedelta(minutes=db_receiver_polling_period)
            time.sleep((sleep_until_time - datetime.datetime.now()).seconds)

            self.logger.warn("Attempted to pull runs from server")

    def _pull_runs(self):
        """
        This method allows the receiver to pull data from the web server.
        """
        data = "min_time=%s" % datetime.datetime.now().isoformat()
        data = data.encode('utf-8')

        res = request.urlopen(db_receiver_url, data)

        return json.loads(res.read().decode('utf-8'))

    def _write_runs(self, runs):
        """
        This method allows the receiver to write information into the internal database.
        """
        con = sqlite3.connect(self.db_name, timeout=30, check_same_thread=False)

        for run in runs:
            time = datetime.datetime.strptime(run["time_slot"], "%Y-%m-%dT%H:%M:%S")

            statement = """
INSERT INTO runs values (%s, "%s", "%s", "")
""" % (run["id"], run["input_pattern"].replace("\\n", "\n"), time.strftime("%Y-%m-%d %H:%M:00.000000"))

            con.execute(statement)

        con.commit()
        con.close()


if __name__ == "__main__":
    DatabaseReceiver().start()