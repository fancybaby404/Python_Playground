from turtle import Turtle

BOTTOM = (-300.0, -300.0)
# add from X by 20 everytime

TOP = (297.0, 307.0)
# add from X by 20 everytime

LEFT = (-307.0, -300.0)
# add from Y by 20 everytime

RIGHT = (300.0, -300.0)
# add from Y by 20 everytime


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.draw_border()
        self.ht()

    def draw_border(self):
        new_bottom = BOTTOM
        new_top = TOP
        new_right = RIGHT
        new_left = LEFT

        # BOTTOM
        for _ in range(0, 31):
            bottom = self.clone()
            bottom.goto(new_bottom)
            new_x = bottom.xcor()
            new_x += 20
            new_bottom = (new_x, bottom.ycor())

        # TOP
        for _ in range(0, 31):
            top = self.clone()
            top.goto(new_top)
            new_x = top.xcor()
            new_x -= 20
            new_top = (new_x, top.ycor())

        # RIGHT
        for _ in range(0, 31):
            right = self.clone()
            right.goto(new_right)
            new_y = right.ycor()
            new_y += 20
            new_right = (right.xcor(), new_y)

        # LEFT
        for _ in range(0, 31):
            left = self.clone()
            left.goto(new_left)
            new_y = left.ycor()
            new_y += 20
            new_left = (left.xcor(), new_y)
