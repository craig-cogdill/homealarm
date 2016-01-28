# Create our global variables
VALID_PASSWORD="123ABC"
START_TIME=""
PASSWORD=""
#SYSTEM_ARMED=False
SYSTEM_ARMED=True
ALARM_TRIGGERED=False
ALARM_TIMEOUT=15 # seconds
ALARM_SEQUENCE_STARTED = False

# Declare I/O Pins
DOOR_SENSOR_PIN = 21
ALARM_PIN = 23
COL_PINS = [4, 17, 27, 22]
ROW_PINS = [6, 13, 19, 26]

# Declare the keypad
KEYPAD = [
	     ["1", "2", "3", "A"],
 	     ["4", "5", "6", "B"],
 	     ["7", "8", "9", "C"],
	     ["*", "0", "#", "D"]
         ]

