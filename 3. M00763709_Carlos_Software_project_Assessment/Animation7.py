#Animation7

#Website to change and modify colors (https://www.rapidtables.com/web/color/RGB_Color.html)


import opc                                              #Import Open Pixel Control
import time                                             #Import time access and conversions 
import random                                           #Import and generate pseudo-random numbers 

leds =[(0,0,0)]*360                                     #Position of the LED - assignment - Simulator color [R,G,B] - BLACK

client = opc.Client('localhost:7890')                   #Use the Simulator_Fadecandy                            
client.put_pixels(leds)                                 #Use the Simulator_Fadecandy - LED's

def world_r():


    #Creating 9 list to use them randomly later
    floor=[135,137,139,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347,348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359]
    nature = [271,272,273,212, 176,116]
    tree = [236]
    clouds = [38,39,40,41, 99,100,  24,25,26]
    especial = [131,17,138]
    block = [136]
    warrior = [75,248]
    connection = [5,6,64,65,66,67, 228,229,230,231,289,290]
    mario = [240]

    
    X=[floor,nature,tree,clouds,especial,block,warrior,connection,mario]            #Assignment of the X equal to the lists created
    q=random.randint(0,8)                                                           #Assignment of the q work randomly using th list 0 to 8 
    z=X[q]                                                                          #Assignment of the z to use randomly(q) the lists(X)


    leds =[(0,0,0)]*360                                 #Position of the LED - assignment - Simulator color [R,G,B] - BLACK
    client.put_pixels(leds)                             #Use the Simulator_Fadecandy - LED's
    for i in range(len(z)):                             #For loop in range(X)
        leds[z[i]] = (204,255,255)                      #Position of the LED - assignment - Simulator color [R,G,B] - Light White
        client.put_pixels(leds)                         #Use the Simulator_Fadecandy - LED's
        time.sleep(0.055)                               #Number in seconds - 0.055s
        
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
world_r ()                                              #Function def of world_r
time.sleep(1)                                           #Number in seconds - 1s





