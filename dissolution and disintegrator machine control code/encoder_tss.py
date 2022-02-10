import RPi.GPIO as GPIO
import time
from time import sleep
from threading import Thread
counter = 0
previous_count=0
pin_A = 18
PPR = 500
#pin_B = 23
in1 =16
in2 =20
en =21

def setup():
    global in1,in2,en,p
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(en, GPIO.OUT)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    p =GPIO.PWM(en, 1000)
    p.start(25)
    
    global pin_A 
    #global pin_B 

    GPIO.setup(pin_A, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    #GPIO.setup(pin_B, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def frequency():
    global counter, previous_count
    print('RPM: {} '.format(((counter - previous_count)*60)/PPR))
    previous_count = counter
    #sleep(1)
    


def edge_detection(ev=None):
    global counter
    counter+=1
    #  Vprint('counter vlaue: {}'.format(counter))

def encoder_reset():
    global counter
    counter=0


def detect_pulse():
    GPIO.add_event_detect(pin_A, GPIO.RISING, callback=edge_detection)
    #GPIO.add_event_detect(pin_B, GPIO.RISING callback=edge_detection)
def call_second():
    global in1, in2
    while True:
        frequency()
        sleep(1)
def motor():
    global p
    while True:
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        p.ChangeDutyCycle(25)
        sleep(3)
        p.ChangeDutyCycle(50)
        sleep(3)
        p.ChangeDutyCycle(75)
        sleep(3)
        p.ChangeDutyCycle(100)
        sleep(3)
        

        #p.start(25)

def main():
    print("A: pin 16")
    print("B: pin 23")
    print('starting encoder')
    print('------------------------------------------')
    setup()
    
    t1 = Thread(target=call_second)
    t2 = Thread(target=detect_pulse)
    t3 = Thread(target=motor)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    
    
if __name__ == '__main__':
    
    
#     f = Thread(target=frequency, args =(1, ))
#     f.start()
#     f.join()
    main()
    
    
    
#     sleep(5)
#     encoder_reset()
    
    GPIO.cleanup()
    #counter = 0
    
    
    
    