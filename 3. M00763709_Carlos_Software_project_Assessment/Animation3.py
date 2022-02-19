#Animation3
# Animation for the ghost list go 1 by 1
import opc
import time
import random

leds =[(250,250,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

p = 0
print (enumerate(leds))
while True:
    Ghost = [25,34,91,105,206,214,268,327,311,333]
    leds[Ghost[p]] = (0,0,0)
    client.put_pixels(leds)
    time.sleep(1)
    p = p + 1
    if p == 10:
        break
