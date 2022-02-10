import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(23, GPIO.OUT)

#LED is connected to Pin 17

GPIO.setup(24, GPIO.IN) 

#PushButton is connected to Pin 18

try:

    while True:

        if GPIO.input (24) == 0:

            print ("led is On")

            GPIO.output (23, True)

        if GPIO.input (24) == 1:

            print ("led is OFF")

            GPIO.output (23, False)

finally:

        GPIO.cleanup ()
