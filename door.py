#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import door
import RPi.GPIO as GPIO
import datetime
import time

FORWARD=11
REVERSE=13
REED_OPEN=15
REED_CLOSE=19

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(FORWARD, GPIO.OUT)
    GPIO.setup(REVERSE, GPIO.OUT)
    GPIO.setup(REED_OPEN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(REED_CLOSE, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def open():
    print('%s : DOOR Opening...' % (datetime.datetime.now()))
    GPIO.output(FORWARD, GPIO.HIGH)
    while GPIO.input(REED_OPEN):
        time.sleep(1.5)
    print('%s : DOOR Opened!' % (datetime.datetime.now()))
    GPIO.output(FORWARD, GPIO.LOW)

def close():
    print('%s : DOOR Closing...' % (datetime.datetime.now()))
    GPIO.output(REVERSE, GPIO.HIGH)
    while GPIO.input(REED_CLOSE):
        time.sleep(5)
    print('%s : DOOR Closed!' % (datetime.datetime.now()))
    GPIO.output(REVERSE, GPIO.LOW)

def forward(seconds)
    GPIO.output(FORWARD, GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(FORWARD, GPIO.LOW)
    
def reverse(seconds)
    GPIO.output(REVERSE, GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(REVERSE, GPIO.LOW)

def cleanup():
    GPIO.cleanup()
