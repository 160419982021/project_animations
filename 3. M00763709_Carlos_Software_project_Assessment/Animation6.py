#Animation6

#Website to change and modify colors (https://www.rapidtables.com/web/color/RGB_Color.html)


import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)


#3. (Swipe left to right) para hacer todo de un color pero todas las filas a la vez 
led = 0
while led<60:
    for rows in range(6):
        leds[led + rows*60] = (0,100,255)
    client.put_pixels(leds)
    time.sleep(.02)
    led = led + 1


#~~~~~~~~~~~~~~~~~~~~~~~Game World 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

##"""
###Moving from right to left
##led = 0
##while led<60:                 
##    for led in range(42):
##"""
led=0      
leds = [(0,0,0)]*360 #Whole simulator White R,G,B (x,x,x)
time.sleep(.1)
##    #First line

leds[0-led+4] = (0,255,0) #green tree
leds[0-led+5] = (0,255,0) #green tree
leds[0-led+6] = (0,255,0) #green tree

leds[10-led+7] = (255,255,102)#Yellow

leds[30-led+8] = (0,255,255) #BLUE LIGHT
leds[30-led+9] = (0,255,255) #BLUE LIGHT
leds[30-led+10] = (0,255,255) #BLUE LIGHT
leds[30-led+11] = (0,255,255) #BLUE LIGHT
##    #Second Line

leds[60-led+3] = (0,255,0) #green tree
leds[60-led+4] = (0,255,0) #green tree
leds[60-led+5] = (0,255,0) #green tree
leds[60-led+6] = (0,255,0) #green tree
leds[60-led+7] = (0,255,0) #green tree

leds[70-led+5] = (255,0,255)# PINK

leds[90-led+9] = (0,255,255) #BLUE LIGHT
leds[90-led+10] = (0,255,255) #BLUE LIGHT

leds[236-120] = (0,255,0)

###Third line
leds[130-led+1] = (255,255,102)#Yellow

leds[130-led+5] = (204,102,0)
leds[130-led+6] = (102,0,0)
leds[130-led+7] = (204,102,0)
leds[130-led+8] = (255,255,102)#Yellow
leds[130-led+9] = (204,102,0)

leds[236-60] = (0,255,0) #green tree

##
###Fourth Line

leds[270-60] = (0,255,0)
leds[230-led-2] = (0,255,0)
leds[230-led-1] = (0,255,0)
leds[230-led] = (0,255,0)
leds[230-led+1] = (0,255,0)

leds[236] = (255,178,102)

#Five Line
leds[240-led+0] = (255,0,0)#RED

leds[247-led-1] = (255,0,255)#PINK

leds[270-led-1] = (0,255,0)
leds[270-led+0] = (0,255,0)
leds[270-led+1] = (0,255,0)#GREEN

leds[290-led-1] = (0,255,0)#GREEN
leds[290-led] = (0,255,0)#GREEN


leds[290-led+6] = (255,128,0)
leds[290-led+7] = (255,128,0)
leds[290-led+8] = (255,128,0)
leds[290-led+9] = (255,128,0)

#Sixth Line
leds[300] = (204,102,0)
leds[301] = (204,102,0)
leds[302] = (204,102,0)
leds[303] = (204,102,0)
leds[304] = (204,102,0)
leds[305] = (204,102,0)
leds[306] = (204,102,0)
leds[307] = (204,102,0)
leds[308] = (204,102,0)
leds[309] = (204,102,0)
leds[310] = (204,102,0)


leds[316] = (204,102,0)
leds[317] = (204,102,0)
leds[318] = (204,102,0)
leds[319] = (204,102,0)
leds[320] = (204,102,0)
leds[321] = (204,102,0)
leds[322] = (204,102,0)
leds[323] = (204,102,0)
leds[324] = (204,102,0)
leds[325] = (204,102,0)
leds[326] = (204,102,0)
leds[327] = (204,102,0)
leds[328] = (204,102,0)
leds[329] = (204,102,0)
leds[330] = (204,102,0)
leds[331] = (204,102,0)

