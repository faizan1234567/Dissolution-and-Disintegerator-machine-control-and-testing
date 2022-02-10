import RPi.GPIO as GPIO
import time

led_on = False #initally led is off
count = 0      #counter is off


def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW) # led is connected to pin 18
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)# push button is connected to pin 23
#     GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def flashLED(count):
    for i in range(count):
        GPIO.output(3, GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(3, GPIO.LOW)
        time.sleep(.2)


def switch1(ev=None):
    global led_on, count
    led_on = not led_on
    count+=1
    print('The counter value: {}'.format(count))
    #count += 1

#     if led_on == True:
#         #print("Turning on\tcount: " + str(count))
#         GPIO.output(3, GPIO.HIGH)
#     else:
#         #print("Turning off\tcount: " + str(count))
#         GPIO.output(3, GPIO.LOW)
# # 
# def switch2(ev=None):
#     global led_on, count
#     led_on = not led_on
#     count += 1
#     print("count: " + str(count))
#     if count == 10 and led_on:
#         GPIO.output(18, GPIO.LOW)
#         count=0
            

def detectButtonPress():
    GPIO.add_event_detect(11, GPIO.FALLING, callback=switch1, bouncetime=300)
#     GPIO.add_event_detect(24, GPIO.FALLING, callback=switch2, bouncetime=300)
# 
# def waitForEvents():
#     while True:
#         time.sleep(1)


# # # # # MAIN # # # # #

def main():
    print("# # # LED Program # # #")
    print("LED:\tpin 18")
    print("Button 1: pin 23")
    print("Button 2: pin 24")
    
 
    setupGPIO()
    flashLED(5)
    detectButtonPress()

    #waitForEvents()


if __name__ == "__main__":
    main()
