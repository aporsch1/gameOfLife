import random 
import time
from os import system, name


def dead_state(rows, cols):
    """creates a 'dead' array consisting of all zeroes from dimensions given in arguments"""
    state = [[0 for i in range(cols)] for j in range(rows)]
    return state


def random_state(rows, cols):
    """alters a given array by giving each value a randomized value, either a zero or one"""
    state = dead_state(rows, cols)
    for i in range(rows):
        for j in range(cols):
            random_number = random.random()
            if random_number >= .5:
                random_number = 0
            else:
                random_number = 1
            state[i][j] = random_number
    return state


def render(state):
    """prints out given array in a readable manner"""
    cols = len(state[1])
    rows = len(state)
    display_state = dead_state(rows, cols)
    for i in range(rows):
        for j in range(cols):
            if state[i][j] == 0:
                display_state[i][j] = "   "
            else:
                display_state[i][j] = " @ "

    for i in range(rows):
        string = ""
        for j in range(cols):
            string = string + display_state[i][j]
            if j == cols-1:
                print(string)


def get_neighbors(state, x, y):
    """given an array and coordinates for a cell, finds if that cell should be 1 or 0"""
    xless = x-1
    xmore = x+1
    yless = y-1
    ymore = y+1
    if xless == -1:
        xless = len(state[0])-1

    if yless == -1:
        yless = len(state)-1

    if xmore == len(state[0]):
        xmore = 0

    if ymore == len(state):
        ymore = 0

    sumx = state[yless][xless] + state[yless][x] + state[yless][xmore] + \
    state[y][xless] + state[y][xmore] + \
    state[ymore][xless] + state[ymore][x] + state[ymore][xmore]
    if sumx == 3:
        return 1

    if sumx >= 3 or sumx < 2:
        return 0

    if state[y][x] == 1 and sumx == 2:
        return 1

    return 0

def play_gol(old_state):
    """given an array, finds what new array should be according to rules and returns it """
    cols = len(old_state[1])
    rows = len(old_state)
    new_state = dead_state(rows, cols)
    for i in range(rows):
        for j in range(cols):
            new_state[i][j] = get_neighbors(old_state, j, i)
    return new_state

def clear():
 
    _ = system('clear')

def main():
    initial_state = random_state(75, 75)
    next_state = initial_state
    while True:
        render(next_state)
        next_state = play_gol(next_state)
        time.sleep(0.05)
        clear()


main()


