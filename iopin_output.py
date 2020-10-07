from time import sleep

from gpiozero import LED

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
