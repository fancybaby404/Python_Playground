import colorgram
from random import choice
from turtle import Turtle
from turtle import Screen


def rgb_colors():
    colors = colorgram.extract("image.jpg", 30)

    rgb = []
    for color in colors:
        rgb.append(tuple(color.rgb))
    return rgb


# Initialization
color_list = [(246, 244, 243), (233, 239, 246), (240, 246, 243), (246, 240, 243), (129, 165, 205), (223, 150, 110),
              (31, 40, 60), (201, 134, 146), (140, 185, 163), (236, 214, 93), (167, 60, 48), (35, 100, 151),
              (141, 64, 72), (236, 165, 156), (215, 86, 78), (171, 29, 32), (49, 113, 91), (231, 160, 164),
              (155, 34, 31), (170, 188, 221), (18, 96, 71), (29, 64, 59), (57, 51, 48), (51, 45, 48), (28, 60, 114),
              (104, 128, 161), (174, 200, 188), (34, 151, 210), (208, 92, 96), (65, 65, 57)]
draw = Turtle()
draw.hideturtle()
draw.pensize(20)
draw.speed("fastest")
screen = Screen()
screen.colormode(255)

# ---------- Main ---------- #
# Paint a painting by 10X10
# Dots should be around 20 in size
# Spaced apart by around 50 paces
for _ in range(109):
    # draw 10 dots:
    draw.dot(20, choice(color_list))

    # space:
    draw.penup()
    draw.forward(50)
    draw.pendown()

    print(draw.position())

    # return position to first dot:
    if draw.position() == (500.00, draw.position()[1]):
        end_position = tuple(draw.position())
        draw.penup()
        draw.setpos(-50, 50 + draw.position()[1])
# ---------- End of Main ---------- #
screen.exitonclick()
