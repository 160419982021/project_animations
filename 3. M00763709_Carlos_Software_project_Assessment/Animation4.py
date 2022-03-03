#Animation4 - Created by Carlos Huallpa - M00763709 - 2nd Year Robotics and Mechatronics

import opc                                              #Import Open Pixel Control
import time                                             #Import time access and conversions 
import random                                           #Import and generate pseudo-random numbers 


def A4():                                               #DEF - keyword for defining a function

##A. Assigments
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
    leds =[(0,0,0)]*360                                 #Simulator color [R,G,B] * numbers of leds working - PINK
    led_colour=[(0,0,0)]*360                            #Simulator color [R,G,B] * numbers of leds working - PINK

    white = (255,255,255)                               #Assignment color - Simulator color [R,G,B] - White
    yellow = (255,255,102)                              #Assignment color - Simulator color [R,G,B] - Yellow
    red = (255,0,0)                                     #Assignment color - Simulator color [R,G,B] - Red
    blue = (0,0,255)                                    #Assignment color - Simulator color [R,G,B] - Blue
    light_blue = (0,254,255)                            #Assignment color - Simulator color [R,G,B] - Light Blue

    client = opc.Client('localhost:7890')               #Use the Simulator_Fadecandy
    client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
    client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
    time.sleep(1)                                       #Number in seconds - 1s

##B. Blue Swipe (left to right)
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    led = 0                                             #Assignment of the LED equal to 0
    while led<60:                                       #While function     
        for rows in range(6):                           #For loop in range(X)
            leds[led + rows*60] = blue                  #Position of the LED and rows - assignment - Simulator color [R,G,B] - BLUE
        client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
        time.sleep(.02)                                 #Number in seconds - 0.1s
        led = led + 1                                   #Count +1 to the last number of led


##C. Using a list show the Character 4 Goof Ball (Gosh)
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    p = 0                                               #Assign p equal to 0
    #print (enumerate(leds))
    while True:                                         #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.
        Ghost = [89,90,91,148,150,152,207,208,209,210,211,212,213,268,272,329,330,331] #Make a list of the positions of the Ghost 1 by 1 in order
        leds[Ghost[p]] = (255,255,255)                  #Position of the LED - assignment - Simulator color [R,G,B] - White
        client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
        time.sleep(0.1)                                 #Number in seconds - 1s
        p = p + 1                                       #Count +1 to the last number of p
        if p == 18:                                     #If p is equal to 18 do the code bellow
            break                                       #The break statement in Python terminates the current loop and resumes execution at the next statement

