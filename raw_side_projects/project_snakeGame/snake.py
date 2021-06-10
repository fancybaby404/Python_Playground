import turtle
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.head.shape("triangle")

    def add_snake(self, position):
        self.snake = Turtle("circle")
        self.snake.color("White")
        self.snake.penup()
        self.snake.setpos(position)
        self.snake_body.append(self.snake)

    def create_snake(self):
        for snake_pos in STARTING_POSITIONS:
            self.add_snake(snake_pos)

    def extend(self):
        self.add_snake(self.snake_body[-1].position())
        # extends the snake from the very end of the snake

    def reset(self):
        for body in self.snake_body:
            body.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
        self.head.shape("triangle")

    def move(self):
        for body_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_num - 1].xcor()  # [2][1][0]
            new_y = self.snake_body[body_num - 1].ycor()
            self.snake_body[body_num].setpos(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() == DOWN:
            pass
        else:
            self.snake_body[0].seth(UP)

    def left(self):
        if self.snake_body[0].heading() == RIGHT:
            pass
        else:
            self.snake_body[0].seth(LEFT)

    def right(self):
        if self.snake_body[0].heading() == LEFT:
            pass
        else:
            self.snake_body[0].seth(RIGHT)

    def down(self):
        if self.snake_body[0].heading() == UP:
            pass
        else:
            self.snake_body[0].seth(DOWN)
