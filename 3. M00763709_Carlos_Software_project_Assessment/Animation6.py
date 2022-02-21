#Animation6

#Website to change and modify colors (https://www.rapidtables.com/web/color/RGB_Color.html)


import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)



#~~~~~~~~~~~~~~~~~~~~~~~Game World 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

##"""
###Moving from right to left
##led = 0
##while led<60:                 
##    for led in range(42):
##"""
led=0      
leds = [(0,0,0)]*360 #Whole simulator White R,G,B (x,x,x)
time.sleep(.1)
##    #First line

leds[0-led+4] = (0,255,0) #green tree
leds[0-led+5] = (0,255,0) #green tree
leds[0-led+6] = (0,255,0) #green tree

leds[10-led+7] = (255,255,102)#Yellow

leds[30-led+8] = (0,255,255) #BLUE LIGHT
leds[30-led+9] = (0,255,255) #BLUE LIGHT
leds[30-led+10] = (0,255,255) #BLUE LIGHT
leds[30-led+11] = (0,255,255) #BLUE LIGHT
##    #Second Line

leds[60-led+3] = (0,255,0) #green tree
leds[60-led+4] = (0,255,0) #green tree
leds[60-led+5] = (0,255,0) #green tree
leds[60-led+6] = (0,255,0) #green tree
leds[60-led+7] = (0,255,0) #green tree

leds[70-led+5] = (255,0,255)# PINK

leds[90-led+9] = (0,255,255) #BLUE LIGHT
leds[90-led+10] = (0,255,255) #BLUE LIGHT

leds[236-120] = (0,255,0)

###Third line
leds[130-led+1] = (255,255,102)#Yellow

leds[130-led+5] = (204,102,0)
leds[130-led+6] = (102,0,0)
leds[130-led+7] = (204,102,0)
leds[130-led+8] = (255,255,102)#Yellow
leds[130-led+9] = (204,102,0)

leds[236-60] = (0,255,0) #green tree

##
###Fourth Line

leds[270-60] = (0,255,0)
leds[230-led-2] = (0,255,0)
leds[230-led-1] = (0,255,0)
leds[230-led] = (0,255,0)
leds[230-led+1] = (0,255,0)

leds[236] = (255,178,102)

#Five Line
leds[240-led+0] = (255,0,0)#RED

leds[247-led-1] = (255,0,255)#PINK

leds[270-led-1] = (0,255,0)
leds[270-led+0] = (0,255,0)
leds[270-led+1] = (0,255,0)#GREEN

leds[290-led-1] = (0,255,0)#GREEN
leds[290-led] = (0,255,0)#GREEN


leds[290-led+6] = (255,128,0)
leds[290-led+7] = (255,128,0)
leds[290-led+8] = (255,128,0)
leds[290-led+9] = (255,128,0)

#Sixth Line
leds[300] = (204,102,0)
leds[301] = (204,102,0)
leds[302] = (204,102,0)
leds[303] = (204,102,0)
leds[304] = (204,102,0)
leds[305] = (204,102,0)
leds[306] = (204,102,0)
leds[307] = (204,102,0)
leds[308] = (204,102,0)
leds[309] = (204,102,0)
leds[310] = (204,102,0)


leds[316] = (204,102,0)#
leds[317] = (204,102,0)
leds[318] = (204,102,0)
leds[319] = (204,102,0)#
leds[320] = (204,102,0)
leds[321] = (204,102,0)
leds[322] = (204,102,0)
leds[323] = (204,102,0)
leds[324] = (204,102,0)
leds[325] = (204,102,0)
leds[326] = (204,102,0)
leds[327] = (204,102,0)
leds[328] = (204,102,0)
leds[329] = (204,102,0)
leds[330] = (204,102,0)
leds[331] = (204,102,0)

leds[338] = (204,102,0)
leds[339] = (204,102,0)
leds[340] = (204,102,0)
leds[341] = (204,102,0)
leds[342] = (204,102,0)
leds[343] = (204,102,0)
leds[344] = (204,102,0)

leds[349] = (204,102,0)
leds[350] = (204,102,0)
leds[351] = (204,102,0)
leds[352] = (204,102,0)
leds[353] = (204,102,0)
leds[354] = (204,102,0)
leds[355] = (204,102,0)
leds[356] = (204,102,0)
leds[357] = (204,102,0)
leds[358] = (204,102,0)
leds[359] = (204,102,0)


client.put_pixels(leds)
time.sleep(.5)
    #break
