from time import sleep
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 250


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.seth(90)
        self.reset_pos()

    def move_up(self):
        print('moving up')
        self.setpos(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            sleep(1)
            return True

    def reset_pos(self):
        self.goto(STARTING_POSITION)

