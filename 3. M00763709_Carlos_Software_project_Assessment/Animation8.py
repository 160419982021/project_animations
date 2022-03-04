#Animation8


import opc                                                                                      #Import Open Pixel Control
import time                                                                                     #Import time access and conversions 
import random                                                                                   #Import and generate pseudo-random numbers 
import colorsys                                                                                 #Conversions between color systems
    

                                                                         #Use the Simulator_Fadecandy - LED's


def A8():

        leds =[(0,0,0)]*360                                                                             #Simulator color [R,G,B] * numbers of leds working - YELLOW

        client = opc.Client('localhost:7890')                                                           #Use the Simulator_Fadecandy
        client.put_pixels(leds)                                                                         #Use the Simulator_Fadecandy - LED's
        client.put_pixels(leds)
                 # 
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        led = 0
        while led<60:

            for rows in range(0,6): 
                leds[59-led + rows*60] = (rows*50,70,240)
            client.put_pixels(leds)
            time.sleep(.001)
            led = led + 1

        time.sleep(2)
        # 
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        led = 0
        while led<60:
                leds[0+led] = (0,255,0)
                leds[60+led] = (0,255,0)
                leds[120+led] = (0,255,0)
                leds[239-led] = (0,255,0)
                leds[299-led] = (0,255,0)
                leds[359-led] = (0,255,0)
                
                time.sleep(.1)
                client.put_pixels(leds)
                led = led + 1

        led = 0
        while led<60:
                leds[0+led] = (255,0,0)
                leds[60+led] = (255,0,0)
                leds[120+led] = (255,0,0)
                leds[239-led] = (255,0,0)
                leds[299-led] = (255,0,0)
                leds[359-led] = (255,0,0)
                
                time.sleep(.1)
                client.put_pixels(leds)
                led = led + 2

        time.sleep(1)
        # 
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        leds = [(0,0,0)]*360 

        client = opc.Client('localhost:7890')
        client.put_pixels(leds)
        client.put_pixels(leds)

        s = 1.0 
        v = 1.0 

        for hue in range(0,360,2): 
            rgb_fractional = colorsys.hsv_to_rgb(random.randint(hue-20, hue+20)/300.0, s, v)            #colorsys returns floats between 0 and 1
            r_float = rgb_fractional[0]
            g_float = rgb_fractional[1]
            b_float = rgb_fractional[2]

            rgb = (r_float*255, g_float*255, b_float*255)
            leds[hue]=rgb
            client.put_pixels(leds) 

            time.sleep(0.00001)
        # 
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        leds =[(255,255,255)]*360                                                                       #Simulator color [R,G,B] * numbers of leds working - WHITE

        client = opc.Client('localhost:7890')                                                           #Use the Simulator_Fadecandy
        client.put_pixels(leds)                                                                         #Use the Simulator_Fadecandy - LED's
        client.put_pixels(leds)                                                                         #Use the Simulator_Fadecandy - LED's


        s = 1.0 
        v = 1.0 
        start_hue = 50 

        for i in range(360):                                                                            #this decides the final value(kind of) THIS AFFECTS THE LENGHT OF HOW MANY BALLS THERE WILL BE IN THE LINES OR THINGY
                rgb_fractional = colorsys.hsv_to_rgb(start_hue+i/360.0, s, v)                           #colorsys returns floats between 0 and 1, THIS AFFECTS THE DIFFERENCE BETWEEN COLOURS BALLS AND DOESN'T CHANGE TOO MUCH BETWEEN THEM 
                r,g,b = rgb_fractional                                                                  #extract said floating point numbers and convert to rgb range
                leds[i] = (r*255,g*255,b*255)
                client.put_pixels(leds) 
        time.sleep(0.1)

        # Left AND right (Black Swipe ) TO MIDDLE UNTIL LED NUMBER 30
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        led = 0                                                                                         #Assignment of the LED equal to 0
        while led<30:                                                                                   #While function (Close until 30)
                for rows in range(6):                                                                   #For loop in range(X) ROWS - (1 to 6) outside to inside
                    leds[led + rows*60] = (0,0,0)                                                       #Position of the LED and rows - assignment - Simulator color [R,G,B] - BLACK
                    leds[59-led + rows*60] = (0,0,0)                                                    #Position of the LED and rows - assignment - Simulator color [R,G,B] - BLACK
                client.put_pixels(leds)                                                                 #Use the Simulator_Fadecandy - LED's
                time.sleep(.02)                                                                         #Number in seconds - 0.2s
                led = led + 1                                                                           #Count +1 to the last number of led

        # 
            ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Blinker Animation
        led_list = [(0,0,0)]*360         
        fade = 10                                                                                       # size of each fade step.

        while True:
            for led in enumerate(led_list): 
                r,g,b = led[1]              
                r = r+fade
                #g = g+fade
                b = b+fade

                new = (r,g,b)                                                                           # create new tuple containing the updated values
                led_list[led[0]] = new                                                                  # place it in the original list at index led_num.

                if r >=100 or r <= 1:                                                                   # check if the fade has hit its' limit;
                    fade = -fade 

            client.put_pixels(led_list)      
            time.sleep(.0002)  
A8()
