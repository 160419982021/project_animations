#Position  of the led in the game World and Characters

import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


#~~~~~~~~~~~~~~~~~~~~~~~Character 1 Watt~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Movement of Watt from right to left covering the whole horitzontal leds (Range 54)
led = 0
while led<60:                 
    for led in range(54):   
        leds = [(0,0,255)]*360 #Whole simulator Blue R,G,B (0,0,0)
        #~~~~~~~~~~~~~~~~~~~~~~~Feet(Black -(0,0,0))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        leds[351-led+2] = (0,0,0)
        leds[351-led+3] = (0,0,0)
        leds[351-led+4] = (0,0,0)

        leds[351-led+6] = (0,0,0)
        leds[351-led+7] = (0,0,0)
        leds[351-led+8] = (0,0,0)
        #~~~~~~~~~~~~~~~~~~~~~~~Outside(Orange -(255,128,0))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        leds[290-led+5] = (255,128,0)
        leds[290-led+6] = (255,128,0)
        leds[290-led+7] = (255,128,0)

        leds[230-led+4] = (255,128,0)
        leds[230-led+8] = (255,128,0)
        
        leds[170-led+3] = (255,128,0)
        leds[170-led+9] = (255,128,0)

        leds[110-led+4] = (255,128,0)
        leds[110-led+8] = (255,128,0)

        leds[50-led+5] = (255,128,0)
        leds[50-led+6] = (255,128,0)
        leds[50-led+7] = (255,128,0)

        #~~~~~~~~~~~~~~~~~~~~~~~Inside(Orange (255,128,0))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        leds[110-led+6] = (255,128,0)
        
        leds[170-led+4] = (255,128,0)
        leds[170-led+5] = (255,128,0)
        leds[170-led+6] = (255,128,0)
        leds[170-led+7] = (255,128,0)
        leds[170-led+8] = (255,128,0)#

        #~~~~~~~~~~~~~~~~~~~~~~~Mouth(Red -(255,0,0))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        leds[230-led+5] = (255,0,0)
        leds[230-led+6] = (255,0,0)
        leds[230-led+7] = (255,0,0)
        #~~~~~~~~~~~~~~~~~~~~~~~Eyes(Yellow (255,255,102))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        leds[110-led+5] = (255,255,102)
        leds[110-led+7] = (255,255,102)
        
        client.put_pixels(leds)
        time.sleep(.5)
    break
