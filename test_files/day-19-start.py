from turtle import Turtle, Screen


# ---------- Functions ---------- #
def move_forwards():
    turtle.forward(30)


def move_backwards():
    turtle.backward(30)


def move_left():
    current_direction = turtle.heading()
    current_direction += 30
    turtle.setheading(current_direction)


def move_right():
    current_direction = turtle.heading()
    current_direction -= 30
    turtle.setheading(current_direction)


def clear_drawing():
    turtle.penup()
    turtle.clear()
    turtle.setposition(0.00, 0.00)
    turtle.pendown()


# ---------- End of Functions ---------- #
turtle = Turtle()
turtle.pensize(5)
screen = Screen()

CURRENT_DIRECTION = turtle.heading()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_drawing)

# W = Forwards
# A = Left
# S = Backwards
# D = Right
# C = Clear Drawings

screen.listen()
screen.exitonclick()
