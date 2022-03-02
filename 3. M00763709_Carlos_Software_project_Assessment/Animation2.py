#Animation2 - Created by Carlos Huallpa - M00763709 - 2nd Year Robotics and Mechatronics

import opc                                              #Import Open Pixel Control
import time                                             #Import time access and conversions 
import random                                           #Import and generate pseudo-random numbers 

def A2():                                               #DEF - keyword for defining a function

    ##A. Set up - Yellow
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
    leds =[(250,250,0)]*360                             #Simulator color [R,G,B] * numbers of leds working - YELLOW
    
    client = opc.Client('localhost:7890')               #Use the Simulator_Fadecandy
    client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
    client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
    time.sleep(1)                                       #Number in seconds - 1s
    
    
    ##B. Spanish Flag
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    led = 0                                             #Assignment of the LED equal to 0
    while led<60:                                       #While function
        for rows in range(2):                           #For loop rows in range(X) - (1 to 2) lines from left to right
            leds[led + rows*60] = (255,0,0)             #Position of the LED and rows - assignment - Simulator color [R,G,B] - RED
            
        for rows in range(4,6):                         #For loop in range(X) - (4 to 6) lines from right to left
            leds[59-led + rows*60] = (255,0,0)          #Position of the LED and rows - assignment - Simulator color [R,G,B] - RED
        client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
        time.sleep(.05)                                 #Number in seconds - 0.5 s
        led = led + 1                                   #Count +1 to the last number of led


    ##C. Show the character 2 Thwomp (Wall)
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



    led = 0                                             #Assignment of the LED equal to 0
    leds = [(0,0,255)]*360                              #Simulator color [R,G,B] * numbers of leds working - BLUE
    time.sleep(1)                                       #Number in seconds - 1 s

    #~~~~~~~~~~~~~~~~~~~~~~~Body(Grey -(160,160,160))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    
    #First line
    leds[0-led] = (160,160,160)                         #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[0-led+1] = (160,160,160)                       #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[0-led+3] = (160,160,160)                       #Position of the LED - assignment - Simulator color [R,G,B] - SILVER

    leds[0-led+5] = (160,160,160)                       #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[0-led+7] = (160,160,160)                       #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[0-led+8] = (160,160,160)                       #Position of the LED - assignment - Simulator color [R,G,B] - SILVER

    #Second Line
    leds[60-led] = (160,160,160)                        #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[60-led+1] = (160,160,160)                      #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[60-led+2] = (255,255,102)                      #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
    leds[60-led+3] = (255,255,102)                      #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
    leds[60-led+4] = (160,160,160)                      #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[60-led+5] = (255,255,102)                      #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
    leds[60-led+6] = (255,255,102)                      #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
    leds[60-led+7] = (160,160,160)                      #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[60-led+8] = (160,160,160)                      #Position of the LED - assignment - Simulator color [R,G,B] - SILVER

    #Third line
    leds[120-led+1] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[120-led+2] = (255,255,102)                     #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
    leds[120-led+3] = (255,255,102)                     #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
    leds[120-led+4] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[120-led+5] = (255,255,102)                     #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
    leds[120-led+6] = (255,255,102)                     #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
    leds[120-led+7] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER

    #Fourth Line
    leds[180-led] = (160,160,160)                       #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[180-led+1] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[180-led+2] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[180-led+3] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[180-led+4] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[180-led+5] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[180-led+6] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[180-led+7] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[180-led+8] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER

    #Five Line
    leds[240-led+1] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[240-led+2] = (255,0,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - RED
    leds[240-led+3] = (255,0,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - RED
    leds[240-led+4] = (255,0,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - RED
    leds[240-led+5] = (255,0,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - RED
    leds[240-led+6] = (255,0,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - RED
    leds[240-led+7] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER

    #Sixth Line
    leds[300-led] = (160,160,160)                       #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[300-led+2] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[300-led+4] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[300-led+6] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER
    leds[300-led+8] = (160,160,160)                     #Position of the LED - assignment - Simulator color [R,G,B] - SILVER

    client.put_pixels(leds)
    time.sleep(5)

    ##D. Left AND right (Black Swipe ) TO MIDDLE UNTIL LED NUMBER 30
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    led = 0                                             #Assignment of the LED equal to 0
    while led<30:                                       #While function (Close until 30)
        for rows in range(6):                           #For loop in range(X) ROWS - (1 to 6) outside to inside
            leds[led + rows*60] = (0,0,0)               #Position of the LED and rows - assignment - Simulator color [R,G,B] - BLACK
            leds[59-led + rows*60] = (0,0,0)            #Position of the LED and rows - assignment - Simulator color [R,G,B] - BLACK
        client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
        time.sleep(.02)                                 #Number in seconds - 0.2s
        led = led + 1                                   #Count +1 to the last number of led
        
    return                                              #The return statement determines the value to be returned.

A2()                                                    #Function def A1

