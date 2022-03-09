#Animation 8 - Created by Carlos Huallpa - M00763709 - 2nd Year Robotics and Mechatronics

#Website to change and modify colors (https://www.rapidtables.com/web/color/RGB_Color.html)


import opc                                                                                              #Import Open Pixel Control
import time                                                                                             #Import time access and conversions 
import random                                                                                           #Import and generate pseudo-random numbers 
import colorsys                                                                                         #Conversions between color systems
    
def A8():                                                                                               #DEF - keyword for defining a function

        leds =[(0,0,0)]*360                                                                             #Simulator color [R,G,B] * numbers of leds working - BLACK

        client = opc.Client('localhost:7890')                                                           #Use the Simulator_Fadecandy
        client.put_pixels(leds)                                                                         #Use the Simulator_Fadecandy - LED's
        client.put_pixels(leds)                                                                         #Use the Simulator_Fadecandy - LED's

                 
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        led = 0                                                                                         #Assignment of the LED equal to 0
        while led<60:                                                                                   #While function 

            for rows in range(0,6):                                                                     #For loop in range(X)
                leds[59-led + rows*60] = (rows*50,70,240)                                               #Position of the LED and rows - assignment - Simulator color [R,G,B] - BLUE
            client.put_pixels(leds)                                                                     #Use the Simulator_Fadecandy - LED's
            time.sleep(.001)                                                                            #Number in seconds - 0.001s
            led = led + 1                                                                               #Increment by +1 to the last number of led

        time.sleep(2)                                                                                   #Number in seconds - 2s


            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        led = 0                                                                                         #Assignment of the LED equal to 0
        while led<60:                                                                                   #While function 
                leds[0+led] = (0,255,0)                                                                 #Assignment color - Simulator color [R,G,B] - GREEN
                leds[60+led] = (0,255,0)                                                                #Assignment color - Simulator color [R,G,B] - GREEN
                leds[120+led] = (0,255,0)                                                               #Assignment color - Simulator color [R,G,B] - GREEN
                leds[239-led] = (0,255,0)                                                               #Assignment color - Simulator color [R,G,B] - GREEN
                leds[299-led] = (0,255,0)                                                               #Assignment color - Simulator color [R,G,B] - GREEN
                leds[359-led] = (0,255,0)                                                               #Assignment color - Simulator color [R,G,B] - GREEN
                
                time.sleep(.1)                                                                          #Number in seconds - 0.1s                                          
                client.put_pixels(leds)                                                                 #Use the Simulator_Fadecandy - LED's
                led = led + 1                                                                           #Increment by +1 to the last number of led

        led = 0                                                                                         #Assignment of the LED equal to 0
        while led<60:                                                                                   #While function 
                leds[0+led] = (255,0,0)                                                                 #Assignment color - Simulator color [R,G,B] - RED
                leds[60+led] = (255,0,0)                                                                #Assignment color - Simulator color [R,G,B] - RED
                leds[120+led] = (255,0,0)                                                               #Assignment color - Simulator color [R,G,B] - RED
                leds[239-led] = (255,0,0)                                                               #Assignment color - Simulator color [R,G,B] - RED
                leds[299-led] = (255,0,0)                                                               #Assignment color - Simulator color [R,G,B] - RED
                leds[359-led] = (255,0,0)                                                               #Assignment color - Simulator color [R,G,B] - RED
                
                time.sleep(.1)                                                                          #Number in seconds - 0.1s
                client.put_pixels(leds)                                                                 #Use the Simulator_Fadecandy - LED's
                led = led + 2                                                                           #Increment by +2 to the last number of led

        time.sleep(1)                                                                                   #Number in seconds - 1s
        # 
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        leds = [(0,0,0)]*360                                                                            #Simulator color [R,G,B] * numbers of leds working - BLACK

        client = opc.Client('localhost:7890')                                                           #Use the Simulator_Fadecandy
        client.put_pixels(leds)                                                                         #Use the Simulator_Fadecandy - LED's
        client.put_pixels(leds)                                                                         #Use the Simulator_Fadecandy - LED's

        s = 1.0 
        v = 1.0 

        for hue in range(0,360,2):                                                                      #For loop in range(X) from 0 to 360 but with skip of TWO positiond of the LED
            rgb_fractional = colorsys.hsv_to_rgb(random.randint(hue-20, hue+20)/300.0, s, v)            #Colours returns floats between 0 and 1
            r_float = rgb_fractional[0]                                                                 #Cloour red float fractional
            g_float = rgb_fractional[1]                                                                 #Cloour red float fractional
            b_float = rgb_fractional[2]                                                                 #Cloour red float fractional

            rgb = (r_float*255, g_float*255, b_float*255)                                               #Cloour RGB float fractional * times the number of the colour desitget
            leds[hue]=rgb
            client.put_pixels(leds)                                                                     #Use the Simulator_Fadecandy - LED's 

            time.sleep(0.00001)                                                                         #Number in seconds - 0.00001s
        # 
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        leds =[(255,255,255)]*360                                                                       #Simulator color [R,G,B] * numbers of leds working - WHITE

        client = opc.Client('localhost:7890')                                                           #Use the Simulator_Fadecandy
        client.put_pixels(leds)                                                                         #Use the Simulator_Fadecandy - LED's
        client.put_pixels(leds)                                                                         #Use the Simulator_Fadecandy - LED's


        s = 1.0 
        v = 1.0 
        start_hue = 50 

        for i in range(360):                                                                            #For loop in range(X) from 0 to 360 
                rgb_fractional = colorsys.hsv_to_rgb(start_hue+i/360.0, s, v)                           #colorsys returns floats between 0 and 1, THIS AFFECTS THE DIFFERENCE BETWEEN COLOURS BALLS AND DOESN'T CHANGE TOO MUCH BETWEEN THEM 
                r,g,b = rgb_fractional                                                                  #extract said floating point numbers and convert to rgb range
                leds[i] = (r*255,g*255,b*255)                                                           #From the range i created 3 lines up we assignet the colours in RGB
                client.put_pixels(leds)                                                                 #Use the Simulator_Fadecandy - LED's
                break
        time.sleep(0.1)                                                                                 #Number in seconds - 0.1s

        # Left AND right (Black Swipe ) 
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        led = 0                                                                                         #Assignment of the LED equal to 0
        while led<30:                                                                                   #While function (Close until 30)
                for rows in range(6):                                                                   #For loop in range(X) ROWS - (1 to 6) outside to inside
                    leds[led + rows*60] = (0,0,0)                                                       #Position of the LED and rows - assignment - Simulator color [R,G,B] - BLACK
                    leds[59-led + rows*60] = (0,0,0)                                                    #Position of the LED and rows - assignment - Simulator color [R,G,B] - BLACK
                client.put_pixels(leds)                                                                 #Use the Simulator_Fadecandy - LED's
                time.sleep(.1)                                                                          #Number in seconds - 0.1s
                led = led + 1                                                                           #Count +1 to the last number of led

        #Blinker Animation
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        led_list = [(0,0,0)]*360                                                                        #Simulator color [R,G,B] * numbers of led_list working - BLACK       
        fade = 10                                                                                       #Fade of the amount and size of every single fade step created

        while True:                                                                                     #While true loop = execute a block of code repeatedly until given boolean condition evaluated to False. If we write while True then the loop will run forever.
            for led in enumerate(led_list):                                                             #For loop in enumerate(X).
                r,g,b = led[1]                                                                          #Assignment of rgb to led[1]              
                r = r+fade                                                                              #Assignment of r to => r + the number assigment before in this case 10
                #g = g+fade                                                                             #Assignment of g to => g + the number assigment before in this case 10
                b = b+fade                                                                              #Assignment of b to => b + the number assigment before in this case 10

                new = (r,g,b)                                                                           # create new tuple containing the updated values
                led_list[led[0]] = new                                                                  # place it in the original list at index led_num.

                if r >=100 or r <= 1:                                                                   # check if the fade has hit its' limit;
                    fade = -fade 

            client.put_pixels(led_list)                                                                 #Use the Simulator_Fadecandy - Led_list      
time.sleep(.0002)                                                                                       #Number in seconds - 0.0002s

A8()
