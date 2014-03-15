"""
This script pulls all available screensavers from the screensavers.txt file and puts them in the raspberry pi's
internal database.
"""

import json
import sqlite3
from display_adapter import db_name

current_file = "display_adapter/scripts/screensavers.txt"

# Run this script if it is called from the command line.
if __name__ == "__main__":
    with open(current_file, "r") as file:
        screensavers = json.loads(file.read())

        if screensavers:
            # Connect to the raspberry pi's internal database.
            con = sqlite3.connect(db_name)

            for screensaver in screensavers:
                screensaver = "\n".join(screensaver)
                #SQLite 3 statement for writing screensaver's to the internal database.
                statement = """
INSERT INTO screensavers
    SELECT "%s"
    WHERE NOT EXISTS (SELECT * FROM screensavers WHERE pattern = "%s")
""" % (screensaver, screensaver)
                con.execute(statement)

            # Commit the changes and close the database connection.
            con.commit()
            con.close()


