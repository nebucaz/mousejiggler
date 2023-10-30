import time
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)
time.sleep(1)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

i = 0

while True:
    led.value = True
    distance =  10 if i < 2 else -10

    if i % 2 == 0:
        mouse.move(x=distance)
    else:
        mouse.move(y=distance)

    i = i + 1 if i < 3 else 0

    time.sleep(0.25)
    led.value = False
    time.sleep(10)