##D. Show the Character 4 Goof Ball (Gosh)
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    led = 0                                             #Assign led equal to 0
    while led<60:                                       #While loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition                 
        for led in range(1):                            #For loop in range(X). Number of position who we can control moving to the left
                
            leds = [(0,0,0)]*360                        #Whole simulator Blue R,G,B (X,X,X) - BLACK

            #First line (Empty)

            #Second Line
            leds[90-led-1] = white                      #Position of the LED - assignment - Simulator color [R,G,B] - White
            leds[90-led] = white                        #Position of the LED - assignment - Simulator color [R,G,B] - White
            leds[90-led+1] = white                      #Position of the LED - assignment - Simulator color [R,G,B] - White

            #Third line
            leds[150-led-2] = white                     #Position of the LED - assignment - Simulator color [R,G,B] - White
            leds[150-led-1] = yellow                    #Position of the LED - assignment - Simulator color [R,G,B] - Yellow
            leds[150-led] = white                       #Position of the LED - assignment - Simulator color [R,G,B] - White
            leds[150-led+1] = yellow                    #Position of the LED - assignment - Simulator color [R,G,B] - Yellow
            leds[150-led+2] = white                     #Position of the LED - assignment - Simulator color [R,G,B] - White

            #Fourth Line
            leds[210-led-3] = white                     #Position of the LED - assignment - Simulator color [R,G,B] - White
            leds[210-led-2] = white                     #Position of the LED - assignment - Simulator color [R,G,B] - White
            leds[210-led-1] = white                     #Position of the LED - assignment - Simulator color [R,G,B] - White
            leds[210-led] = white                       #Position of the LED - assignment - Simulator color [R,G,B] - White
            leds[210-led+1] = white                     #Position of the LED - assignment - Simulator color [R,G,B] - White
            leds[210-led+2] = white                     #Position of the LED - assignment - Simulator color [R,G,B] - White
            leds[210-led+3] = white                     #Position of the LED - assignment - Simulator color [R,G,B] - White

            #Five Line# 
           
            leds[270-led-2] = white                     #Position of the LED - assignment - Simulator color [R,G,B] - White
            leds[270-led-1] = red                       #Position of the LED - assignment - Simulator color [R,G,B] - Red
            leds[270-led] = red                         #Position of the LED - assignment - Simulator color [R,G,B] - Red
            leds[270-led+1] = red                       #Position of the LED - assignment - Simulator color [R,G,B] - Red
            leds[270-led+2] = white                     #Position of the LED - assignment - Simulator color [R,G,B] - White

            #Sixth Line#
            leds[330-led-1] = white                     #Position of the LED - assignment - Simulator color [R,G,B] - White
            leds[330-led] = white                       #Position of the LED - assignment - Simulator color [R,G,B] - White
            leds[330-led+1] = white                     #Position of the LED - assignment - Simulator color [R,G,B] - White


            client.put_pixels(leds)                     #Use the Simulator_Fadecandy - LED's
            time.sleep(.5)                              #Number in seconds - 0.1s

        break                                           #The break statement in Python terminates the current loop and resumes execution at the next statement

    time.sleep(5)                                       #Number in seconds - 0.1s Enough time to be able to see the gosh (Goof Ball)


##E. Snake move from 0 to 360 (left to right always)
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    led = 0                                             #Assignment of the LED equal to 0
    while True:                                         #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.               
        for led in range(355):                          #For loop in range(X) movement of code bellow 
            leds = [(192,192,192)]*360                  #Whole simulator Blue R,G,B (X,X,X) - WHITE LIGHT
            leds[led+0] = blue                          #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[led+1] = blue                          #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[led+2] = blue                          #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[led+3] = blue                          #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[led+4] = blue                          #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[led+5] = light_blue                    #Position of the LED - assignment - Simulator color [R,G,B] - LIGHT BLUE

            if led == 255:                              #When the LED reach/equal to 255 will do the code bellow
                led = 0                                 #Assignment of the LED equal to 0
            client.put_pixels(leds)                     #Use the Simulator_Fadecandy - LED's
            time.sleep(.01)                              #Number in seconds - 0.2s
        
        break                                           #The break statement in Python terminates the current loop and resumes execution at the next statement


##F. BLUE CURTAINS -CLOSING
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    led = 0                                             #Assignment of the LED equal to 0
    while led<60:                                       #While loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition   

        for rows in range (0,2):                        #For loop in range(1 and 2 lines) movement of code bellow - Left to Right         
            led_colour[led+rows*60] = (0,100,255)       #Assign the this lines to the blue color

        for rows in range (2,4):                        #For loop in range(3 and 4 lines) movement of code bellow - Right to Left
            led_colour[59-led+rows*60] = (0,100,255)    #Assign the this lines to the blue color  

        for rows in range (4,6):                        #For loop in range(3 and 4 lines) movement of code bellow - Left to Right                    
            led_colour[led+rows*60] = (0,100,255)       #Assign the this lines to the blue color

        client.put_pixels(led_colour)                   #Use the Simulator_Fadecandy - LED's
        time.sleep(.1)                                  #Number in seconds - 0.1s
        led = led + 1                                   #Increment by +1 to the last number of led

A4()                                                    #Function def A1



        
