"""
This modules tests the client-side logic of the raspberry pi's database receiver, making sure it can correctly pull
information from the web server and correctly write it to the internal database.
"""

class TestDatabaseReceiver(object):
    """
    This class tests the logic contained in the DatabaseReceiver class, making sure it can communicate with the web
    server and the internal database correctly.
    """

    def test__pull(self):
        """
        Tests the _pull method of the database receiver. Should correctly pull data from the web server.
        """
        pass

    def test__write_runs(self):
        """
        Tests the _write_runs method of the database receiver. Should correctly write data to the pi's internal
        database.
        """
        pass