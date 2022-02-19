#Animation1

import opc
import time
import random

leds =[(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

##1. left to right
##def Ani1():
led=0
for led in range(60):
    leds[led] = (255,0,0)
    leds[led+60] = (255,0,0)
    leds[led+120] = (255,0,0)
    leds[led+180] = (255,0,0)
    leds[led+180+60] = (255,0,0)
    leds[led+120+180] = (255,0,0)
    time.sleep (0.05)
    client.put_pixels(leds)
