import turtle

t = turtle.Turtle()

def create_grid(): 
    t.hideturtle()
    turtle.bgcolor("black")
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
    
    draw_rows()
    create_buttons()
    
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

def create_buttons():
    for square in range(1,10):
        button = turtle.Turtle()
        button.penup()
        
        if square == 1:
            button.goto(-200,138)
        if square == 2:
            button.goto(0,138)
        if square == 3:
            button.goto(200,138)
        if square == 4:
            button.goto(-200,0)
        if square == 5:    
            button.goto(0,0)
        if square == 6:
            button.goto(200,0)
        if square == 7:
            button.goto(-200,-138)
        if square == 8:
            button.goto(0,-138)
        if square == 9:
            button.goto(200, -138)
            
def main():
    create_grid()
      
if __name__ == "__main__":
    main()