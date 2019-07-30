import turtle
import random 

turtle.tracer(1,0)
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) 
                                 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6

TIME_STEP = 100


pos_list = []
stamp_list = []
food_pos = []
food_stamps = []


snake = turtle.clone()
snake.shape("square")



turtle.hideturtle()
def new_stamp():
    snake_pos = snake.pos() 
    pos_list.append(snake_pos) 
         
    stm= snake.stamp()
         
    stamp_list.append(stm)
for x  in range(START_LENGTH)  :
    x_pos=snake.xcor()
    y_pos=snake.ycor()
    x_pos+=SQUARE_SIZE
    
    snake.goto(0,0) 
    new_stamp()
    
def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0)

snake.direction = "Up"
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    snake.direction="Up"
def down():
    snake.direction="Down"
def left():
    snake.direction="Left"
def right():
    snake.direction="Right"
    
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")
turtle.listen()
turtle.register_shape('trash.gif')

food = turtle.clone()
food.shape("trash.gif")
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
for this_food_pos in food_pos :
    food.goto(this_food_pos)
    gif_stamp=food.stamp()
    food_stamps.append(gif_stamp)
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
        
        

    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
    elif snake.direction=="Right":
        snake.goto(x_pos+SQUARE_SIZE, y_pos )
    elif snake.direction=="Left":
        snake.goto(x_pos-SQUARE_SIZE, y_pos)


    new_stamp()

    remove_tail()


    if x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    elif LEFT_EDGE >= x_pos:
         print("You hit the left edge! Game over!")
         quit()
    elif  DOWN_EDGE >= y_pos:
         print("You hit the down edge! Game over!")
         quit()
    elif y_pos >= UP_EDGE:
         print("You hit the up edge! Game over!")
         quit()

    turtle.ontimer(move_snake,TIME_STEP)
move_snake()

turtle.bgcolor("blue")
turtle.mainloop()




