#Animation8

##
####
##import opc
##from time import sleep
##
##client = opc.Client('localhost:7890')
##
############Blinker Animation
##led_list = [(0,0,0)]*360         .
##fade_amount = 10                     # size of each fade step.
##print(led_list)
##print(enumerate(led_list))
##while True:
##    for led in enumerate(led_list): 
##        r,g,b = led[1]              
##        r = r+fade_amount
##        g = g+fade_amount
##        #b = b+fade_amount
##
##        new_colour = (r,g,b)            # create new tuple containing the updated values
##        led_list[led[0]] = new_colour   # place it in the original list at index led_num.
##
##        if r >=255 or r <= 0:           # check if the fade has hit its' limit;
##            fade_amount = -fade_amount 
##
##    client.put_pixels(led_list)      
##    sleep(.02)                          

#######################rainbown animation (show only)
##########        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##########import opc
##########import time
##########import colorsys
##########
##########leds =[(255,255,255)]*360                           #Simulator color [R,G,B] * numbers of leds working - WHITE
##########
##########client = opc.Client('localhost:7890')               #Use the Simulator_Fadecandy
##########client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
##########client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
##########
##########
##########s = 1.0 
##########v = 1.0 
##########start_hue = 50 
##########
##########for i in range(360):                                                                  #this decides the final value(kind of) THIS AFFECTS THE LENGHT OF HOW MANY BALLS THERE WILL BE IN THE LINES OR THINGY
##########	rgb_fractional = colorsys.hsv_to_rgb(start_hue+i/360.0, s, v)                   #colorsys returns floats between 0 and 1, THIS AFFECTS THE DIFFERENCE BETWEEN COLOURS BALLS AND DOESN'T CHANGE TOO MUCH BETWEEN THEM 
##########	r,g,b = rgb_fractional                                                          #extract said floating point numbers and convert to rgb range
##########	leds[i] = (r*255,g*255,b*255)
##########	client.put_pixels(leds) 
##########time.sleep(0.1)

###############Pride flag
##       
####import opc
####from time import sleep
####import colorsys
####import random
####
####leds = [(0,0,0)]*360 #black
####
####client = opc.Client('localhost:7890')
####client.put_pixels(leds)
####client.put_pixels(leds)
####
####s = 1.0 
####v = 1.0 
####
####for hue in range(0,360,2):
####    rgb_fractional = colorsys.hsv_to_rgb(random.randint(hue-20, hue+20)/300.0, s, v) #colorsys returns floats between 0 and 1
####    r_float = rgb_fractional[0]
####    g_float = rgb_fractional[1]
####    b_float = rgb_fractional[2]
####
####    rgb = (r_float*255, g_float*255, b_float*255)
####    leds[hue]=rgb
####    client.put_pixels(leds) 
####
####    sleep(0.00001) 

 ##C. 
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

####import opc
####from time import sleep
####import colorsys
####import random
####
####client = opc.Client('localhost:7890')
####leds = [(2,0,0)]*360
####
####s = 1.0 #max colour
####v = 1.0 #max brightness
####
####for hue in range(360,2):
####    rgb_fractional = colorsys.hsv_to_rgb(hue/300.0, s, v) 
####    print(rgb_fractional)
####    r_float = rgb_fractional[0]
####    g_float = rgb_fractional[1]
####    b_float = rgb_fractional[2]
####
####    rgb = (r_float*255, g_float*255, b_float*255) #tuple
####    print(rgb)
####    leds[hue] = rgb 
####    client.put_pixels(leds) 
####
####    sleep(0.00001)
####



 ##D. 
        ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import opc
import time
import random
leds = [(0,0,255)]*360
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

led = 0
while led<60:
        leds[0+led] = (0,255,0)
        leds[59+led] = (0,255,0)
        leds[119+led] = (0,255,0)
        leds[179-led] = (0,255,0)
        leds[239-led] = (0,255,0)
        leds[299-led] = (0,255,0)
        leds[359-led] = (0,255,0)
        
        time.sleep(.1)
        client.put_pixels(leds)
        led = led + 2


led = 0
while led<60:

    for rows in range(0,6): 
        leds[59-led + rows*60] = (rows*25,75,255)
    client.put_pixels(leds)
    time.sleep(.00001)
    led = led + 1


