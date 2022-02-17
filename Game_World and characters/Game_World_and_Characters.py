#Position  of the led in the game World and Characters


#Website to change and modify colors (https://www.rapidtables.com/web/color/RGB_Color.html)


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
        time.sleep(.1)
    break


#~~~~~~~~~~~~~~~~~~~~~~~Character 2 Thwomp (Wall)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Only position of Thwomp (Wall)
led = 60
while led<60:                 
    for led in range(-54):
    
        led = 0
        leds = [(0,0,255)]*360 #Whole simulator White R,G,B (x,x,x)
                #~~~~~~~~~~~~~~~~~~~~~~~Body(Grey -(160,160,160))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        time.sleep(1)
        #First line
        leds[0+led] = (160,160,160)
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
        time.sleep(1)
    break

#~~~~~~~~~~~~~~~~~~~~~~~Character 3 The Grump (Mushroom)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Moving from right to left
led = 0
while led<60:                 
    for led in range(54-7):
            
        leds = [(225,225,225)]*360 #Whole simulator White R,G,B (x,x,x)

            #First line (Empty)

            #Second Line
        leds[110-led-2] = (204,102,0)
        leds[110-led-1] = (204,102,0)
        leds[110-led-0] = (204,102,0)

        #Third line
        leds[170-led-3] = (204,102,0)
        leds[170-led-2] = (255,255,102)#Yellow
        leds[170-led-1] = (204,102,0)
        leds[170-led-0] = (255,255,102)#Yellow
        leds[170-led+1] = (204,102,0)

        #Fourth Line
        leds[230-led-4] = (204,102,0)
        leds[230-led-3] = (204,102,0)
        leds[230-led-2] = (204,102,0)
        leds[230-led-1] = (255,0,0)
        leds[230-led] = (204,102,0)
        leds[230-led+1] = (204,102,0)
        leds[230-led+2] = (204,102,0)

        #Five Line
        leds[290-led-2] = (255,128,0)
        leds[290-led-1] = (255,128,0)
        leds[290-led] = (255,128,0)

        #Sixth Line
        leds[350-led-4] = (102,51,0)
        leds[350-led-3] = (102,51,0)

        leds[350-led+1] = (102,51,0)
        leds[350-led+2] = (102,51,0)

        client.put_pixels(leds)
        time.sleep(.5)
    break


#~~~~~~~~~~~~~~~~~~~~~~~Character 4 Goof Ball (Gosh)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

led = 0
while led<60:                 
    for led in range(1):# Number of position who we can control moving to the left
            
        leds = [(0,0,0)]*360 #Whole simulator Black R,G,B (x,x,x)

            #First line (Empty)

        #Second Line
        leds[90-led-1] = (255,255,255)
        leds[90-led] = (255,255,255)
        leds[90-led+1] = (255,255,255)

        #Third line
        leds[150-led-2] = (255,255,255)
        leds[150-led-1] = (255,255,102)#Yellow
        leds[150-led] = (255,255,255)
        leds[150-led+1] = (255,255,102)#Yellow
        leds[150-led+2] = (255,255,255)

        #Fourth Line
        leds[210-led-3] = (255,255,255)
        leds[210-led-2] = (255,255,255)
        leds[210-led-1] = (255,255,255)
        leds[210-led] = (255,255,255)
        leds[210-led+1] = (255,255,255)
        leds[210-led+2] = (255,255,255)
        leds[210-led+3] = (255,255,255)

        #Five Line# 
       
        leds[270-led-2] = (255,255,255)
        leds[270-led-1] = (255,0,0)#rojo
        leds[270-led] = (255,0,0)
        leds[270-led+1] = (255,0,0)
        leds[270-led+2] = (255,255,255)

        #Sixth Line#
        leds[330-led-1] = (255,255,255)
        leds[330-led] = (255,255,255)
        leds[330-led+1] = (255,255,255)

        client.put_pixels(leds)
        time.sleep(.5)
    break

#~~~~~~~~~~~~~~~~~~~~~~~Character 5 The Grump: Angel wings~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


#Moving from right to left
led = 0
while led<60:                 
    for led in range(42):
            
        leds = [(0,0,0)]*360 #Whole simulator White R,G,B (x,x,x)

            #First line (Empty)

            #Second Line
        leds[110-led-9] = (255,255,255)# White Wings
        leds[110-led-8] = (255,255,255)# White Wings
        leds[110-led-7] = (255,255,255)# White Wings
        leds[110-led-6] = (255,255,255)# White Wings
        leds[110-led-5] = (255,255,255)# White Wings
        leds[110-led-4] = (255,255,255)# White Wings
        leds[110-led-3] = (255,255,255)# White Wings
        leds[110-led-2] = (204,102,0)#Brown
        leds[110-led-1] = (204,102,0)#Brown
        leds[110-led-0] = (204,102,0)#Brown
        leds[110-led+1] = (255,255,255)# White Wings
        leds[110-led+2] = (255,255,255)# White Wings
        leds[110-led+3] = (255,255,255)# White Wings
        leds[110-led+4] = (255,255,255)# White Wings
        leds[110-led+5] = (255,255,255)# White Wings
        leds[110-led+6] = (255,255,255)# White Wings



        #Third line
        leds[170-led-6] = (255,255,255)# White Wings
        leds[170-led-5] = (255,255,255)# White Wings
        leds[170-led-4] = (255,255,255)# White Wings
        leds[170-led-3] = (204,102,0)
        leds[170-led-2] = (255,255,102)#Yellow
        leds[170-led-1] = (204,102,0)
        leds[170-led-0] = (255,255,102)#Yellow
        leds[170-led+1] = (204,102,0)
        leds[170-led+2] = (255,255,255)# White Wings
        leds[170-led+3] = (255,255,255)# White Wings
        leds[170-led+4] = (255,255,255)# White Wings

        #Fourth Line
        
        leds[230-led-5] = (255,255,255)# White Wings
        leds[230-led-4] = (204,102,0)
        leds[230-led-3] = (204,102,0)
        leds[230-led-2] = (204,102,0)
        leds[230-led-1] = (255,0,0)
        leds[230-led] = (204,102,0)
        leds[230-led+1] = (204,102,0)
        leds[230-led+2] = (204,102,0)
        leds[230-led+3] = (255,255,255) # White Wings
        
        
        #Five Line
        leds[290-led-2] = (255,128,0)
        leds[290-led-1] = (255,128,0)
        leds[290-led] = (255,128,0)

        #Sixth Line
        leds[350-led-4] = (102,51,0)
        leds[350-led-3] = (102,51,0)

        leds[350-led+1] = (102,51,0)
        leds[350-led+2] = (102,51,0)

        client.put_pixels(leds)
        time.sleep(.5)
    break

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
