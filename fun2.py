import turtle
turtle.goto(0,0)


turtle.direction = None
def up():
    turtle.direction='Up'
    print('you pressed the up key')
    on_move()

def left():
    turtle.direction='Left'
    print('you pressed the left key')
    on_move()


def right():
    turtle.direction='Right'
    print('you pressed the left key')
    on_move()

def down():
    turtle.direction='Down'
    print('you pressed the down key')
    on_move()
turtle.onkey(up,'Up')
turtle.onkey(down,'Down')
turtle.onkey(left,'Left')
turtle.onkey(right,'Right')
turtle.listen()

def on_move():
    x_pos = turtle.xcor()
    y_pos = turtle.ycor()

    if turtle.direction == 'Up':
        turtle.goto(x_pos,y_pos + 15)
    elif turtle.direction=='Down':
            turtle.goto(x_pos,y_pos-30)
    elif turtle.direction=='Left':
         turtle.goto(x_pos-15,y_pos)
    elif turtle.direction=='Right':
            turtle.goto(x_pos+15,y_pos)     
            
