import os
import RPi.GPIO as GPIO
import time
# from gpio import LED
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# led = 21
# GPIO.setup(led, GPIO.OUT)

def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20
def read(ds18b20):
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit
def loop(ds18b20):
    while True:
        if read(ds18b20) != None:
            print ("Current temperature : %0.3f C" % read(ds18b20)[0])
            return read(ds18b20)[0]
    return 'done'
#             if read(ds18b20)[0] >= 25:
#                 GPIO.output(led, GPIO.HIGH)
#                 #print 'temperature has exceeded 25C'
#             else:
#                 GPIO.output(led, GPIO.LOW)
                #print 'temperature is below 25C'
                
            
            #print "Current temperature : %0.3f F" % read(ds18b20)[1]
def kill():
    quit()
if __name__ == '__main__':
    try:
        serialNum = sensor()
        print(loop(serialNum))
    except KeyboardInterrupt:
        kill()
    