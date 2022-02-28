#Animation7

#Website to change and modify colors (https://www.rapidtables.com/web/color/RGB_Color.html)


import opc
import time
import random

leds =[(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)

def world_r():
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

    leds =[(0,0,0)]*360
    client.put_pixels(leds)
    for i in range(len(z)):
        leds[z[i]] = (204,255,255)
        client.put_pixels(leds)
        time.sleep(0.055)
        
world_r ()
time.sleep(1)
world_r ()
time.sleep(1)
world_r ()
time.sleep(1)
world_r ()
time.sleep(1)
world_r ()
time.sleep(1)
world_r ()
time.sleep(1)
world_r ()
time.sleep(1)
world_r ()
time.sleep(1)
world_r ()
time.sleep(1)
world_r ()
time.sleep(1)
world_r ()
time.sleep(1)
world_r ()
