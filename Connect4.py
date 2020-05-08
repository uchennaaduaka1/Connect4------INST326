import turtle
from piececolors import *
from winChecker import game_is_win


pen = turtle.Turtle()

def create_lines(a,b,x,y):
    pen.up()
    pen.goto(a,b)
    pen.down()
    pen.goto(x,y)
    
def grid():
    pen.screen().bgcolor('dark blue')
    for x in range(-150,200,50):
        create_lines(x,-200,x,200)
    
    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            pen.up()
            pen.goto(x,y)
            pen.dot(40,'white')
            
    pen._update()
    
player_turns = {'red': 'yellow', 'yellow': 'red'}
player_state = State()

def restartGame():
    pen.reset()
    pen.hideturtle()
    grid()
    State.resetBoard(tap_screen)
    pen.screen().onscreenclick(tap_screen)
    

def tap_screen(x,y):
    player = player_state.player
    slots = player_state.gameSlots
    grid = player_state.grid
    
    game_slot = int((x+200) // 50)
    counter = slots[game_slot]
    
    if counter >= len(grid):
        print("Invalid space, try another")
        return " "
    
    x = ((x + 200) // 50) * 50 - 200 + 25
    y = counter * 50 - 200 + 25
    
    pen.up()
    pen.goto(x,y)
    pen.dot(40,player)
    pen._update()
    
    grid[len(grid) - counter - 1][game_slot] = player
    last_chosen_cell = [len(grid) - counter - 1, game_slot]
    if game_is_win(grid, player, last_chosen_cell, 4):
        print("{} wins".format(player))
        restartGame()
    slots[game_slot] = counter + 1
    State.player = player_turns[player]

Screen().setup(420,420,370,0)
pen.hideturtle(0)