#/usr/bin/env python
import httplib, urllib
import RPi.GPIO as GPIO
import time
import logging
from post import stallPost
GPIO.setmode(GPIO.BCM)

DOOR_SENSOR_PIN = 21



logging.basicConfig(filename='/var/log/FrontDoor.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s')



GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def doorSensorChange(self):
    if GPIO.input(DOOR_SENSOR_PIN):
	logging.info('Front door closed.')
	print('Front door closed.')
	#stallPost(1, True, False)
    else:
	logging.info('Front door opened.')
	print('Front door opened.')
	#stallPost(1, False, False)


GPIO.add_event_detect(DOOR_SENSOR_PIN, GPIO.BOTH, callback=doorSensorChange)

try:

    while True:
        time.sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
