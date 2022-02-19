#Animation1

import opc
import time
import random

leds =[(255,255,255)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

##1. left to right (Cortain - Red)
##def Ani1():
led=0
for led in range(60):
    leds[led] = (255,0,0)
    leds[led+60] = (255,0,0)
    leds[led+120] = (255,0,0)
    leds[led+180] = (255,0,0)
    leds[led+180+60] = (255,0,0)
    leds[led+120+180] = (255,0,0)
    time.sleep (0.02)
    client.put_pixels(leds)



# 2. Doble movement
led = 0
while led<60:
    for rows in range(3):
        leds[led + rows*60] = (51,255,255) # Primeras 3 lineas de izquierda a derecha
    for rows in range(3,6):
        leds[59-led + rows*60] = (0,255,0) # Ultimas 3 lineas de derecha a izquierda
    client.put_pixels(leds)
    time.sleep(.01)
    led = led + 1

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#3. #Movement of Watt from right to left covering the whole horitzontal leds (Range 54)

#~~~~~~~~~~~~~~~~~~~~~~~Character 1 Watt~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
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
        time.sleep(.1)
    break


