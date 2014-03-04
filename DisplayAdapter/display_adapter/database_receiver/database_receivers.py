"""
This module contains the client-side logic for the raspberry pi's database receiver, pulling user's patterns from the
server into the pi's internal database.
"""

from urllib import request

class DatabaseReceiver(object):
    """
    This class is responsible for retrieving data from the web server and writing it to the pi's internal server.
    """

    def __init__(self, db_name):
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
        pass

    def _write_runs(self, runs):
        """
        This method allows the receiver to write information into the internal database.
        """
        pass