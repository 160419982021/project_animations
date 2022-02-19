#Animation4
import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


#3. (Swipe left to right) para hacer todo de un color pero todas las filas a la vez 
led = 0
while led<60:
    for rows in range(6):
        leds[led + rows*60] = (0,0,255)
    client.put_pixels(leds)
    time.sleep(.02)
    led = led + 1

#Point by point until last one 
p = 0
print (enumerate(leds))
while True:
    Ghost = [89,90,91,148,150,152,207,208,209,210,211,212,213,268,272,329,330,331]
    leds[Ghost[p]] = (255,255,255)
    client.put_pixels(leds)
    time.sleep(0.1)
    p = p + 1
    if p == 18:
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

time.sleep(5) # Enough time to be able to see the gosh (Goof Ball)

#6. serpiente que recorre todo el panel de leds from 0 to 360(left to right always)
led = 0
while True:                
    for led in range(355): 
        leds = [(192,192,192)]*360    
        leds[led+0] = (0,0,255)         
        leds[led+1] = (0,0,255)
        leds[led+2] = (0,0,255)
        leds[led+3] = (0,0,255)
        leds[led+4] = (0,0,255)
        leds[led+5] = (0,254,255)# Head of the snake

        if led == 255:                              led = 0
        client.put_pixels(leds)
        time.sleep(.02)
    break

#3. (Swipe left to right) para hacer todo de un color pero todas las filas a la vez 
led = 0
while led<60:
    for rows in range(6):
        leds[led + rows*60] = (0,100,255)
    client.put_pixels(leds)
    time.sleep(.02)
    led = led + 1
