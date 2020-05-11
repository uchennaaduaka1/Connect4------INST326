import turtle

t = turtle.Turtle()

def create_grid(): 
    t.hideturtle()
    turtle.bgcolor("steel blue")
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
    draw_rows()
    
    turtle.Screen().exitonclick() 
    
def draw_rows():
    t.pu()
    t.goto(-300,75)
    t.pd()
    t.goto(300,75)
    t.pu()
    t.goto(300,-75)
    t.pd()
    t.goto(-300,-75)
  
def main():
    create_grid()
    
if __name__ == "__main__":
    main()