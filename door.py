#!/usr/bin/env python3

"""
Python source code - replace this with a description of the code and write the
code below this text.
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import RPi.GPIO as GPIO
import datetime
import time

PIN_MOTOR_FORWARD = 11
PIN_MOTOR_REVERSE = 13
PIN_SWITCH_DOOROPEN_POSITION = 19
PIN_SWITCH_DOORCLOSE_POSITION = 15

# Set the LOCK_ENGAGE_TIME to zero when there is no locking mechinisim.
LOCK_ENGAGE_TIME = 0


def setup():
    GPIO.setmode(GPIO.BOARD)

    # Define Motor Pins
    GPIO.setup(PIN_MOTOR_FORWARD, GPIO.OUT)
    GPIO.setup(PIN_MOTOR_REVERSE, GPIO.OUT)

    # Define Swich pins
    GPIO.setup(PIN_SWITCH_DOOROPEN_POSITION, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_SWITCH_DOORCLOSE_POSITION, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def cleanup():
    GPIO.cleanup()


def open():
    # if door is alread open do nothing.
    if isOpen():
        return


    print ('%s : DOOR Opening...') % datetime.datetime.now()
    setup()

    GPIO.output(PIN_MOTOR_FORWARD, GPIO.HIGH)
    while GPIO.input(PIN_SWITCH_DOOROPEN_POSITION):
        time.sleep(1.5)
    GPIO.output(PIN_MOTOR_FORWARD, GPIO.LOW)

    cleanup()
    print ('%s : DOOR Opened!') % datetime.datetime.now()


def close():
    # if door is alread closed do nothing.
    if not isOpen():
        return

    print ('%s : DOOR Closing...') % datetime.datetime.now()
    setup()

    GPIO.output(PIN_MOTOR_REVERSE, GPIO.HIGH)
    while GPIO.input(PIN_SWITCH_DOORCLOSE_POSITION):
        time.sleep(LOCK_ENGAGE_TIME)
    GPIO.output(PIN_MOTOR_REVERSE, GPIO.LOW)

    cleanup()
    print ('%s : DOOR Closed!') % datetime.datetime.now()


def forward(seconds):
    GPIO.output(PIN_MOTOR_FORWARD, GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(PIN_MOTOR_FORWARD, GPIO.LOW)


def reverse(seconds):
    GPIO.output(PIN_MOTOR_REVERSE, GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(PIN_MOTOR_REVERSE, GPIO.LOW)


def isOpen():
    if GPIO.input(PIN_SWITCH_DOOROPEN_POSITION):
        return True
    return False
