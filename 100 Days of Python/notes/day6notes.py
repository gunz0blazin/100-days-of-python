#day6notes
'''
list = ["q", "w", "e", "r", "t", "y"]

char = len(list)
print (char)
'''
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


#use a for loop with a count

'''''
for step in range(6):
    jump()
'''
'''
while not at_goal():
    while front_is_clear():
        move()
    while not front_is_clear():
        jump()
while at_goal():
    exit
'''

'''
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
'''
'''
 # 24 lines or less
def var_jump():
    while wall_in_front():
        turn_left()
        while wall_on_right():
            move()
'''
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()   
       
def var_jump():
    turn_left()
    while wall_on_right():
        move()
   
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()
              
while not at_goal():
    if wall_in_front():
        var_jump()
    else:
        move()
'''        