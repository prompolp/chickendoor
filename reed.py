#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import time
import RPi.GPIO as GPIO
import datetime

GPIO.setmode(io.BOARD)
door_pin = 15

GPIO.setup(door_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # activate input with PullUp

while True:
    if not GPIO.input(door_pin):
        print('%s : DOOR Closed!' % datetime.datetime.now())
    time.sleep(0.5)

