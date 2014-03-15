"""
This python script initialises the raspberry pi's internal database.
"""
import sys
import sqlite3
from display_adapter import db_name

help_message = """
This initialises an sqlite3 db for the purposes of the DisplayAdapter programs.

Arguments: init_db.py database_name
"""

# SQLite 3 table in which to hold the users' patterns and the time at which they are to be run.
runs_table = """
CREATE TABLE runs (
    id INTEGER NOT NULL,
    input_pattern VARCHAR,
    time_slot DATETIME,
    user_name VARCHAR(50),
    PRIMARY KEY (id)
)
"""

# SQLite 3 table in which to hold the screensaver patterns played when the display is not showing a user's patterns
screensavers_table = """
CREATE TABLE screensavers (
    pattern VARCHAR
)
"""


def init_db(db_name=db_name):
    """
    This function takes a database name and creates the database required for the DisplayAdapter programs.

    @param db_name the name of the database with which the applications should connect.
    """
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    try:
        # Attempt to set up the database
        cur.execute("pragma journal_mode=wal")
        cur.execute(runs_table)
        cur.execute(screensavers_table)
        con.commit()
    except sqlite3.OperationalError:
        # If the code drops into this except, then one of the tables already exists.
        pass
    con.close()


# Run this script if the module is called from the command line
if __name__ == "__main__":
    if len(sys.argv) > 2:
        if sys.argv[1].lower() == "help":
            print(help_message)
        else:
            init_db(sys.argv[1])
    else:
        init_db()