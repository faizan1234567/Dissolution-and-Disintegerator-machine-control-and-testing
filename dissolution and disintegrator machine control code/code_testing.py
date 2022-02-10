import os
def sensor():
    
   for i in os.listdir('/sys/bus/w1/devices'):
       #print(i)
       if i != 'w1_bus_master1':
          ds18b20 = i
          #print(i)
   return ds18b20

print(sensor())

file = '/sys/bus/w1/devices/' + sensor() + '/w1_slave'
tfile = open(file)
print(tfile)
text = tfile.read()
print(text)
tfile.close()
secondline = text.split("\n")[1]
print(secondline)
temperaturedata = secondline.split(" ")[9]
print(temperaturedata)
temperature = float(temperaturedata[2:])
print(temperature)
celsius = temperature / 1000
print(celsius)