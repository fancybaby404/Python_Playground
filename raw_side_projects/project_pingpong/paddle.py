import turtle
from turtle import Turtle


class Player(Turtle):
    def __init__(self, x_axis, y_axis):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.goto(x_axis, y_axis)

    def move_up(self):
        if self.ycor() < 230:
            self.setpos(self.xcor(), self.ycor() + 40)

    def move_down(self):
        if self.ycor() > -230:
            self.setpos(self.xcor(), self.ycor() - 40)
