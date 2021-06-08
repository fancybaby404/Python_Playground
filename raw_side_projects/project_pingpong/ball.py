from turtle import Turtle
from random import randint, choice

RANDOM_ANGLES = [(randint(0, 30)), (randint(320, 360)), (randint(150, 180)), (randint(180, 210))]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.set_heading()

    def set_heading(self):
        self.setheading(choice(RANDOM_ANGLES))

    def move_forwards(self, speed):
        self.forward(speed)

    def bounce_top_bottom(self, increase_speed):
        self.setheading(360 - self.heading() % 360)
        if increase_speed:
            self.speed += 1

    def bounce_paddle(self, increase_speed):
        self.setheading(180 - self.heading() % 360)
        if increase_speed:
            self.speed += 5
