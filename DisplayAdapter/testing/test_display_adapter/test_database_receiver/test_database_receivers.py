"""
This modules tests the client-side logic of the raspberry pi's database receiver, making sure it can correctly pull
information from the web server and correctly write it to the internal database.
"""

import json
import sqlite3
from mock import MagicMock, patch
from display_adapter import test_db_name
from display_adapter.database_receiver.database_receivers import DatabaseReceiver

class TestDatabaseReceiver(object):
    """
    This class tests the logic contained in the DatabaseReceiver class, making sure it can communicate with the web
    server and the internal database correctly.
    """

    runs = """[
    {
        "input_pattern": "----------\\n----------\\n-*--*-----\\n----------\\n----------\\n----------\\n*---*-----\\n----------\\n--------*-\\n----------",
        "time_slot": "2014-03-04T23:20:00",
        "id": 6,
        "sent": true
    }
]"""


    @patch('urllib.request.urlopen')
    def test__pull(self, mock_urllib):
        """
        Tests the _pull method of the database receiver. Should correctly pull data from the web server.
        """

        class FakeResponse(object):
            """
            Fake response object that mocks the urliib.response
            """

            def read(self):
                """
                Mock the repsonse accessor
                """
                return self.runs

        mock_urllib.return_value = FakeResponse()

        dr = DatabaseReceiver()
        runs = dr._pull_runs()

        assert runs
        assert runs == self.runs

    def test__write_runs(self):
        """
        Tests the _write_runs method of the database receiver. Should correctly write data to the pi's internal
        database.
        """
        dr = DatabaseReceiver(db_name=test_db_name)

        runs = json.loads(self.runs)
        assert dr._write_runs(runs)

        con = sqlite3.connect(test_db_name)
        try:
            assert con.execute("SELECT * FROM runs WHERE runs.id = %s" % runs[0]["id"]).fetchone()
        except:
            raise
        finally:
            con.close()











