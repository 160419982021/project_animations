#Animation8


##
##import opc
##from time import sleep
##
##client = opc.Client('localhost:7890')
##
##led_list = [(0,0,0)]*360           # list of 360 tuples, each containing R,G,B values.
##fade_amount = 5                     # size of each fade step.
##print(led_list)
##print(enumerate(led_list))
##while True:
##    for led in enumerate(led_list): # enumerate creates a list of tuples that contain index and contents of each element
##                                    # in our case: led = (led_num, (R,G,B))
##        r,g,b = led[1]              # this points to the second element in led - the (R,G,B) tuple.
##        r = r+fade_amount
##        g = g+fade_amount
##        #b = b+fade_amount
##
##        new_colour = (r,g,b)            # create new tuple containing the updated values
##        led_list[led[0]] = new_colour   # place it in the original list at index led_num.
##
##        if r >=255 or r <= 0:           # check if the fade has hit its' limit;
##            fade_amount = -fade_amount  # if it has - change directions from the next iteration.
##
##    client.put_pixels(led_list)         # send the entire new list to the lights.
##    sleep(.02)                          # 20ms delay



##import opc
##from time import sleep
##import colorsys
##
##leds = [(0,0,0)]*360 #white
##
##client = opc.Client('localhost:7890')
##client.put_pixels(leds)
##client.put_pixels(leds)
##
##s = 1.0 ##maximum colour
##v = 1.0 ##maximum brightness
##start_hue = 50 #colour vals
##
##for i in range(60): #this decides the final value(kind of)
##	rgb_fractional = colorsys.hsv_to_rgb(start_hue+i/360.0, s, v) #colorsys returns floats between 0 and 1
##	r,g,b = rgb_fractional #extract said floating point numbers and convert to rgb range
##	leds[i] = (r*255,g*255,b*255)
##	client.put_pixels(leds) #assign
##	sleep(0.1)


##import opc
##from time import sleep
##import colorsys
##import random
##
##leds = [(0,0,0)]*360 #black
##
##client = opc.Client('localhost:7890')
##client.put_pixels(leds)
##client.put_pixels(leds)
##
##s = 1.0 ##maximum colour
##v = 1.0 ##maximum brightness
##
##for hue in range(360):
##    rgb_fractional = colorsys.hsv_to_rgb(random.randint(hue-20, hue+20)/360.0, s, v) #colorsys returns floats between 0 and 1
##    r_float = rgb_fractional[0] #extract said floating point numbers
##    g_float = rgb_fractional[1]
##    b_float = rgb_fractional[2]
##
##    rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
##    leds[hue]=rgb
##    client.put_pixels(leds) #send out
##
##    sleep(0.03) #20ms

##import opc
##from time import sleep
##import colorsys
##import random
##
##client = opc.Client('localhost:7890')
##leds = [(0,0,0)]*360
##
##s = 1.0 ##maximum colour
##v = 1.0 ##maximum brightness
##
##for hue in range(360):
##    rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v) #colorsys returns floats between 0 and 1
##    print(rgb_fractional)
##    r_float = rgb_fractional[0] #extract said floating point numbers
##    g_float = rgb_fractional[1]
##    b_float = rgb_fractional[2]
##
##    rgb = (r_float*255, g_float*255, b_float*255) #make new tuple with corrected values
##    print(rgb)
##    leds[hue] = rgb 
##    client.put_pixels(leds) #send out
##
##    sleep(0.03) #20ms






import opc
import time
import random
leds = [(255,255,255)]*360 #white
client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)
# #for led in leds: # pick out an element: led = (255,255,255)
# for led in range(60): #pick out indeces: led = 0,1,2,3...
#     leds[led] = (255,0,0)
#     time.sleep(.1)
#     client.put_pixels(leds)
# led = 0
# while led<60:
#     leds[59-led] = (0,255,0)
#     time.sleep(.1)
#     client.put_pixels(leds)
#     led = led + 1 #or reverse if you want
# #led = 59
# #while led>=0:
# #    leds[led] = (0,255,0)
# #    time.sleep(.1)
# #    client.put_pixels(leds)
# #    led = led - 1 #or reverse if you want

led = 0
while led<60: #scroll all rows at the same time
##    for rows in range(3): #first three rows left to right
##        leds[led + rows*60] = (rows*0,0,255)
    for rows in range(0,6): #last three rows reversed (right to left)
        leds[59-led + rows*60] = (rows*25,75,255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1

### reverse the last example.
### do a scroll from the middle to the outside - two pixels moving away from each other.
### reverse the scroll from the middle
### do a snake, 5 pixels long, returns to start when it hits the end
##while True:                         #do this forever:
##    for led in range(0, 360, 60):
##        leds = [(255,255,255)]*360  #white  #set everything white,
##        leds[355-led] = (0,0,255)       #set 5 leds another colour, incrementing position each frame
##        leds[355-led+1] = (0,0,255)
##        leds[355-led+2] = (0,0,255)
##        leds[355-led+3] = (0,0,255)
##        leds[355-led+4] = (0,0,255)
##        if led == 355:              #if we reach the end go back;
##            led = 0
##        client.put_pixels(leds)     #place the latest frame on screen.
##        time.sleep(0.02)            #delay the frame a bit
###what can we improve?
