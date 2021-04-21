#HURDLE 4 CODE:
turn_left = "true"
turn_right = "true"
wall_in_front = "true"
wall_on_right = "true"
move = "true"
front_is_clear = "true"
def turn_right():
    turn_left()
    turn_left()
    turn_left()
right_is_clear = "True"
at_goal = "true"
def go_around_wall():
    if wall_on_right():
        turn_left()
        while wall_on_right() == True:
            turn_left
            move()
            if right_is_clear():
                turn_right()
                move()
                turn_right()
                if front_is_clear() == True:
                    while wall_in_front != True:
                        move()
                        if front_is_clear != True:
                            turn_left()    
                            break   
##MAZE CODE:                    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

while not at_goal():
    if right_is_clear():
        turn_right()
        if front_is_clear():
            while front_is_clear():
                move()
                if right_is_clear():
                    break
                    
    if right_is_clear() != True:
        turn_left()
        while front_is_clear():
            move()
            if right_is_clear():
                break
                
#simplified bug free from video code:
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

#TURN RIGHT IF IT CAN, 
#GOING STRAIGHT AHEAD IF IT CANT TURN RIGHT, OR TURNING LEFT AS A LAST RESORT.