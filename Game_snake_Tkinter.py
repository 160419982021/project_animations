from tkinter import *           #Import tkinter to use the console to create the game
import random                   #import random for the food of the snake

GAME_WIDTH = 700                #Width of the game
GAME_HEIGHT = 700               #Height of the game
SPEED = 50                      #Speed of the snake
SPACE_SIZE = 50                 #Size of the space of the game
BODY_PARTS = 3                  #Size of the snake at the beginning
                                #Website too see the HEX codes and the color corresponent = https://htmlcolorcodes.com/
SNAKE_COLOR = "#00FF00"         #Color snake = GREEN from [HEX]. Others= RGB, CMYK, HSV, HSL         
FOOD_COLOR = "#FF0000"          #Color food = RED from [HEX].
BACKGROUND_COLOR = "#000000"    #Color background = Black from [HEX].


class Snake:
    
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:
    
    def __init__(self):

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

#************************   Define the direction of the snake using the keyboard to control  ******************* 
def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction
            
#************************    Define when the snake collitionate with the limits ("walls")  ******************* 
def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

#********Define Game Over at the Screen (text, font, colour, tag, position of the text)  ******************* 
def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")


window = Tk()                                                                                   #Window with Tkinter
window.title("Snake game")                                                                      #Text in the title of the Tkinter
window.resizable(False, False)                                                                  #Can be change the X-Axis and Y-Axis, respectivament (x,y) using TRUE and FALSE

score = 0                                                                                       #Since which number start counting the score 
direction = 'down'                                                                              #Direcction of the snake => From the initial position of the snake 

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))                     #Label in the Tkinter Centtre, format and font of the text
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)              #Canvas of the window in Tkinter
canvas.pack()

window.update()

#************************    Sezing the creeen of the game  ******************* 

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))                                                    #Centring the screen in Tkinter X-Axis depends on the Screen_Width and Window_width
y = int((screen_height/2) - (window_height/2))                                                  #Centring the screen in Tkinter Y-Axis depends on the Screen_Height and Window_height

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#*************************   Using a,s,d,w to move the snake  ******************* 
window.bind('<w>', lambda event: change_direction('up'))
window.bind('<a>', lambda event: change_direction('left'))
window.bind('<s>', lambda event: change_direction('down'))
window.bind('<d>', lambda event: change_direction('right'))

#*************************   Using arrow keys to move the snake*******************
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake,food)

window.mainloop()
