#/usr/bin/env python
import httplib, urllib
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from pad4pi import rpi_gpio
import time
import logging
from post import stallPost
from keypadAlarm import triggerAlarm
from keypadAlarm import resetAlarm
from keypadAlarm import handleKeyPress
import globals

# Setup door input and alarm output
GPIO.setup(globals.DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(globals.ALARM_PIN, GPIO.OUT)

# Initialize the Alarm Pin
GPIO.output(globals.ALARM_PIN, GPIO.LOW)

# Setup the keypad
keypadFactory = rpi_gpio.KeypadFactory()
keypad = keypadFactory.create_keypad(keypad  =globals.KEYPAD,
				     row_pins=globals.ROW_PINS,
                                     col_pins=globals.COL_PINS)
keypad.registerKeyPressHandler(handleKeyPress)


# Alarm is armed
def handleArmedDoorBreach():
    print("You have %d seconds to input a key..." %globals.ALARM_TIMEOUT)
    globals.START_TIME = time.time()
    # wait for 15 seconds
    while (time.time() - globals.START_TIME < globals.ALARM_TIMEOUT and globals.ALARM_SEQUENCE_STARTED):
        None    
    if (globals.ALARM_SEQUENCE_STARTED):
        triggerAlarm()

# Door Sensor handler (effectively main)
def doorSensorChange(self):
    print("SYSTEM_ARMED = ", globals.SYSTEM_ARMED)
    if ( GPIO.input(globals.DOOR_SENSOR_PIN) ):
        print("Front door closed.")
        #stallPost(1, True, False)
    else:
        print("Front door opened.")
        #stallPost(1, False, False)
	if (globals.SYSTEM_ARMED):
            globals.ALARM_SEQUENCE_STARTED = True
            handleArmedDoorBreach()

# Add event detections
GPIO.add_event_detect(globals.DOOR_SENSOR_PIN, GPIO.BOTH, callback=doorSensorChange)


try: 
    while True:
        time.sleep(10);

except KeyboardInterrupt:
    GPIO.cleanup()

keypad.cleanup()
GPIO.cleanup()




# some algorithms I might need later
# while (ALARM_TRIGGERED == False and SYSTEM_ARMED == True):
#     TIME_NOW = time.time()
#     if (TIME_NOW - START_TIME >= ALARM_TIMEOUT):
#         triggerAlarm()
