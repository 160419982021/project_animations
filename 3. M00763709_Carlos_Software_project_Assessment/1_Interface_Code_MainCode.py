#Interface Code NO WORKING
import opc
import time
import random



client = opc.Client('localhost:7890')
leds =[(255,255,255)]*360

def main ():

    value = input ('''\n\n Welcome!!! \n Select one of the Animations from bellow:
            \n\t\t 1. Animation 1
            \n\t\t 2. Animation 2
            \n\t\t 3. Animation 3
            \n\t\t 4. Animation 4
            \n\t\t 5. Animation 5
            \n\t\t 6. Animation 6
            \n\t\t 7. Animation 7
            \n\t\t 8. Animation 8
            
            \n Type the number from 1 to 2 and press Enter: ''')

##    def A1(val):
##        Y=[]
##        Y.append(Animation1())
##        return


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


    
    
##    def Ani2():
##        Y=[]
##        Y.append(Animation2())
##        print(Y)
##        return

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


    while True:
        if value.isdigit() == True:
            value = int (value)
            if value > 2 or value < 1:
                value = input("Please input a number between 1 to 2.")
                continue
            else:
                break
        else:
            value = input ("Invalid input, please input an integrator between 1 to 2:")


    if value == 1:
        A1()

    elif value == 2:
        A2()

while True:
    main()
