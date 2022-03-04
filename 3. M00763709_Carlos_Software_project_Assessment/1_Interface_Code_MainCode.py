#Interface Code NO WORKING
import opc
import time
import random
import colorsys

s = 1.0 ##maximum colour
v = 1.0 ##maximum brightness
start_hue = 50 #colour vals


client = opc.Client('localhost:7890')
leds =[(255,255,255)]*360

def main ():

    value = input ('''\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to my code!!!
\nSelect one of the animations from bellow:
            \n\t\t 1. Animation 1
            \n\t\t 2. Animation 2
            \n\t\t 3. Animation 3
            \n\t\t 4. Animation 4
            \n\t\t 5. Animation 5
            \n\t\t 6. Animation 6
            \n\t\t 7. Animation 7
            \n\t\t 8. Animation 8
            
            \nType the number from 1 to 8 and press Enter: ''')




    def A1():                                               #DEF - keyword for defining a function
        
        ##A. Set up - White
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        leds =[(255,255,255)]*360                           #Simulator color [R,G,B] * numbers of leds working - WHITE

        client = opc.Client('localhost:7890')               #Use the Simulator_Fadecandy
        client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
        client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's

        time.sleep(1)                                       #Number in seconds - 1s


        ##B. Left to right (Cortain - Red)
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        led=0                                               #Assignment of the LED equal to 0
        for led in range(1,60):                             #For loop in range(X)
            leds[led] = (255,0,0)                           #Position of the LED - assignment - Simulator color [R,G,B] - RED
            leds[led+60] = (255,0,0)                        #Position of the LED - assignment - Simulator color [R,G,B] - RED
            leds[led+120] = (255,0,0)                       #Position of the LED - assignment - Simulator color [R,G,B] - RED
            leds[led+180] = (255,0,0)                       #Position of the LED - assignment - Simulator color [R,G,B] - RED
            leds[led+180+60] = (255,0,0)                    #Position of the LED - assignment - Simulator color [R,G,B] - RED
            leds[led+120+180] = (255,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - RED
            time.sleep (0.02)                               #Number in seconds - 1s
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's


        ##C. Doble movement (Light blue and Green)
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        led = 0                                             #Assignment of the LED equal to 0
        while led<60:                                       #While function
            for rows in range(3):                           #For loop in range(X) - (1 to 3) lines from left to right
                leds[led + rows*60] = (51,255,255)          #Position of the LED and rows - assignment - Simulator color [R,G,B] - LIGHT BLUE
            for rows in range(3,6):                         #For loop in range(X) - (4 to 6) lines from right to left
                leds[59-led + rows*60] = (0,255,0)          #Position of the LED and rows - assignment - Simulator color [R,G,B] - GREEN
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(.01)                                 #Number in seconds - 0.1s
            led = led + 1                                   #Count +1 to the last number of led

        leds =[(0,0,0)]*360                                 #Simulator color [R,G,B] * numbers of leds working - White

        client = opc.Client('localhost:7890')               #Use the Simulator_Fadecandy
        client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
        client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's


        ##D. Movement of Watt from right to left covering the whole horitzontal leds (Range 54)
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Character 1 Watt~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        led = 0                                             #Assignment of the LED equal to 0
        while led<60:                                       #While function                 
            for led in range(54):                           #For loop in range(X)   
                leds = [(0,0,255)]*360                      #Whole simulator Blue R,G,B (X,X,X) - BLUE
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~Feet(Black -(0,0,0))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                leds[351-led+2] = (0,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
                leds[351-led+3] = (0,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
                leds[351-led+4] = (0,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - BLACK

                leds[351-led+6] = (0,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
                leds[351-led+7] = (0,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
                leds[351-led+8] = (0,0,0)                   #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~Outside(Orange -(255,128,0))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Inside(Orange (255,128,0))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                
                leds[110-led+6] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
                
                leds[170-led+4] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
                leds[170-led+5] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
                leds[170-led+6] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
                leds[170-led+7] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE
                leds[170-led+8] = (255,128,0)               #Position of the LED - assignment - Simulator color [R,G,B] - ORANGE

                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Mouth(Red -(255,0,0))~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                leds[230-led+5] = (255,0,0)                 #Position of the LED - assignment - Simulator color [R,G,B] - RED
                leds[230-led+6] = (255,0,0)                 #Position of the LED - assignment - Simulator color [R,G,B] - RED
                leds[230-led+7] = (255,0,0)                 #Position of the LED - assignment - Simulator color [R,G,B] - RED
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~Eyes[Yellow (255,255,102)]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                leds[110-led+5] = (255,255,102)             #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
                leds[110-led+7] = (255,255,102)             #Position of the LED - assignment - Simulator color [R,G,B] - YELLOW
                
                client.put_pixels(leds)                     #Use the Simulator_Fadecandy - LED's
                time.sleep(.1)                              #Number in seconds - 0.1s
            break                                           #The break statement in Python terminates the current loop and resumes execution at the next statement


        ##E. Left to right (Black Swipe )
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


    def A4():                                               #DEF - keyword for defining a function

    ##A. Assigments
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
        leds =[(0,0,0)]*360                                 #Simulator color [R,G,B] * numbers of leds working - BLACK
        led_colour=[(0,0,0)]*360                            #Simulator color [R,G,B] * numbers of leds working - BLACK

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
            time.sleep(.02)                                 #Number in seconds - 0.2s
            led = led + 1                                   #Increment by +1 to the last number of led


    ##C. Using a list show the Character 4 Goof Ball (Gosh)
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        p = 0                                               #Assign p equal to 0
        #print (enumerate(leds))
        while True:                                         #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.
            Ghost = [89,90,91,148,150,152,207,208,209,210,211,212,213,268,272,329,330,331] #Make a list of the positions of the Ghost 1 by 1 in order
            leds[Ghost[p]] = (255,255,255)                  #Position of the LED - assignment - Simulator color [R,G,B] - White
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(0.1)                                 #Number in seconds - 1s
            p = p + 1                                       #Increment by +1
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
                time.sleep(.04)                             #Number in seconds - 0.04s
            
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


    def A6():                                               #DEF - keyword for defining a function

        ##A. Assigments
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
        leds =[(0,0,0)]*360                                 #Simulator color [R,G,B] * numbers of leds working - BLACK

        client = opc.Client('localhost:7890')               #Use the Simulator_Fadecandy
        client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
        client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
        

        ##B. Blue Swipe - left to right
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        led = 0                                             #Assignment of the LED equal to 0
        while led<60:                                       #While function
            for rows in range(6):                           #For loop in range(X)
                leds[led + rows*60] = (0,100,255)           #Position of the LED and rows - assignment - Simulator color [R,G,B] - BLACK
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(.02)                                 #Number in seconds - 0.02s
            led = led + 1                                   #Increment by +1 to the last number of led


        ##C. Show the Game World 1
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        led=0                                               #Assign led equal to 0
        leds = [(0,0,0)]*360                                #Simulator color [R,G,B] * numbers of leds working - BLACK
        time.sleep(.1)                                      #Number in seconds - 0.1s

        
        ##First line
        leds[0-led+4] = (0,255,0)                           #Position of the LED - assignment - Simulator color [R,G,B] - Green
        leds[0-led+5] = (0,255,0)                           #Position of the LED - assignment - Simulator color [R,G,B] - Green
        leds[0-led+6] = (0,255,0)                           #Position of the LED - assignment - Simulator color [R,G,B] - Green

        leds[10-led+7] = (255,255,102)                      #Position of the LED - assignment - Simulator color [R,G,B] - Yellow

        leds[30-led+8] = (0,255,255)                        #Position of the LED - assignment - Simulator color [R,G,B] - Light blue
        leds[30-led+9] = (0,255,255)                        #Position of the LED - assignment - Simulator color [R,G,B] - Light blue
        leds[30-led+10] = (0,255,255)                       #Position of the LED - assignment - Simulator color [R,G,B] - Light blue
        leds[30-led+11] = (0,255,255)                       #Position of the LED - assignment - Simulator color [R,G,B] - Light blue
        
        ##Second Line
        leds[60-led+3] = (0,255,0)                          #Position of the LED - assignment - Simulator color [R,G,B] - Green
        leds[60-led+4] = (0,255,0)                          #Position of the LED - assignment - Simulator color [R,G,B] - Green
        leds[60-led+5] = (0,255,0)                          #Position of the LED - assignment - Simulator color [R,G,B] - Green
        leds[60-led+6] = (0,255,0)                          #Position of the LED - assignment - Simulator color [R,G,B] - Green
        leds[60-led+7] = (0,255,0)                          #Position of the LED - assignment - Simulator color [R,G,B] - Green

        leds[70-led+5] = (255,0,255)                        #Position of the LED - assignment - Simulator color [R,G,B] - Pink

        leds[90-led+9] = (0,255,255)                        #Position of the LED - assignment - Simulator color [R,G,B] - Light blue
        leds[90-led+10] = (0,255,255)                       #Position of the LED - assignment - Simulator color [R,G,B] - Light blue

        leds[236-120] = (0,255,0)                           #Position of the LED - assignment - Simulator color [R,G,B] - Green

        ##Third line
        leds[130-led+1] = (255,255,102)                     #Position of the LED - assignment - Simulator color [R,G,B] - Yellow

        leds[130-led+5] = (204,102,0)                       #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[130-led+6] = (102,0,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - Brown dark
        leds[130-led+7] = (204,102,0)                       #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[130-led+8] = (255,255,102)                     #Position of the LED - assignment - Simulator color [R,G,B] - Yellow
        leds[130-led+9] = (204,102,0)                       #Position of the LED - assignment - Simulator color [R,G,B] - Brown

        leds[236-60] = (0,255,0)                            #Position of the LED - assignment - Simulator color [R,G,B] - Green

        
        ##Fourth Line
        leds[270-60] = (0,255,0)                            #Position of the LED - assignment - Simulator color [R,G,B] - Green
        leds[230-led-2] = (0,255,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - Green
        leds[230-led-1] = (0,255,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - Green
        leds[230-led] = (0,255,0)                           #Position of the LED - assignment - Simulator color [R,G,B] - Green
        leds[230-led+1] = (0,255,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - Green

        leds[236] = (255,178,102)                           #Position of the LED - assignment - Simulator color [R,G,B] - Brown for tree

        ##Five Line
        leds[240-led+0] = (255,0,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - Red

        leds[247-led-1] = (255,0,255)                       #Position of the LED - assignment - Simulator color [R,G,B] - Pink

        leds[270-led-1] = (0,255,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - Green
        leds[270-led+0] = (0,255,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - Green
        leds[270-led+1] = (0,255,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - Green

        leds[290-led-1] = (0,255,0)                         #Position of the LED - assignment - Simulator color [R,G,B] - Green
        leds[290-led] = (0,255,0)                           #Position of the LED - assignment - Simulator color [R,G,B] - Green


        leds[290-led+6] = (255,128,0)                       #Position of the LED - assignment - Simulator color [R,G,B] - Orange
        leds[290-led+7] = (255,128,0)                       #Position of the LED - assignment - Simulator color [R,G,B] - Orange
        leds[290-led+8] = (255,128,0)                       #Position of the LED - assignment - Simulator color [R,G,B] - Orange
        leds[290-led+9] = (255,128,0)                       #Position of the LED - assignment - Simulator color [R,G,B] - Orange

        ##Sixth Line
        leds[300] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[301] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[302] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[303] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[304] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[305] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[306] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[307] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[308] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[309] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[310] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown


        leds[316] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[317] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[318] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[319] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[320] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[321] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[322] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[323] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[324] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[325] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[326] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[327] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[328] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[329] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[330] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[331] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown

        leds[338] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[339] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[340] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[341] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[342] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[343] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[344] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown

        leds[349] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[350] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[351] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[352] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[353] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[354] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[355] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[356] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[357] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[358] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown
        leds[359] = (204,102,0)                             #Position of the LED - assignment - Simulator color [R,G,B] - Brown


        client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
        time.sleep(2)                                       #Number in seconds - 2s


        ##D. Black Swipe (left to right)
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        led = 0                                             #Assignment of the LED equal to 0
        while led<60:                                       #While function     
            for rows in range(6):                           #For loop in range(X)
                leds[led + rows*60] = (0,0,0)               #Position of the LED and rows - assignment - Simulator color [R,G,B] - BLUE
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(.02)                                 #Number in seconds - 0.2s
            led = led + 1                                   #Increment by +1 to the last number of led


        ##E. Show parts of the Game World 1 in order of the list made
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        f = 0                                               #Assignment of the f equal to 0
        while True:                                         #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.
            floor = [135,137,139,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359]#Assingment of a list 
            leds[floor[f]] = (204,102,0)                    #Asssign a color to the list made
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(.01)                                 #Number in seconds - 0.1s
            f = f + 1                                       #Increment by +1
            if f == 67:                                     #If f is equal to 67 do the code bellow
                break                                       #The break statement in Python terminates the current loop and resumes execution at the next statement
        time.sleep(1)                                       #Number in seconds - 1s



        n = 0                                               #Assignment of the n equal to 0
        while True:                                         #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.
            nature = [271,272,273,212, 176,116]             #Assingment of a list 
            leds[nature[n]] = (0,255,0)                     #Asssign a color to the list made
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(.01)                                 #Number in seconds - 0.1s
            n = n + 1                                       #Increment by +1
            if n == 6:                                      #If n is equal to 6 do the code bellow
                break                                       #The break statement in Python terminates the current loop and resumes execution at the next statement
        time.sleep(1)                                       #Number in seconds - 1s



        h = 0                                               #Assignment of the h equal to 0
        while True:                                         #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.
            tree = [236]                                    #Assingment of a list 
            leds[tree[h]] = (255,178,102)                   #Asssign a color to the list made
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(.01)                                 #Number in seconds - 0.1s
            h = h + 1                                       #Increment by +1
            if h == 1:                                      #If h is equal to 1 do the code bellow
                break                                       #The break statement in Python terminates the current loop and resumes execution at the next statement
        time.sleep(1)                                       #Number in seconds - 1s


        c = 0                                               #Assignment of the c equal to 0
        while True:                                         #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.
            clouds = [38,39,40,41, 99,100,  24,25,26]       #Assingment of a list 
            leds[clouds[c]] = (0,255,255)                   #Asssign a color to the list made
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(.01)                                 #Number in seconds - 0.1s
            c = c + 1                                       #Increment by +1
            if c == 9:                                      #If c is equal to 9 do the code bellow
                break                                       #The break statement in Python terminates the current loop and resumes execution at the next statement
        time.sleep(1)                                       #Number in seconds - 1s



        e = 0                                               #Assignment of the e equal to 0
        while True:                                         #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.
            especial = [131,17,138]                         #Assingment of a list 
            leds[especial[e]] = (255,255,0)                 #Asssign a color to the list made
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(.01)                                 #Number in seconds - 0.1s
            e = e + 1                                       #Increment by +1
            if e == 3:                                      #If e is equal to 3 do the code bellow
                break                                       #The break statement in Python terminates the current loop and resumes execution at the next statement
        time.sleep(1)                                       #Number in seconds - 1s


        b = 0                                               #Assignment of the b equal to 0
        while True:                                         #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.
            block = [136]                                   #Assingment of a list 
            leds[block[b]] = (102,0,0)                      #Asssign a color to the list made
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(.01)                                 #Number in seconds - 0.1s
            b = b + 1                                       #Increment by +1
            if b == 1:                                      #If b is equal to 1 do the code bellow
                break                                       #The break statement in Python terminates the current loop and resumes execution at the next statement
        time.sleep(1)                                       #Number in seconds - 1s



        t = 0                                               #Assignment of the t equal to 0
        while True:                                         #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.
            warrior = [75,248]                              #Assingment of a list 
            leds[warrior[t]] = (255,0,255)                  #Asssign a color to the list made
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(.01)                                 #Number in seconds - 0.1s
            t = t + 1                                       #Increment by +1
            if t == 2:                                      #If t is equal to 2 do the code bellow                          
                break                                       #The break statement in Python terminates the current loop and resumes execution at the next statement
        time.sleep(1)                                       #Number in seconds - 1s



        r = 0                                               #Assignment of the r equal to 0
        while True:                                         #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.
            connection = [5,6,64,65,66,67, 228,229,230,231,289,290]#Assingment of a list 
            leds[connection[r]] = (76,153,0)                #Asssign a color to the list made
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(.01)                                 #Number in seconds - 0.1s
            r = r + 1                                       #Increment by +1
            if r == 12:                                      #If r is equal to 12 do the code bellow
                break                                       #The break statement in Python terminates the current loop and resumes execution at the next statement
        time.sleep(1)                                       #Number in seconds - 1s



        m = 0                                               #Assignment of the m equal to 0
        while True:                                         #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.
            mario = [240]                                   #Assingment of a list 
            leds[mario[m]] = (255,0,0)                      #Asssign a color to the list made
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(.01)                                 #Number in seconds - 0.1s
            m = m + 1                                       #Increment by +1
            if m == 1:                                      #If m is equal to 1 do the code bellow
                break                                       #The break statement in Python terminates the current loop and resumes execution at the next statement
        time.sleep(1)                                       #Number in seconds - 1s


        ##F. Black swipe
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        led = 0                                             #Assignment of the LED equal to 0
        while led<60:                                       #While function     
            for rows in range(6):                           #For loop in range(X)
                leds[led + rows*60] = (0,0,0)               #Position of the LED and rows - assignment - Simulator color [R,G,B] - BLUE
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(.02)                                 #Number in seconds - 0.2s
            led = led + 1                                   #Increment by +1 to the last number of led


    def world_r():#7 animation 7

        floor=[135,137,139,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359]
        nature = [271,272,273,212, 176,116]
        tree = [236]
        clouds = [38,39,40,41, 99,100,  24,25,26]
        especial = [131,17,138]
        block = [136]
        warrior = [75,248]
        connection = [5,6,64,65,66,67, 228,229,230,231,289,290]
        mario = [240]
        
        X=[floor,nature,tree,clouds,especial,block,warrior,connection,mario]
        q=random.randint(0,8)
        z=X[q]

        leds =[(0,0,0)]*360                                 #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
        client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
        for i in range(len(z)):                             #For loop in range(X)
            leds[z[i]] = (204,255,255)                      #Position of the LED - assignment - Simulator color [R,G,B] - Light White
            client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
            time.sleep(0.1)                               #Number in seconds - 0.055s
            


    def A8():


        for i in range(360): #this decides the final value(kind of) THIS AFFECTS THE LENGHT OF HOW MANY BALLS THERE WILL BE IN THE LINES OR THINGY
                rgb_fractional = colorsys.hsv_to_rgb(start_hue+i/360.0, s, v) #colorsys returns floats between 0 and 1, THIS AFFECTS THE DIFFERENCE BETWEEN COLOURS BALLS AND DOESN'T CHANGE TOO MUCH BETWEEN THEM 
                r,g,b = rgb_fractional #extract said floating point numbers and convert to rgb range
                leds[i] = (r*255,g*255,b*255)
                client.put_pixels(leds) #assign
        time.sleep(0.1)


        time.sleep(3)

        ##B. Left to right (Cortain - Red)
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        led=0                                               #Assignment of the LED equal to 0
        for led in range(60):                               #For loop in range(X)
                leds[led] = (255,153,51)                           #Position of the LED - assignment - Simulator color [R,G,B] - SLIGHTLY ORANGE
                leds[led+60] = (255,153,51)                        #Position of the LED - assignment - Simulator color [R,G,B] - SLIGHTLY ORANGE
                leds[led+120] = (255,153,51)                       #Position of the LED - assignment - Simulator color [R,G,B] - SLIGHTLY ORANGE
                leds[led+180] = (255,153,51)                       #Position of the LED - assignment - Simulator color [R,G,B] - SLIGHTLY ORANGE
                leds[led+180+60] = (255,153,51)                    #Position of the LED - assignment - Simulator color [R,G,B] - SLIGHTLY ORANGE
                leds[led+120+180] = (255,153,51)                   #Position of the LED - assignment - Simulator color [R,G,B] - SLIGHTLY ORANGE
                time.sleep (0.02)                               #Number in seconds - 1.5s
                client.put_pixels(leds)

            

#All the animations code finish HERE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    while True:
        if value.isdigit() == True:
            value = int (value)
            if value > 8 or value < 1:
                value = input("Please input a number between 1 to 8.")
                continue
            else:
                break
        else:
            value = input ("Invalid input, please input an integrator between 1 to 2:")


    if value == 1:
        A1()
    elif value == 2:
        A2()
    elif value == 3:
        A3()
    elif value == 4:
        A4()
    elif value == 5:
        A5()
    elif value == 6:
        A6()
    elif value == 7:

        world_r ()                                              #Function def of world_r
        time.sleep(1)                                           #Number in seconds - 1s
        world_r ()                                              #Function def of world_r
        time.sleep(1)                                           #Number in seconds - 1s
        world_r ()                                              #Function def of world_r
        time.sleep(1)                                           #Number in seconds - 1s
        world_r ()                                              #Function def of world_r
        time.sleep(1)                                           #Number in seconds - 1s
        world_r ()                                              #Function def of world_r
        time.sleep(1)                                           #Number in seconds - 1s
        world_r ()                                              #Function def of world_r
        time.sleep(1)                                           #Number in seconds - 1s
        world_r ()                                              #Function def of world_r
        time.sleep(1)                                           #Number in seconds - 1s
        world_r ()                                              #Function def of world_r
        time.sleep(1)                                           #Number in seconds - 1s
        world_r ()                                              #Function def of world_r
        time.sleep(1)                                           #Number in seconds - 1s
        world_r ()                                              #Function def of world_r
        time.sleep(1)                                           #Number in seconds - 1s
        world_r ()                                              #Function def of world_r
        time.sleep(1)                                           #Number in seconds - 1s

    elif value == 8:
        A8()

        

    again = input('''\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\nWould you like continue watching more animations?  

            \t YES
            \t NO
                       
ANSWER (Write down in Capital letters , please):''')

    if again == "YES":
        main()
    else:
        again = input('''Thank you for see my animations. Have a great day!
                           \t Carlos Ariel Huallpa Fernandez''')
main()
