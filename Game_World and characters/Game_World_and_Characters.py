#Position  of the led in the game World and Characters

import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


#~~~~~~~~~~~~~~~~~~~~~~~Character 1 Watt~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,255)]*360 #Whole simulator black R,G,B (0,0,0)
        #~~~~~~~~~~~~~~~~~~~~~~~Feet(Black)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        leds[351-led+2] = (0,0,0)
        leds[351-led+3] = (0,0,0)
        leds[351-led+4] = (0,0,0)

        leds[351-led+6] = (0,0,0)
        leds[351-led+7] = (0,0,0)
        leds[351-led+8] = (0,0,0)
        

        
        client.put_pixels(leds)
        time.sleep(.5)
    break
