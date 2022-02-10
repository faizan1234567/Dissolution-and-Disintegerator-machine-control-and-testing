import DHT
import pigpio
import sys
from threading import Thread
from time import sleep
pi = pigpio.pi()
argc = len(sys.argv)
if argc < 2:
    print("Need to specify at least one GPIO")
    exit()
if not pi.connected:
      exit()
      
g = int(sys.argv[i])
S = []
for i in range(1, argc): # ignore first argument which is command name
  g = int(sys.argv[i])
  if (g >= 100):
     s = DHT.sensor(pi, g-100, callback=callback)
  else:
     s = DHT.sensor(pi, g)
  S.append((g,s)) # store GPIO and class
print(s._datum())


value = DHT.sensor(pi,g-100)
value._datum()