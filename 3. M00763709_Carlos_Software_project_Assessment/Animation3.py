#Animation3 - Created by Carlos Huallpa - M00763709 - 2nd Year Robotics and Mechatronics

import opc                                              #Import Open Pixel Control
import time                                             #Import time access and conversions 
import random                                           #Import and generate pseudo-random numbers 


def A3():                                               #DEF - keyword for defining a function

    ##A. Set up - PINK
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
    leds =[(255,51,255)]*360                            #Simulator color [R,G,B] * numbers of leds working - PINK

    client = opc.Client('localhost:7890')               #Use the Simulator_Fadecandy
    client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
    client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
    time.sleep(1)                                       #Number in seconds - 1s
    
    
    ##B. MOVEMENT OF THE BLOCK (UPWARDS) - BLUE
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    led = 0                                             #Assignment of the LED equal to 0
    while True:                                         #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.
        for led in range(0, 360, 60):                   #For loop in range(X) movement of code bellow from 360 to 0 in steps of 60 positions of the LED
            leds = [(224,224,224)]*360                  #Whole simulator Blue R,G,B (X,X,X) - WHITE LIGHT
            leds[330-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[331-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[332-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[333-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[334-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[335-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[336-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[337-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[338-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[339-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[340-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[341-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[342-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[343-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[344-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[345-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[346-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[347-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[348-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[349-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[350-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[351-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[352-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[353-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[354-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[355-led+1] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[355-led+2] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[355-led+3] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE
            leds[355-led+4] = (0,0,255)                 #Position of the LED - assignment - Simulator color [R,G,B] - BLUE

            
            if led == 255:                              #When the LED reach/equal to 255 will do the code bellow
                led = 0                                 #Assignment of the LED equal to 0
            client.put_pixels(leds)                     #Use the Simulator_Fadecandy - LED's
            time.sleep(.3)                               #Number in seconds - 0.3s
        
        break                                           #The break statement in Python terminates the current loop and resumes execution at the next statement


    ##C. MOVEMENT OF THE BLOCK (DOWNWARDS) - YELLOW
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       
    led = 0                                             #Assignment of the LED equal to 0
    while True:                                         #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.
        for rows in range(6):                           #For loop in range(X) movement
            leds = [(255,255,255)]*360                  #Whole simulator Blue R,G,B (X,X,X) - WHITE

            leds[led+00 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+ 1 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+ 2 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+ 3 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+ 4 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+ 5 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+ 6 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+ 7 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+ 8 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+ 9 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+10 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+11 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+12 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+13 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+14 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+15 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+16 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+17 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+18 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+19 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+20 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+21 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+22 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+23 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+24 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+25 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+26 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+27 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+28 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+29 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW
            leds[led+30 + rows*60] = (255,255,51)       #Position of the LED - assignment the rows - Simulator color [R,G,B] - YELLOW

            client.put_pixels(leds)                     #Use the Simulator_Fadecandy - LED's
            time.sleep(.3)                              #Number in seconds - 0.3s

        break                                           #The break statement in Python terminates the current loop and resumes execution at the next statement




    ##D. Character 3 - The Grump (Mushroom) - Moving from right to left covering the whole horitzontal leds (Range 54-7)
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    led = 0                                             #Assignment of the LED equal to 0
    while led<60:                                       #While loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition     
        for led in range(54-7):                         #For loop in range(X)
                
            leds = [(10,10,10)]*360                     #Whole simulator Blue R,G,B (X,X,X) - BLACK

                #First line (Empty)

                #Second Line
            leds[110-led-2] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[110-led-1] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[110-led-0] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN

            #Third line
            leds[170-led-3] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[170-led-2] = (255,255,102)             #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
            leds[170-led-1] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[170-led-0] = (255,255,102)             #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
            leds[170-led+1] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN

            #Fourth Line
            leds[230-led-4] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[230-led-3] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[230-led-2] = (255,0,0)                 #Position of the LED - assignment - Simulator color [R,G,B] - RED
            leds[230-led-1] = (255,0,0)                 #Position of the LED - assignment - Simulator color [R,G,B] - RED
            leds[230-led] = (255,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - RED
            leds[230-led+1] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN
            leds[230-led+2] = (204,102,0)               #Position of the LED - assignment - Simulator color [R,G,B] - BROWN DARK

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

        break                                           #The break statement in Python terminates the current loop and resumes execution at the next statement


    ##E. Two colors from the outside will finish in the X number from the while loop (We can change the color from each side)
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    led = 0                                             #Assignment of the LED equal to 0
    while led<15:                                       #While function
        for rows in range(6):                           #For loop in range(X) - (1 to 6) lines 
            leds[led + rows*60] = (0,255,0)             #Position of the LED and rows - assignment - Simulator color [R,G,B] - GREEN
            leds[59-led + rows*60] = (0,255,0)          #Position of the LED and rows - assignment - Simulator color [R,G,B] - GREEN
        client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
        time.sleep(.1)                                  #Number in seconds - 0.1s
        led = led + 1                                   #Count +1 to the last number of led
        
    return                                              #The return statement determines the value to be returned.





A3()                                                    #Function def A1
