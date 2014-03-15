"""
This module contains testing logic for the Raspberry Pi's database receiver. The tests should make sure the database
receiver can correctly pull information from the web server and correctly write it to the Pi's internal database.
"""

import os
import json
import sqlite3
from mock import MagicMock, patch
from display_adapter import test_db_name
from display_adapter.scripts.init_db import init_db
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

    def setup_class(self):
        """
        This method is called before the testing logic runs to correctly set up the class. In this case, it
        initialises a test database.
        """
        try:
            init_db(test_db_name)
        except sqlite3.OperationalError:
            pass

    @patch('urllib.request.urlopen')
    def test__pull(self, mock_urllib):
        """
        Tests the database receiver's _pull method. The expected result of this test is that the information is
        correctly pulled from the database.

        @param mock_urllib A mock URL library used to represent the connection with the web server.
        """

        class FakeResponse(object):
            """
            Fake response object that mocks urllib.response
            """

            def read(self):
                """
                Mock the repsonse accessor
                """
                return bytes(TestDatabaseReceiver.runs, 'utf-8')

        mock_urllib.return_value = FakeResponse()

        dr = DatabaseReceiver()
        runs = dr._pull_runs()

        # Assert that runs has been properly defined
        assert runs
        # Assert tht runs contains the right information - A JSON string representing the database table from which
        # the data will be pulled.
        assert runs == json.loads(self.runs)

    def test__write_runs(self):
        """
        Tests the database receiver's _write_runs method. The expected result of this test is that data can be
        correctly written to the database.
        """
        dr = DatabaseReceiver(db_name=test_db_name)

        runs = json.loads(self.runs)
        dr._write_runs(runs)

        con = sqlite3.connect(test_db_name)
        try:
            # Assert that the data can be pulled from the database table. This shows it has been correctly inserted.
            assert con.execute("SELECT * FROM runs WHERE runs.id = %s" % runs[0]["id"]).fetchone()
        except:
            raise
        finally:
            con.close()

    def teardown_class(self):
        """
        This method is called after the testing logic has been called, to correctly tear down the class. In this case
        it removes the test database from the filing system.
        """
        os.system("rm %s" % test_db_name)










