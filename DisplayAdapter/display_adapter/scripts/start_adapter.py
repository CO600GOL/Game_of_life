"""
This script starts the display adapter, using threading to start the database receiver and the display driver.
"""

from threading import Thread
from display_adapter.display_driver.display_drivers import DisplayDriver
from display_adapter.database_receiver.database_receivers import DatabaseReceiver

if __name__ == "__main__":
    Thread(target=DatabaseReceiver().start).start()
    Thread(target=DisplayDriver().start).start()
