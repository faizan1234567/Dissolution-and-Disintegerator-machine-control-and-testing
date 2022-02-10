import RPi.GPIO as GPIO
import time
from time import sleep
from threading import Thread

class speed_monitor:     # monitor the speed of motor and print it out every 1 second
    counter = 0          # current count values
    previous_count = 0   #previous count values
#     pin_A = 18         # encoder pin 
#     PPR = 500          # encoder pulse per revolution
#     in1 =16            # motor direction outuput1
#     in2 =20            #motor direction output2
#     en =21             #speed control pin
    def __init__(self, encoder_pin, speed_pin, direction_pin1, direction_pin2, PPR):
        self.encoder_pin = encoder_pin
        self.speed_pin = speed_pin
        self.direction_pin1 = direction_pin1
        self.direction_pin2 = direction_pin2
        self.PPR = PPR
        GPIO.setmode(GPIO.BCM) 
        #self.p = GPIO.PWM(self.speed_pin, 1000)
    
    #def setup(self):
        #GPIO.setmode(GPIO.BCM) # raspberry pi in the BCM mode
        GPIO.setwarnings(False)
        GPIO.setup(self.direction_pin1, GPIO.OUT)
        GPIO.setup(self.direction_pin2, GPIO.OUT)
        GPIO.setup(self.speed_pin, GPIO.OUT)
        GPIO.output(self.direction_pin1, GPIO.LOW)
        GPIO.output(self.direction_pin2, GPIO.LOW)
        self.p = GPIO.PWM(self.speed_pin, 1000)
        #p = GPIO.PWM(self.speed_pin, 1000)
        self.p.start(25)
        GPIO.setup(self.encoder_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        
    def frequency(self):
#         global counter, previous_count
        print('RPM: {} '.format(((self.counter - self.previous_count)*60)/self.PPR))
        self.previous_count = self.counter
        
    def detect_pulse(self):
        GPIO.add_event_detect(self.encoder_pin, GPIO.RISING, callback=self.edge_detection)
    
    def edge_detection(self,ev=None):
        #global counter
        self.counter+=1
    def encoder_reset(self):
    #global counter
        self.counter=0
    def call_second(self):
    #global in1, in2
        while True:
            self.frequency()
            sleep(1)
    def motor(self):
    #global p
        while True:
            GPIO.output(self.direction_pin1, GPIO.LOW)
            GPIO.output(self.direction_pin2, GPIO.HIGH)
            self.p.ChangeDutyCycle(25)
            sleep(3)
            self.p.ChangeDutyCycle(50)
            sleep(3)
            self.p.ChangeDutyCycle(75)
            sleep(3)
            self.p.ChangeDutyCycle(100)
            sleep(3)
    def main(self): 
        print("A: pin 16")
        print("B: pin 23")
        print('starting encoder')
        print('------------------------------------------')
        #self.setup()
        
        t1 = Thread(target=self.call_second)
        t2 = Thread(target=self.detect_pulse)
        t3 = Thread(target=self.motor)
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
    def kill(self):
        quit()

if __name__ =='__main__':
    try:
        m1 = speed_monitor(18, 21, 16, 20, 500)
        print('starting motor with PWM')
        print('--------------------------')
        m1.main()
        #PIO.cleanup()
    except:
        m1.kill()
        GPIO.cleanup()
        KeyboardInterrupt()

