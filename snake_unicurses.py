# import modules necessary for the game
import random
from unicurses import *

# initialize the curses library to create our screen
stdscr = initscr()
# hide the mouse cursor
clear()
noecho()
cbreak()
curs_set(0)

# getmax screen height and width
screen_height, screen_width = getmaxyx(stdscr)
# create a new window
window = newwin(screen_height, screen_width, 0, 0)
# allow window to receive input from the keyboard
keypad(window, True)
wtimeout(window, 100)
# set the x, y coordinates of the initial position of snake's head
snk_x = screen_width // 4

snk_y = screen_height // 2
# define the initial position of the snake body
snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]
# create the food in the middle of window
food = [screen_height // 2, screen_width // 2]
mvaddch(food[0], food[1], ACS_PI)
# add the food by using PI character from curses module

# set initial movement direction to right
key = KEY_RIGHT
# create game loop that loops forever until player loses or quits the game
while True:
    # get the next key that will be pressed by user
    next_key = wgetch(window)
    # if user doesn't input anything, key remains same, else key will be set to the new pressed key
    key = key if next_key == -1 else next_key

    # check if snake collided with the walls or itself
    if snake[0][0] in [0, screen_height] or snake[0][1] in [
        0, screen_width
    ] or snake[0] in snake[1:]:
        print("You lost")
        break
    # set the new position of the snake head based on the direction
    new_head = [snake[0][0], snake[0][1]]
    if key == KEY_DOWN:
        new_head[0] += 1
    if key == KEY_UP:
        new_head[0] -= 1
    if key == KEY_RIGHT:
        new_head[1] += 1
    if key == KEY_LEFT:
        new_head[1] -= 1

    # insert the new head to the first position of snake list
    snake.insert(0, new_head)
    # check if snake ate the food
    if snake[0] == food:
        food = None  # remove food if snake ate it
        # while food is removed, generate new food in a random place on screen
        while food is None:
            new_food = [
                random.randint(1, screen_height - 1),  # 200, 400
                random.randint(1, screen_width - 1)
            ]
            food = new_food if new_food not in snake else None
        mvaddch(food[0], food[1], ACS_PI)
        refresh()
    else:
        # otherwise remove the last segment of snake body
        tail = snake.pop()
        mvaddch(tail[0], tail[1], ' ')
        refresh()
    mvaddch(snake[0][0], snake[0][1], ACS_CKBOARD)
    refresh()
    # update the position of the snake on the screen

refresh()
endwin()
