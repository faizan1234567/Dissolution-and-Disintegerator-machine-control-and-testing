import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
channel = 11

counter =0
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def mycounter():
    global counter
    input_state = GPIO.input(channel)
    #print(input_state)
    if input_state == True:
        print('button is pressed')
        counter+=1
        print('counter value: {}'.format(counter))
GPIO.remove_event_detect(channel)
GPIO.add_event_detect(channel, GPIO.RISING, callback=lambda x:mycounter(),bouncetime=200)