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
        
    
    t.done()
            
def draw_x(x,y):
    tictactoe = t.Turtle()
    tictactoe.hideturtle()
    tictactoe.pu()
    tictactoe.goto(x,y)
    tictactoe.pencolor("white")
    tictactoe.write("X", False, "center",["chalkduster",80])

def draw_o(x,y)
    tictactoe = t.Turtle()
    tictactoe.hideturtle()
    tictactoe.pu()
    tictactoe.goto(x,y)
    tictactoe.pencolor("white")
    tictactoe.write("O", False, "center",["chalkduster",80])

            

            
def main()
    wn = t.Screen()
    wn.title("TIC TAC TOE!")
    create_game()

    wn.onclick(draw_pieces)
    wn.listen()

    

    
    
    
if __name__ == "__main__":
    main()