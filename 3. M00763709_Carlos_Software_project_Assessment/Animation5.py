#Animation5

#Position  of the led in the game World and Characters


#Website to change and modify colors (https://www.rapidtables.com/web/color/RGB_Color.html)


import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)



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
        leds[230-led-2] = (255,0,0)
        leds[230-led-1] = (255,0,0)
        leds[230-led] = (255,0,0)
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
        time.sleep(.08)
    break
