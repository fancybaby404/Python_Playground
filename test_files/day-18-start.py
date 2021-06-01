from turtle import Turtle, Screen
import random


class TurtleMechanism:
    def __init__(self, turtle):
        self.turtle = turtle

    def dashed_line(self, forward_range):
        for _ in range(20):
            self.turtle.forward(forward_range)
            self.turtle.up()
            self.turtle.forward(forward_range)
            self.turtle.down()

    def shape(self, forward_range, num_of_sides):
        for _ in range(0, num_of_sides):
            self.turtle.forward(forward_range)
            self.turtle.right(360 / num_of_sides)

    def random_direction(self):
        directions = [0, 90, 180, 270]
        self.turtle.setheading(random.choice(directions))


def rand_rgb():
    return random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255)


# Initialization
screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape()
tim.pensize(5)
turtle_mech = TurtleMechanism(tim)

# Square Dashed Line
"""
for i in range(4):
    tim.left(90)
    turtle_mech.dashed_line(10)
"""

# Drawing different shapes
# Square - 90 degree angles
# Pentagon - 72 degree angles
# 360 / 4(number_of_sides) = 90 <Square>
# 360 / 5(number_of_sides) = 72 <Pentagon>
"""
for i in range(2, 30):
    # Random Colors:
    tim.color(rand_rgb())
    
    # Movement Mechanism:
    tim.speed(1000000000)
    turtle_mech.shape(100, i)
    turtle_mech.shape(-100, i)
"""

# Draw a Random Walk - turtle making random movements north,
# east, south or west each time after the same forward distance
"""
for _ in range(1000000):
    # Random Colors:
    tim.color(rand_rgb())

    # Movement Mechanism:
    tim.speed("fastest")
    turtle_mech.random_direction()
    tim.forward(50)
"""

# Draw a Spirograph
# Make a circle and gradually increase the tilt
"""
tim.speed("fastest")
angle = 1
for _ in range(360):
    tim.color(rand_rgb())
    tim.setheading(angle)
    angle += 50
    tim.circle(100)
"""

screen.exitonclick()
