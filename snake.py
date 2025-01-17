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
snake.shape("triangle")

snake_color=["navy","seagreen","maroon","orange"]



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
def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    food_turtle_stamp=food.stamp()
    food_stamps.append(food_turtle_stamp)

turtle.register_shape("p.gif")
poison = turtle.clone()
poison.shape("p.gif")
##poison_pos = [(100,150), (-120,100), (100,-120)]
poison_stamps = []
poison_pos=[]

def make_poison():
    min1_x=-int(SIZE_X/2/SQUARE_SIZE)+2
    
    max1_x=int(SIZE_X/2/SQUARE_SIZE)-3
    min1_y=-int(SIZE_Y/2/SQUARE_SIZE)-2
    max1_y=int(SIZE_Y/2/SQUARE_SIZE)-3
    poison_x = random.randint(min1_x,max1_x)*SQUARE_SIZE
    poison_y = random.randint(min1_y,max1_y)*SQUARE_SIZE

    poison.goto(poison_x,poison_y)
    poison_pos.append((poison_x,poison_y))
    poison_turtle_stamp=poison.stamp()
    poison_stamps.append(poison_turtle_stamp)
    
def make_super1():
    min2_x=-int(SIZE_X/2/SQUARE_SIZE)+3
    
    max2_x=int(SIZE_X/2/SQUARE_SIZE)-4
    min2_y=-int(SIZE_Y/2/SQUARE_SIZE)-3
    max2_y=int(SIZE_Y/2/SQUARE_SIZE)-4
    super1_x = random.randint(min2_x,max2_x)*SQUARE_SIZE
    super1_y = random.randint(min2_y,max2_y)*SQUARE_SIZE

    super1.goto(super1_x,super1_y)
    super1_pos.append((super1_x,super1_y))
    super1_turtle_stamp=super1.stamp()
    super1_stamps.append(super1_turtle_stamp)    

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if len(food_stamps) <= 6 :
       make_food()

    if len(poison_stamps) <= 3 :
       make_poison()
    if snake.pos() in food_pos:
        food_index =food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
        new_stamp()
        snake.color(random.choice(snake_color))

    if snake.pos() in poison_pos:
        poison_index=poison_pos.index(snake.pos()) #What does this do?
        print('44')
        print(poison_index)
        print(poison_stamps)
        poison.clearstamp(poison_stamps[poison_index]) #Remove eaten food stamp
        print("01")
        poison_pos.pop(poison_index) #Remove eaten food position
        print("0")
        poison_stamps.pop(poison_index) #Remove eaten food stamp
        print("You have eaten the poison!")
        remove_tail()
        
       
        
        

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
    if snake.pos() in pos_list[:-1]:
     quit()


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


    if len(pos_list)==0:
        print("ffffff")
        quit()


    turtle.ontimer(move_snake,TIME_STEP)
move_snake()
turtle.bgpic("background.gif")
turtle.mainloop()




