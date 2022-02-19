#Animation2


import opc
import time
import random

leds =[(64,64,64)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)



#~~~~~~~~~~~~~~~~~~~~~~~Character 2 Thwomp (Wall)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Only position of Thwomp (Wall)
##led = 60
##while led<60:                 
##    for led in range(-54):
##    
led = 0
leds = [(0,0,255)]*360 #Whole simulator White R,G,B (x,x,x)
        #~~~~~~~~~~~~~~~~~~~~~~~Body(Grey -(160,160,160))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

time.sleep(1)
#First line

leds[0+led] = (160,160,160)      #ffsdfsdfdsf
leds[0+led+1] = (160,160,160)
leds[0+led+3] = (160,160,160)

leds[0+led+5] = (160,160,160)
leds[0+led+7] = (160,160,160)
leds[0+led+8] = (160,160,160)

#Second Line
leds[60+led] = (160,160,160)
leds[60+led+1] = (160,160,160)
leds[60+led+2] = (255,255,102)
leds[60+led+3] = (255,255,102)
leds[60+led+4] = (160,160,160)
leds[60+led+5] = (255,255,102)
leds[60+led+6] = (255,255,102)
leds[60+led+7] = (160,160,160)
leds[60+led+8] = (160,160,160)

#Third line
leds[120+led+1] = (160,160,160)
leds[120+led+2] = (255,255,102)#Yellow
leds[120+led+3] = (255,255,102)#Yellow
leds[120+led+4] = (160,160,160)
leds[120+led+5] = (255,255,102)#Yellow
leds[120+led+6] = (255,255,102)#Yellow
leds[120+led+7] = (160,160,160)

#Fourth Line
leds[180+led] = (160,160,160)
leds[180+led+1] = (160,160,160)
leds[180+led+2] = (160,160,160)
leds[180+led+3] = (160,160,160)
leds[180+led+4] = (160,160,160)
leds[180+led+5] = (160,160,160)
leds[180+led+6] = (160,160,160)
leds[180+led+7] = (160,160,160)
leds[180+led+8] = (160,160,160)

#Five Line
leds[240+led+1] = (160,160,160)
leds[240+led+2] = (255,0,0)
leds[240+led+3] = (255,0,0)
leds[240+led+4] = (255,0,0)
leds[240+led+5] = (255,0,0)
leds[240+led+6] = (255,0,0)
leds[240+led+7] = (160,160,160)

#Sixth Line
leds[300+led] = (160,160,160)
leds[300+led+2] = (160,160,160)
leds[300+led+4] = (160,160,160)
leds[300+led+6] = (160,160,160)
leds[300+led+8] = (160,160,160)

client.put_pixels(leds)
time.sleep(0.5)
#break

###2.(rigth to left)
##led = 0
##while led<60:
##    leds[59-led] = (0,255,0)
##    leds[119-led] = (0,255,0)
##    leds[179-led] = (0,255,0)
##    leds[239-led] = (0,255,0)
##    leds[299-led] = (0,255,0)
##    leds[359-led] = (0,255,0)
##
##    time.sleep(.05)
##    client.put_pixels(leds)
##    led = led + 1
