#Interface Code NO WORKING
import opc
import time
import random
import Animation1
import Animation2


client = opc.Client('localhost:7890')
leds =[(255,255,255)]*360


value = input ('''\n\n Welcome!!! \n Select one of the Animations from bellow:
        \n\t\t 1. Animation1
        \t 2. Animation 2
        \n Type the number from 1 to 2 and press Enter: ''')

def Ani1(val):
    Y=[]
    Y.append(Animation1())
    return
def Ani2():
    Y=[]
    Y.append(Animation2())
    print(Y)
    return

while True:
    if value.isdigit() == True:
        value = int (value)
        if value > 2 or value < 1:
            value = input("Please input a number between 1 to 2.")
            continue
        else:
            break
    else:
        value = input ("Invalid input, please input an integrator between 1 to 2:")


if value == 1:
    print(Animation1(value))

elif value == 2:
    print(Animation2())


