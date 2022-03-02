#Animation1 - Created by Carlos Huallpa - M00763709 - 2nd Year Robotics and Mecahtronics

import opc                                              #Import Open Pixel Control
import time                                             #Import time access and conversions 
import random                                           #Import and generate pseudo-random numbers 

def A1():                                               #DEF - keyword for defining a function
    
    ##A. Set up - White
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    leds =[(255,255,255)]*360                           #Simulator color [R,G,B] * numbers of leds working - WHITE

    client = opc.Client('localhost:7890')               #Use the Simulator_Fadecandy
    client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
    client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's

    time.sleep(1)                                       #Number in seconds - 1s


    ##B. Left to right (Cortain - Red)
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    led=0                                               #Assignment of the LED equal to 0
    for led in range(60):                               #For loop in range(X)
        leds[led] = (255,0,0)                           #Position of the LED - assignment - Simulator color [R,G,B] - RED
        leds[led+60] = (255,0,0)                        #Position of the LED - assignment - Simulator color [R,G,B] - RED
        leds[led+120] = (255,0,0)                       #Position of the LED - assignment - Simulator color [R,G,B] - RED
        leds[led+180] = (255,0,0)                       #Position of the LED - assignment - Simulator color [R,G,B] - RED
        leds[led+180+60] = (255,0,0)                    #Position of the LED - assignment - Simulator color [R,G,B] - RED
        leds[led+120+180] = (255,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - RED
        time.sleep (0.02)                               #Number in seconds - 1s
        client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's


    ##C. Doble movement (Light blue and Green)
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    led = 0                                             #Assignment of the LED equal to 0
    while led<60:                                       #While function
        for rows in range(3):                           #For loop in range(X) - (1 to 3) lines from left to right
            leds[led + rows*60] = (51,255,255)          #Position of the LED and rows - assignment - Simulator color [R,G,B] - LIGHT BLUE
        for rows in range(3,6):                         #For loop in range(X) - (1 to 3) lines from right to left
            leds[59-led + rows*60] = (0,255,0)          #Position of the LED and rows - assignment - Simulator color [R,G,B] - GREEN
        client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
        time.sleep(.01)                                 #Number in seconds - 0.1s
        led = led + 1                                   #Count +1to the last number of led

    leds =[(0,0,0)]*360                                 #Simulator color [R,G,B] * numbers of leds working - White

    client = opc.Client('localhost:7890')               #Use the Simulator_Fadecandy
    client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
    client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's


    ##D. Movement of Watt from right to left covering the whole horitzontal leds (Range 54)
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Character 1 Watt~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    led = 0                                             #Assignment of the LED equal to 0
    while led<60:                                       #While function                 
        for led in range(54):                           #For loop in range(X)   
            leds = [(0,0,255)]*360                      #Whole simulator Blue R,G,B (0,0,0) - BLUE
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~Feet(Black -(0,0,0))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            leds[351-led+2] = (0,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
            leds[351-led+3] = (0,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
            leds[351-led+4] = (0,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - BLACK

            leds[351-led+6] = (0,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
            leds[351-led+7] = (0,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
            leds[351-led+8] = (0,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~Outside(Orange -(255,128,0))~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            leds[290-led+5] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            leds[290-led+6] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            leds[290-led+7] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE

            leds[230-led+4] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            leds[230-led+8] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            
            leds[170-led+3] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            leds[170-led+9] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE

            leds[110-led+4] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            leds[110-led+8] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE

            leds[50-led+5] = (255,128,0)                #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            leds[50-led+6] = (255,128,0)                #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            leds[50-led+7] = (255,128,0)                #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Inside(Orange (255,128,0))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            
            leds[110-led+6] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            
            leds[170-led+4] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            leds[170-led+5] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            leds[170-led+6] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            leds[170-led+7] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            leds[170-led+8] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Mouth(Red -(255,0,0))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

            leds[230-led+5] = (255,0,0)                 #Position of the LED - assignment - Simulator color [R,G,B] - RED
            leds[230-led+6] = (255,0,0)                 #Position of the LED - assignment - Simulator color [R,G,B] - RED
            leds[230-led+7] = (255,0,0)                 #Position of the LED - assignment - Simulator color [R,G,B] - RED
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~Eyes(Yellow (255,255,102))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            leds[110-led+5] = (255,255,102)             #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
            leds[110-led+7] = (255,255,102)             #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
            
            client.put_pixels(leds)                     #Use the Simulator_Fadecandy - LED's
            time.sleep(.1)                              #Number in seconds - 0.1s
        break                                           #The break statement in Python terminates the current loop and resumes execution at the next statement


    ##E. Left to right (Black Swipe )
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    led=0                                               #Assignment of the LED equal to 0
    for led in range(60):                               #For loop in range(X)
        leds[led] = (0,0,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
        leds[led+60] = (0,0,0)                          #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
        leds[led+120] = (0,0,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
        leds[led+180] = (0,0,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
        leds[led+180+60] = (0,0,0)                      #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
        leds[led+120+180] = (0,0,0)                     #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
        time.sleep (0.02)                               #Number in seconds - 0.2s
        client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
    return                                              #The return statement determines the value to be returned.


A1 ()                                                   #Work def A1



