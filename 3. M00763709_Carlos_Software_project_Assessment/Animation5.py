#Animation5 - Created by Carlos Huallpa - M00763709 - 2nd Year Robotics and Mechatronics

#Website to change and modify colors (https://www.rapidtables.com/web/color/RGB_Color.html)

import opc                                              #Import Open Pixel Control
import time                                             #Import time access and conversions 
import random                                           #Import and generate pseudo-random numbers 


def A5():                                               #DEF - keyword for defining a function

    ##A. Assigments
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
    leds =[(255,0,255)]*360                             #Simulator color [R,G,B] * numbers of leds working - PINK

    client = opc.Client('localhost:7890')               #Use the Simulator_Fadecandy
    client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
    client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
    


    ##B. Nice animation
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
    led = 0                                             #Assignment of the LED equal to 0
    while led<30:                                       #While function
        for rows in range(7):                           #For loop in range(X)
            leds[led + rows*45] = (0,0,0)               #Position of the LED and rows - assignment - Simulator color [R,G,B] - BLACK
            leds[59-led + rows*45] = (0,0,0)            #Position of the LED and rows - assignment - Simulator color [R,G,B] - BLUE
        client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
        time.sleep(.1)                                  #Number in seconds - 0.1s
        led = led + 1                                   #Increment by +1 to the last number of led


    ##C. Character 5 The Grump: Angel wings Moving from right to left
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    led = 0                                             #Assign led equal to 0
    while led<60:                                       #While loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition                              
        for led in range(43):                           #For loop in range(X). Number of position who we can control moving to the left
                
            leds = [(0,0,0)]*360                        #Whole simulator Blue R,G,B (X,X,X) - BLACK

            #First line (Empty)

            #Second Line
            leds[110-led-8] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[110-led-7] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[110-led-6] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[110-led-5] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[110-led-4] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[110-led-3] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[110-led-2] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[110-led-1] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[110-led-0] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[110-led+1] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[110-led+2] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[110-led+3] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[110-led+4] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[110-led+5] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[110-led+6] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings



            #Third line
            leds[170-led-6] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[170-led-5] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[170-led-4] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[170-led-3] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[170-led-2] = (255,255,102)             #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
            leds[170-led-1] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[170-led-0] = (255,255,102)             #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
            leds[170-led+1] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[170-led+2] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[170-led+3] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[170-led+4] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings

            #Fourth Line
            
            leds[230-led-5] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            leds[230-led-4] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[230-led-3] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[230-led-2] = (255,0,0)                 #Position of the LED - assignment - Simulator color [R,G,B] - RED
            leds[230-led-1] = (255,0,0)                 #Position of the LED - assignment - Simulator color [R,G,B] - RED
            leds[230-led] = (255,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - RED
            leds[230-led+1] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[230-led+2] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN DARK
            leds[230-led+3] = (255,255,255)             #Position of the LED - assignment - Simulator color [R,G,B] - White Wings
            
            
            #Five Line
            leds[290-led-2] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            leds[290-led-1] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
            leds[290-led] = (255,128,0)                 #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE

            #Sixth Line
            leds[350-led-4] = (102,51,0)                #Position of the LED - assignment - Simulator color [R,G,B] - BROWN DARK
            leds[350-led-3] = (102,51,0)                #Position of the LED - assignment - Simulator color [R,G,B] - BROWN DARK

            leds[350-led+1] = (102,51,0)                #Position of the LED - assignment - Simulator color [R,G,B] - BROWN DARK
            leds[350-led+2] = (102,51,0)                #Position of the LED - assignment - Simulator color [R,G,B] - BROWN DARK

            client.put_pixels(leds)                     #Use the Simulator_Fadecandy - LED's
            time.sleep(.1)                              #Number in seconds - 0.1s

        break   

    time.sleep(1)                                       #Number in seconds - 0.1s


    ##D. POLAND'S FLAG
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    led = 0                                             #Assignment of the LED equal to 0
    while led<60:                                       #While function
        
        for rows in range(3):                           #For loop in range(X)
            leds[led + rows*60] = (255,255,255)         #Position of the LED and rows - assignment - Simulator color [R,G,B] - WHITE [THE FIRSTS 3 LINES - LEFT TO RIGHT]
            
        for rows in range(3,6):                         #For loop in range(X)
            leds[59-led + rows*60] = (255,0,0)          #Position of the LED and rows - assignment - Simulator color [R,G,B] - RED [THE LASTS 3 LINES - RIGTH TO LEFT]


        client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
        time.sleep(.03)                                 #Number in seconds - 0.3s
        led = led + 1                                   #Increment by +1 to the last number of led



        

A5()
