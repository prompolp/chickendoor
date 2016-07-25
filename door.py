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
REED_OPEN=19
REED_CLOSE=15
LOCK_ENGAGE=9

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(FORWARD, GPIO.OUT)
    GPIO.setup(REVERSE, GPIO.OUT)
    GPIO.setup(REED_OPEN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(REED_CLOSE, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def cleanup():
    GPIO.cleanup()

def open():
    if door.isOpen():
	return
    print('%s : DOOR Opening...' % (datetime.datetime.now()))
    GPIO.output(FORWARD, GPIO.HIGH)
    while GPIO.input(REED_OPEN):
        time.sleep(1.5)
    print('%s : DOOR Opened!' % (datetime.datetime.now()))
    GPIO.output(FORWARD, GPIO.LOW)

def isOpen():
    if not GPIO.input(REED_OPEN):
        print('%s : DOOR Open!' % datetime.datetime.now())

def forward(seconds):
    GPIO.output(FORWARD, GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(FORWARD, GPIO.LOW)
    
def close():
    if door.isClosed():
        return
    print('%s : DOOR Closing...' % (datetime.datetime.now()))
    GPIO.output(REVERSE, GPIO.HIGH)
    while GPIO.input(REED_CLOSE):
        time.sleep(LOCK_ENGAGE)
    print('%s : DOOR Closed!' % (datetime.datetime.now()))
    GPIO.output(REVERSE, GPIO.LOW)

def isClosed():
    if not GPIO.input(REED_CLOSE):
        print('%s : DOOR Closed!' % datetime.datetime.now())

def reverse(seconds):
    GPIO.output(REVERSE, GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(REVERSE, GPIO.LOW)
