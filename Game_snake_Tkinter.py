from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00" #Color snake = GREEN from [HEX]. Others= RGB, CMYK, HSV, HSL
FOOD_COLOR = "#FF0000" #Color food = RED from [HEX].
BACKGROUND_COLOR = "#000000" #Color background = Black from [HEX].

class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("Snake game")
window.resizable(False, False) #Can be change the X-Axis and Y-Axis, respectivament (x,y) using TRUE and FALSE

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.mainloop()
