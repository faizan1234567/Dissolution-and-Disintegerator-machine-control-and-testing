import time

from w1thermsensor import w1ThermSensor

sensor = W1ThermSensor()

while True:
    temp = sensor.get_temperature()
    print('Temperature = %0.1f celcius' %temp)
    time.sleep(0.1)