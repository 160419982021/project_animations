#!/usr/bin/env python

import opc #connect to the client and publish
import time

led_colour=[(255,0,0)]*10 #The 10 is the n* of the position of the leds using in the simulator and the pixel with the color
time.sleep(1)
client = opc.Client('localhost:7890')

print (enumerate(led_colour))
# SHOWING THIS IN THE PYTHON 3.9.0 SHELL
#(1, (255, 0, 0)) = 1 is the n* of the LED and the three numbers between
#the braquests are the color of that LED

time.sleep(1)

for item in enumerate(led_colour): #Index position, value of the index position
    time.sleep(1)
    print (item)
    if item[0]%2 == 0: # reduce only in the even numbers
        #need to get values out of tuple
        r, g, b = item[1]
        #print('R:', r, 'G:', g, 'B:', b) #[*]
        r = r-12
        g = 255#[*]
        b = 255#[*]


        #create changed tuple (uses some values from old and some new) 
        new_colour =(r,g,b)
        led_colour[item[0]] = new_colour
        #print(new_colour) #[*]
        
    client.put_pixels(led_colour)
    client.put_pixels(led_colour)

client.put_pixels(led_colour)
#need to send it twice if not constantly sending values 
#due to interpolation setting on fadecandy
client.put_pixels(led_colour)
print (led_colour)

