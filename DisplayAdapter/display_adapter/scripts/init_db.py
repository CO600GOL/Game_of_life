"""
Script that is run from the command line in order to
"""
import sys
import sqlite3
from display_adapter import db_name

help_message = """
This initialises an sqlite3 db for the purposes of the DisplayAdapter programs.

Arguments: init_db.py database_name
"""

runs_table = """
CREATE TABLE runs (
    id INTEGER NOT NULL,
    input_pattern VARCHAR,
    time_slot DATETIME,
    user_name VARCHAR(50),
    PRIMARY KEY (id)
)
"""

screensavers_table = """
CREATE TABLE screensavers (
    pattern VARCHAR
)
"""


def init_db(db_name=db_name):
    """
    This function takes a database name and creates the database required
    for the DisplayAdapter programs
    """
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    cur.execute(runs_table)
    cur.execute(screensavers_table)

    con.commit()
    con.close()


if __name__ == "__main__":
    if len(sys.argv) > 2:
        if sys.argv[1].lower() == "help":
            print(help_message)
        else:
            init_db(sys.argv[1])
    else:
        init_db()