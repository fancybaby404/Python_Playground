import time
from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=700, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Colors:\nRed, Orange, Yellow, Green, Blue, and Purple\n\nWhich turtle will win the race? Enter a color: ").lower()
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
all_turtles = []

if user_bet:
    is_race_on = True
else:
    text = Turtle()
    text.hideturtle()
    text.penup()
    text.setposition(-50, 0)
    text.write("You didn't enter a bet", True)
    time.sleep(3)
    screen.bye()

y_position = -165
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.shapesize(2)
    turtle.color(color)
    turtle.penup()
    y_position += 50
    turtle.setpos(-300, y_position)
    all_turtles.append(turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 300:
            is_race_on = False
            winning_turtle = turtle.color()[1]
            print(f"{winning_turtle} turtle wins!")
            
        turtle.forward(randint(0, 10))

if user_bet == str(winning_turtle).lower():
    print(f"Congratulations your bet is right! {winning_turtle} turtle won!")
else:
    print(f"Your bet was: {user_bet}\nBetter luck next time!")

screen.exitonclick()
