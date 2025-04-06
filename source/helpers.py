"""
Helper functions
"""

import os

def clear():
    """
    Clears the console
    """
    os.system('cls' if os.name=='nt' else 'clear')

def wait(seconds):
    """
    Waits for a given number of seconds and is required since the time module is not allowed.
    """
    # Get the current time in seconds
    # os.times() returns a tuple, the 5th element is the elapsed time
    start_time = os.times()[4]

    # Busy-wait loop
    while True:
        current_time = os.times()[4]
        elapsed_time = current_time - start_time
        if elapsed_time >= seconds:
            break
