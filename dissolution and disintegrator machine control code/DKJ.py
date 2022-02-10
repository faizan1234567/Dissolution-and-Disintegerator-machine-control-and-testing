import RPi.GPIO as GPIO
from time import sleep
from threading import Thread
import multiprocessing as mp
import ds18b20_temp_sensor

led1 = 3
led2 = 18
button= 11
counter = 0
Led = True
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)
    GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    
def control_LED1():
    global counter
    global Led
    Led = not Led 
    if Led:
        
        GPIO.output(led1, GPIO.HIGH)
        counter+=1
        #print('Counter: {}'.format(counter))
    else:
       
       GPIO.output(led1, GPIO.LOW)
       
#     
# def control_LED2():
#    while True:
#        GPIO.output(led2, GPIO.HIGH)
#        sleep(2)
#        GPIO.output(led2,GPIO.LOW)
#        sleep(2)
        

def detect_button():
    GPIO.remove_event_detect(button)
    GPIO.add_event_detect(button, GPIO.RISING, callback=lambda x:control_LED1(),bouncetime=200)
def printing():
    while True:
        sleep(2)
        print('This is using multi-threading')
    
if __name__ == '__main__':
    setup()
    
    #GPIO.add_event_detect(button, GPIO.RISING, callback=lambda x:control_LED2(),bouncetime=200)

    p1 = Thread(target = control_LED2)
    p2 = Thread(target = detect_button)
    p3 = Thread(target = printing)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    GPIO.cleanup()
    quit()