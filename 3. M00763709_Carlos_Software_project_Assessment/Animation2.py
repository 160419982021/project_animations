#Animation2


import opc
import time
import random

leds =[(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#2.(rigth to left)
led = 0
while led<60:
    leds[59-led] = (0,255,0)
    leds[119-led] = (0,255,0)
    leds[179-led] = (0,255,0)
    leds[239-led] = (0,255,0)
    leds[299-led] = (0,255,0)
    leds[359-led] = (0,255,0)

    time.sleep(.05)
    client.put_pixels(leds)
    led = led + 1
