import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#RELAY 1
GPIO.setup(18, GPIO.OUT)

GPIO.setup(23, GPIO.OUT)


try:
    while True:
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        print('Relay 1 is activated')
        time.sleep(1)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        print('Relay 2 is activated')
        time.sleep(1)
#         print('Relay 1 is activated')
#         time.sleep(1)
#         GPIO.output(18, GPIO.LOW)
#         GPIO.output(23, GPIO.HIGH)
#         print('Relay 2 is activated')
#         time.sleep(1)
#         GPIO.output(18, GPIO.LOW)
#         print('Relay 1 is de-activated')
#         time.sleep(1)
#         GPIO.output(23, GPIO.LOW)
#         print('Relay 2 is de-activated')
#         time.sleep(1)
finally:
    GPIO.cleanup()
    
        