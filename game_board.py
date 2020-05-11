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
    
    wn = WindowFunction()
    
    turns = 9

    
    wn.x_click()
    wn.o_click() 
       
    t.mainloop()
      
    
class WindowFunction:
    def __init__(self):
        t.setup(700,700)
        window = t.Screen()
        window.title("TIC TAC TOE!") 
        self.window = window
        
    def x_click(self):
        self.window.onclick(draw_x)
        
    def o_click(self):
        self.window.onclick(draw_o)
 

            
def draw_x(x,y):
    tictactoe = t.Turtle()
    tictactoe.hideturtle()
    tictactoe.pu()
    tictactoe.goto(x,y-40)
    tictactoe.pencolor("white")
    tictactoe.write("X", False, "center",["chalkduster",80])
    onscreenclick(draw_o)

def draw_o(x,y):
    tictactoe = t.Turtle()
    tictactoe.hideturtle()
    tictactoe.pu()
    tictactoe.goto(x,y-40)
    tictactoe.pencolor("white")
    tictactoe.write("O", False, "center",["chalkduster",80])
    onscreenclick(draw_x)
            
                    
    
        
    
    
if __name__ == "__main__":
    create_game()
    