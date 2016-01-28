#!/usr/bin/env python2.7
from pad4pi import rpi_gpio
import time
import RPi.GPIO as GPIO
import globals

def triggerAlarm():
	globals.ALARM_TRIGGERED = True
        GPIO.output(globals.ALARM_PIN, GPIO.HIGH)	
	print("SYSTEM ALARM IS SOUNDING!!!")

def resetAlarm():
    GPIO.output(globals.ALARM_PIN, GPIO.LOW)
    globals.ALARM_TRIGGERED = False
    globals.ALARM_SEQUENCE_STARTED = False
    print("Alarm is reset")

def handleKeyPress(key):
    print(key)
    if (globals.ALARM_SEQUENCE_STARTED):
        if (key == "#"):
            if (globals.PASSWORD == globals.VALID_PASSWORD):
	        resetAlarm()
	        globals.SYSTEM_ARMED = False
	        print("SYSTEM DISARMED!!")
	    else:	
	        print("INVALID PASSWORD!!")
	        globals.PASSWORD = ""
        else:
	    globals.PASSWORD += key
