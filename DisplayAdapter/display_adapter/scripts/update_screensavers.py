"""
This script pulls all available screensavers from the screensavers.txt file and
puts them in the raspberry pi's internal database.
"""

import sqlite3
from display_adapter import db_name

if __name__ == "__main__":
    with open("display_adapter/scripts/screensavers.txt", "r") as file:
        screensavers = file.read()
        screensavers = screensavers.split("\n\n")

        if screensavers:
            con = sqlite3.connect(db_name)

            for screensaver in screensavers:
                statement = """
INSERT INTO screensavers
    SELECT "%s"
    WHERE NOT EXISTS (SELECT * FROM screensavers WHERE pattern = "%s")
""" % (screensaver, screensaver)
                con.execute(statement)

            con.commit()
            con.close()


