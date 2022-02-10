import RPi.GPIO as GPIO
from time import sleep
import  time



    
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

input_A = 18
input_B = 23

GPIO.setup(input_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(input_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter=0
#counterB =0

def myA():
    global counter
    input_state1 = GPIO.input(input_A)
    input_state2 = GPIO.input(input_B)
    #print(input_state)
    if input_state1 == True:
        counter+=1
    elif input_state2 == True:
        counter+=1
    print('counter value: {}'.format(counter))
    previous_count = counter
    
# def myB():
#     global counterB
#     input_state = GPIO.input(input_B)
#     #print(input_state)
#     if input_state == True:
#         counterB+=1
        #print('counter value: {}'.format(counter))
def detect_pulses():
    GPIO.remove_event_detect(input_A)
    GPIO.remove_event_detect(input_B)
    GPIO.add_event_detect(input_A, GPIO.RISING, callback=lambda x:myA())
    GPIO.add_event_detect(input_B, GPIO.RISING, callback=lambda x:myA())
    
    
if __name__ == '__main__':
    
    counter = 0
    print('starting counter')          
    print('--------------------------------------------------------------------------------------------------------------------------')
    detect_pulses()
    
    
        
    
    
    
    
    
    
    
