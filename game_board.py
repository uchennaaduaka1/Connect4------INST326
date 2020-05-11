import turtle as t




    
def create_game(): 
    
    t.hideturtle()
    t.bgcolor("steel blue")
    t.pencolor("white")
    t.pu()
    t.goto(0,250)
    t.write("TIC-TAC-TOE !", False, "center",["chalkduster",28])
    
    t.pensize(6)
    t.pu()
    t.goto(-100,200)
    t.pd()
    t.goto(-100,-200)
    t.pu()
    t.goto(100,200)
    t.pd()
    t.goto(100,-200)
    
    t.pu()
    t.goto(-300,75)
    t.pd()
    t.goto(300,75)
    t.pu()
    t.goto(300,-75)
    t.pd()
    t.goto(-300,-75)
    
    window()
    t.done()
    
    
    
def window():
    t.setup(700,700)
    window = t.Screen()
    window.title("TIC TAC TOE!") 
    x = window.onclick(draw_x)
    o = window.onclick(draw_o)
    

            
def draw_x(x,y):
    tictactoe = t.Turtle()
    tictactoe.hideturtle()
    tictactoe.pu()
    tictactoe.goto(x,y-20)
    tictactoe.pencolor("white")
    tictactoe.write("X", False, "center",["chalkduster",80])

def draw_o(x,y):
    tictactoe = t.Turtle()
    tictactoe.hideturtle()
    tictactoe.pu()
    tictactoe.goto(x,y-20)
    tictactoe.pencolor("white")
    tictactoe.write("O", False, "center",["chalkduster",80])

            

            
def main():
    create_game()
   
    
   

    

    
    
    
if __name__ == "__main__":
    main()