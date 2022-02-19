#Animation3
# Animation for the ghost list go 1 by 1
import opc
import time
import random

leds =[(250,250,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)



#7.(Block from bottom to up) serpiente que recorre todo el panel de leds al reves
led = 0
while True:                 #hacer el movimiento para siempre 
    for led in range(0, 360, 60):   # en que rango queiro que el movimiento ocurra 
        leds = [(255,255,255)]*360      #todo de un color
        leds[330-led+1] = (0,0,255)
        leds[331-led+1] = (0,0,255)
        leds[332-led+1] = (0,0,255)
        leds[333-led+1] = (0,0,255)
        leds[334-led+1] = (0,0,255)
        leds[335-led+1] = (0,0,255)
        leds[336-led+1] = (0,0,255)
        leds[337-led+1] = (0,0,255)
        leds[338-led+1] = (0,0,255)
        leds[339-led+1] = (0,0,255)
        leds[340-led+1] = (0,0,255)
        leds[341-led+1] = (0,0,255)
        leds[342-led+1] = (0,0,255)
        leds[343-led+1] = (0,0,255)
        leds[344-led+1] = (0,0,255)
        leds[345-led+1] = (0,0,255)
        leds[346-led+1] = (0,0,255)
        leds[347-led+1] = (0,0,255)
        leds[348-led+1] = (0,0,255)
        leds[349-led+1] = (0,0,255)
        leds[350-led+1] = (0,0,255)
        leds[351-led+1] = (0,0,255)
        leds[352-led+1] = (0,0,255)
        leds[353-led+1] = (0,0,255)
        leds[354-led+1] = (0,0,255)
        leds[355-led+1] = (0,0,255)
        leds[355-led+2] = (0,0,255)
        leds[355-led+3] = (0,0,255)
        leds[355-led+4] = (0,0,255)

        
        if led == 255:                  #si alcanza el final que vuelva al inicio
            led = 0
        client.put_pixels(leds)
        time.sleep(.1)
    break


#8. (Block from up to bottom) va en columnas descendientes - no en filas        
led = 0
while True:                 #hacer el movimiento para siempre 
    for rows in range(6):   # en que rango queiro que el movimiento ocurra 
        leds = [(255,255,255)]*360      #todo de un color

        leds[led + rows*60] = (0,0,255)
        leds[led+1 + rows*60] = (0,0,255)
        leds[led+2 + rows*60] = (0,0,255)
        leds[led+3 + rows*60] = (0,0,255)
        leds[led+4 + rows*60] = (0,0,255)
        leds[led+5 + rows*60] = (0,0,255)
        leds[led+6 + rows*60] = (0,0,255)
        leds[led+7 + rows*60] = (0,0,255)
        leds[led+8 + rows*60] = (0,0,255)
        leds[led+9 + rows*60] = (0,0,255)
        leds[led+10 + rows*60] = (0,0,255)
        leds[led+11 + rows*60] = (0,0,255)
        leds[led+12 + rows*60] = (0,0,255)
        leds[led+13 + rows*60] = (0,0,255)
        leds[led+14 + rows*60] = (0,0,255)
        leds[led+15 + rows*60] = (0,0,255)
        leds[led+16 + rows*60] = (0,0,255)
        leds[led+17 + rows*60] = (0,0,255)
        leds[led+18 + rows*60] = (0,0,255)
        leds[led+19 + rows*60] = (0,0,255)
        leds[led+20 + rows*60] = (0,0,255)
        leds[led+21 + rows*60] = (0,0,255)
        leds[led+22 + rows*60] = (0,0,255)
        leds[led+23 + rows*60] = (0,0,255)
        leds[led+24 + rows*60] = (0,0,255)
        leds[led+25 + rows*60] = (0,0,255)
        leds[led+26 + rows*60] = (0,0,255)
        leds[led+27 + rows*60] = (0,0,255)
        leds[led+28 + rows*60] = (0,0,255)
        leds[led+29 + rows*60] = (0,0,255)
        leds[led+30 + rows*60] = (0,0,255)

        client.put_pixels(leds)
        time.sleep(.1)
    break

#~~~~~~~~~~~~~~~~~~~~~~~Character 3 The Grump (Mushroom)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Moving from right to left
led = 0
while led<60:                 
    for led in range(54-7):
            
        leds = [(10,10,10)]*360 #Whole simulator White R,G,B (x,x,x)

            #First line (Empty)

            #Second Line
        leds[110-led-2] = (204,102,0)
        leds[110-led-1] = (204,102,0)
        leds[110-led-0] = (204,102,0)

        #Third line
        leds[170-led-3] = (204,102,0)
        leds[170-led-2] = (255,255,102)#Yellow
        leds[170-led-1] = (204,102,0)
        leds[170-led-0] = (255,255,102)#Yellow
        leds[170-led+1] = (204,102,0)

        #Fourth Line
        leds[230-led-4] = (204,102,0)
        leds[230-led-3] = (204,102,0)
        leds[230-led-2] = (255,0,0)
        leds[230-led-1] = (255,0,0)
        leds[230-led] = (255,0,0)
        leds[230-led+1] = (204,102,0)
        leds[230-led+2] = (204,102,0)

        #Five Line
        leds[290-led-2] = (255,128,0)
        leds[290-led-1] = (255,128,0)
        leds[290-led] = (255,128,0)

        #Sixth Line
        leds[350-led-4] = (102,51,0)
        leds[350-led-3] = (102,51,0)

        leds[350-led+1] = (102,51,0)
        leds[350-led+2] = (102,51,0)

        client.put_pixels(leds)
        time.sleep(.1)
    break

#5. Two colors from the outside will finish in the middle with differents colors

    #para dos colores, uno desde la hizquierda y otro desde la derrecha
#que se paran en el medio
led = 0
while led<30: # si cambio a led<60 al cruzarse se cambian los colores
    for rows in range(6):
        leds[led + rows*60] = (0,255,0)
        leds[59-led + rows*60] = (0,255,0)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1
