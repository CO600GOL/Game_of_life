__author__ = 'richard'

db_name = "internal_db.sqlite"
test_db_name = "test_internal_db.sqlite"
serial_name = "/dev/tty1"
serial_baudrate = 9600
sleep_time = 0.5 # Amount of time the display sleeps between generations

# Information that is specific to the run mode animation
runmode_config = {
    "iterations": 3, # Number of iterations of "full" and "pattern" frames in the animation
    "full_frames": 1, # Number of "full" frames per animation interation
    "pattern_frames": 2 # Number of "pattern" frames per animation iteration
}

# Information that is specific to the screensaver animation
screensaver_config = {
    "pause_frames": 3, #(exclusive)
}