leds[338] = (204,102,0)
leds[339] = (204,102,0)
leds[340] = (204,102,0)
leds[341] = (204,102,0)
leds[342] = (204,102,0)
leds[343] = (204,102,0)
leds[344] = (204,102,0)

leds[349] = (204,102,0)
leds[350] = (204,102,0)
leds[351] = (204,102,0)
leds[352] = (204,102,0)
leds[353] = (204,102,0)
leds[354] = (204,102,0)
leds[355] = (204,102,0)
leds[356] = (204,102,0)
leds[357] = (204,102,0)
leds[358] = (204,102,0)
leds[359] = (204,102,0)


client.put_pixels(leds)
time.sleep(2)
    #break


    #3. (Swipe left to right) para hacer todo de un color pero todas las filas a la vez 
led = 0
while led<60:
    for rows in range(6):
        leds[led + rows*60] = (0,0,0)
    client.put_pixels(leds)
    time.sleep(.02)
    led = led + 1



#Point by point until last one 
f = 0
print (enumerate(leds))
while True:
    floor = [135,137,139,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359]
    leds[floor[f]] = (204,102,0)
    client.put_pixels(leds)
    time.sleep(0.1)
    f = f + 1
    if f == 67:
        break
    
time.sleep(1)

n = 0
print (enumerate(leds))
while True:
    nature = [271,272,273,212, 176,116]
    leds[nature[n]] = (0,255,0)
    client.put_pixels(leds)
    time.sleep(0.1)
    n = n + 1
    if n == 6:
        break
    
time.sleep(1)


h= 0
print (enumerate(leds))
while True:
    tree = [236]
    leds[tree[h]] = (255,178,102)
    client.put_pixels(leds)
    time.sleep(0.1)
    h = h + 1
    if h == 1:
        break
time.sleep(1)


c = 0
print (enumerate(leds))
while True:
    clouds = [38,39,40,41, 99,100,  24,25,26]
    leds[clouds[c]] = (0,255,255)
    client.put_pixels(leds)
    time.sleep(0.1)
    c = c + 1
    if c == 9:
        break
time.sleep(1)


e = 0
print (enumerate(leds))
while True:
    especial = [131,17,138]
    leds[especial[e]] = (255,255,0)
    client.put_pixels(leds)
    time.sleep(0.1)
    e = e + 1
    if e == 3:
        break
time.sleep(1)

b = 0
print (enumerate(leds))
while True:
    block = [136]
    leds[block[b]] = (102,0,0)
    client.put_pixels(leds)
    time.sleep(0.1)
    b = b + 1
    if b == 1:
        break
time.sleep(1)


t = 0
print (enumerate(leds))
while True:
    warrior = [75,248]
    leds[warrior[t]] = (255,0,255)#PINK
    client.put_pixels(leds)
    time.sleep(0.1)
    t = t + 1
    if t == 2:
        break
time.sleep(1)


r = 0
print (enumerate(leds))
while True:
    connection = [5,6,64,65,66,67, 228,229,230,231,289,290]
    leds[connection[r]] = (76,153,0)
    client.put_pixels(leds)
    time.sleep(0.1)
    r = r + 1
    if r == 12:
        break
time.sleep(1)

m = 0
print (enumerate(leds))
while True:
    mario = [240]
    leds[mario[m]] = (255,0,0)
    client.put_pixels(leds)
    time.sleep(0.1)
    m = m + 1
    if m == 1:
        break
time.sleep(1)


    #3. (Swipe left to right) para hacer todo de un color pero todas las filas a la vez 
led = 0
while led<60:
    for rows in range(6):
        leds[led + rows*60] = (0,0,0)
    client.put_pixels(leds)
    time.sleep(.02)
    led = led + 1


