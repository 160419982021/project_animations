#Position  of the led in the game World and Characters

import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Floor~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

led = 0
while led<60:                 
    for led in range(52):   
        leds = [(0,0,0)]*360 #Whole simulator black R,G,B (0,0,0)


        
        client.put_pixels(leds)
        time.sleep(.01)
    break
