import time
from turtle import Screen
from paddle import Player
from ball import Ball
from pongscreen import DashedLine, ScoreBoard

screen = Screen()
dashed_line = DashedLine()

screen.bgcolor("black")
screen.title("pong")
screen.setup(800, 600)
screen.tracer(0)

player1 = Player(-380, 0)
player2 = Player(380, 0)

score_board = ScoreBoard()

p1_score = score_board.player1_score = 0
p2_score = score_board.player2_score = 0

ball = Ball()

screen.listen()
screen.onkey(fun=player1.move_up, key="w")
screen.onkey(fun=player1.move_down, key="s")

screen.onkey(fun=player2.move_up, key="Up")
screen.onkey(fun=player2.move_down, key="Down")


def reset():
    player1.sety(0)
    player2.sety(0)
    ball.setpos(0, 0)
    ball.speed = 10


game_is_on = True
ball.speed = 10
while game_is_on:
    score_board.scoreboard_refresh(p1_score, p2_score)
    time.sleep(0.1)
    screen.update()
    ball.move_forwards(ball.speed)

    # Check if ball a point
    if ball.xcor() > 430:
        p1_score += 1
        print(p1_score)
        reset()
        print('PLAYER1 GETS A POINT!')
        time.sleep(2)
    if ball.xcor() < -430:
        p2_score += 1
        reset()
        print(p2_score)
        print('PLAYER2 GETS A POINT!')
        time.sleep(3)

    # Bounce from top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_top_bottom(True)

    # Bounce from paddle
    if ball.xcor() < player1.xcor() + 20 and player1.ycor() - 80 <= ball.ycor() <= player1.ycor() + 80:
        print("player1 hit")
        ball.bounce_paddle(True)

    if ball.xcor() > player2.xcor() - 20 and player2.ycor() - 80 <= ball.ycor() <= player2.ycor() + 80:
        print("player2 hit")
        ball.bounce_paddle(True)

screen.exitonclick()
