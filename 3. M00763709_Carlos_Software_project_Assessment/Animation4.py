#Animation4

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
