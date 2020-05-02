import turtle
import time


class MoveGetter():
  def __init__(self):
    # Setting these attributes as none and false as we assume nothing has happened yet
    self.curr_move = None
    self.getting = False
  
  def done_drawing(self):
    # this function will be drawing the game board when the script is first run
    self.getting = False
  
  def on_click(self, x, y):
    #This function will allow us to move and choose positions we want to set the chips 
    if not self.getting and -200 < x < 200:
      self.curr_move = int((x + 200) / 40) + 1
      
  def get_move(self):
    #executes the move a player wants. The sleep will allow the program to be overworked
    while self.curr_move is None:
      time.sleep(0.1)
    self.getting = True
    move = self.curr_move
    self.curr_move = None
    return move

move_getter = MoveGetter()


#200 x 200 dimensions
#The drawing of the board with the turtle module.
started = time.time()
screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)
pen.ht()
pen.pu()
pen.goto(-200,-200)
pen.pd()


screen.onclick(move_getter.on_click)
screen.listen()


def win_check(columns):
    #This function will represents the logic as well as determing what wins are in terms of matches in horizontal and vertical
	for column in range(10):
		for array in range(10):
			reach = array + 4
			try:
				# Vertical Matches
				if ['YELLOW','YELLOW','YELLOW','YELLOW'] == columns[column][array:reach]:
					return 'Black'
				elif ['RED','RED','RED','RED'] == columns[column][array:reach]:
					return 'Red'
				# Horizontal Matches
				elif columns[column][array] and columns[column+1][array] and columns[column+2][array] and columns[column+3][array] == 'YELLOW':
					return 'YELLOW'
				elif columns[column][array] and columns[column+1][array] and columns[column+2][array] and columns[column+3][array] == 'RED':
					return 'Red'
			except:
				pass
		
# Our drawing functions
def draw_x():
	pen.setx(200)
	pen.setx(-200)
	
def draw_y():
	pen.sety(200)
	pen.sety(-200)

# Our drawing latitude
for i in range(10):
	draw_x()
	pen.sety(pen.ycor() + 40)
draw_x()

pen.pu()
pen.goto(-200,-200)
pen.pd()

# Our drawing longitude
for i in range(10):
	draw_y()
	pen.setx(pen.xcor() + 40)
draw_y()

pen.pu()
pen.goto(0,210)
pen.pd()
pen.write("Connect Four",align='center',font=("Trebucket", 16))
def write(text, x):
	text += 1
	pen.write(str(text),align='center',font=('Ariel',13))
	pen.pu()
	pen.setx(x + 40)
	
	
pen.pu()
pen.goto(-180,-220)
for i in range(10):
	write(i, pen.xcor())

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.ht()
t2.ht()
t1.speed(0)
t2.speed(0)
t1.pu()
t2.pu()
t1.shape('square')
t2.shape('square')
t1.color('yellow')
t2.color('red')

def admin(drop_token):
    # this function simulates the "dropping" of a chip
	if drop_token == 'l':
		print(columns)
		return True

def stamp(player):
    #the function to determine how yellow player can move
	if player == 'YELLOW':
		t1.setx(t1.xcor() - 8) # left
		t1.stamp()
		t1.sety(t1.ycor() + 8) # up
		t1.stamp()
		t1.sety(t1.ycor() - 16) # down
		t1.stamp()
		t1.setx(t1.xcor() + 8) # right
		t1.stamp()
		t1.sety(t1.ycor() + 16) # up
		t1.stamp()
		t1.setx(t1.xcor() + 8) # right
		t1.stamp()
		t1.sety(t1.ycor() - 8) # down
		t1.stamp()
		t1.sety(t1.ycor() - 8) # down
		t1.stamp()
	if player == 'RED':
     #the function to determine how the red player can move
		t2.setx(t2.xcor() - 8) # left
		t2.stamp()
		t2.sety(t2.ycor() + 8) # up
		t2.stamp()
		t2.sety(t2.ycor() - 16) # down
		t2.stamp()
		t2.setx(t2.xcor() + 8) # right
		t2.stamp()
		t2.sety(t2.ycor() + 16) # up
		t2.stamp()
		t2.setx(t2.xcor() + 8) # right
		t2.stamp()
		t2.sety(t2.ycor() - 8) # down
		t2.stamp()
		t2.sety(t2.ycor() - 8) # down
		t2.stamp()
	
	move_getter.done_drawing() # ending the function

#Draw's columns
columns = [['','','','','','','','','',''],['','','','','','','','','',''],['','','','','','','','','',''],['','','','','','','','','',''],['','','','','','','','','',''],['','','','','','','','','',''],['','','','','','','','','',''],['','','','','','','','','',''],['','','','','','','','','',''],['','','','','','','','','','']]

turn = 'RED'
while 1:
	# This function allows turns to alternate
	if turn == 'RED':
		turn = 'YELLOW'
	elif turn == 'YELLOW':
		turn = 'YELLOW'
	while 1: # This will insert a token into the game.
		
		drop_token = move_getter.get_move()
		
		
		
			
		if turn == 'YELLOW': # BLACK'S TURN
			for i in range(10):
				if columns[drop_token - 1][i] != '': # if block, check above
					continue
				else:
					columns[drop_token - 1][i] = turn # there's an empty block! lets put a token there...
					t1.pu()
					t1.goto(drop_token * 40 - 220, i * 40 - 180)
					t1.pd()
					stamp('YELLOW')
					break
			break
		
		elif turn == 'RED': # RED'S TURN
			for i in range(10):
				if columns[drop_token - 1][i] != '': # if block, check above
					continue
				else:
					columns[drop_token - 1][i] = turn # there's an empty block! lets put a token there...
					t2.pu()
					t2.goto(drop_token * 40 - 220, i * 40 - 180)
					t2.pd()
					stamp('RED')
					break
			break
		
	winning_team = win_check(columns[:])
	if winning_team:
		break
		
print('\n\n\n\n%s Won!' % (winning_team))
print('The game took %s minutes!' % ((time.time() - started) // 60))
