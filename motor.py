#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

def forward(x):
    GPIO.output(13, GPIO.HIGH)
    sleep(x)
    GPIO.output(13, GPIO.LOW)

def reverse(x):
    GPIO.output(11, GPIO.HIGH)
    sleep(x)
    GPIO.output(11, GPIO.LOW)

duration=18

forward(duration)
sleep(5)
reverse(duration-2)

GPIO.cleanup()
