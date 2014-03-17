"""
This __init__ file holds some centralised information for the display_adapter library.
"""

# Database information
db_name = "internal_db.sqlite"
test_db_name = "test_internal_db.sqlite"
db_receiver_url = "http://127.0.0.1:6543/run_transmitter.json"
db_receiver_polling_period = 1 # minutes

# Serial information
serial_name = "/dev/ttyACM0"
serial_baudrate = 9600
sleep_time = 0.5 # Amount of time the display sleeps between generations (in seconds)

# Information that is specific to the run mode animation
runmode_config = {
    "iterations": 3, # Number of iterations of "full" and "pattern" frames in the animation
    "full_frames": 1, # Number of "full" frames per animation iteration
    "pattern_frames": 2 # Number of "pattern" frames per animation iteration
}

# Information that is specific to the screensaver animation
screensaver_config = {
    "pause_frames": 3, #(exclusive)
}
