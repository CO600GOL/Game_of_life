"""
This module contains the client-side logic for the raspberry pi's database receiver, pulling user's patterns from the
server into the pi's internal database.
"""

import json
import sqlite3
from urllib import request
from display_adapter import db_receiver_url, db_name

class DatabaseReceiver(object):
    """
    This class is responsible for retrieving data from the web server and writing it to the pi's internal server.
    """

    def __init__(self, db_name=db_name):
        """
        Init for the DatabaseReciever
        """
        pass

    def start(self):
        """
        This is ths method in which the database does its work.
        """
        pass

    def _pull_runs(self):
        """
        This method allows the receiver to pull data from the web server.
        """
        res = request.urlopen(db_receiver_url)
        return json.loads(res.read())

    def _write_runs(self, runs):
        """
        This method allows the receiver to write information into the internal database.
        """
        pass