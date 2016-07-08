#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import RPi.GPIO as GPIO
import datetime
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def open():
    print('%s : DOOR Opening' % datetime.datetime.now())
    GPIO.output(13, GPIO.HIGH)
    while GPIO.input(15):
        time.sleep(1.5)
    print('%s : DOOR Open!' % datetime.datetime.now())
    GPIO.output(13, GPIO.LOW)

def close():
    print('%s : DOOR Closing!' % datetime.datetime.now())
    GPIO.output(11, GPIO.HIGH)
    while GPIO.input(15):
        time.sleep(1.5)
    print('%s : DOOR closed!' % datetime.datetime.now())
    GPIO.output(11, GPIO.LOW)

def cleanup():
    GPIO.cleanup()
