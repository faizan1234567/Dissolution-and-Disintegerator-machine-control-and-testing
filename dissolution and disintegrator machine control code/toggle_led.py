from gpiozero import LED
from gpiozero import Button
import time

led = LED(18)

led.on()
time.sleep(3)
led.off()