from time import sleep     # Import sleep Library
import RPi.GPIO as GPIO    # Import GPIO Library 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)# Use Physical Pin Numbering Scheme
button1=18                 # Button 1 is connected to physical pin 16
button2=23                 # Button 2 is connected to physical pin 12
LED=24                    # LED 1 is connected to physical pin 22                # LED 2 is connected to physical pin 18
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button1 an input, Activate Pull UP Resistor
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 2 an input, Activate Pull Up Resistor
GPIO.setup(LED,GPIO.OUT) # Make LED 1 an Output  # Make LED 2 an Output
BS1=False                  # Set Flag BS1 to indicate LED is initially off
BS2=False# Set Flag
count = 0
while True:
    if GPIO.input(button1)== 0:
        print('button 1 was pressed')
        if BS1==False:
            GPIO.output(LED, True)
            BS1 = True
            sleep(.5)
        else:
            GPIO.output(LED, False)
            BS1 = False
            sleep(.5)
    elif GPIO.input(button2)== 0 and LED==True:
        count +=1
        print('counter value is' + str(count))
        if count == 5:
            GPIO.output(LED, False)
            count = 0
GPIO.cleanup()
            
            
