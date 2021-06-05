import time
from turtle import Screen

import text
from snake import Snake
from border import Border
from food import Food
from text import Text, GameOver

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("ONONO DA SNEK")
screen.tracer(0)

snake = Snake()
food = Food()
border = Border()

score = 0
scoreboard = Text(score)

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.right, key="d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score += 1

        food.refresh()
        snake.extend()
        scoreboard.scoreboard_refresh(score)

    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -299 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        game_over = GameOver()

    # Detect collision with tail
    for snake_body in snake.snake_body[1:]:
        if snake.head.distance(snake_body) < 10:
            game_is_on = False
            game_over = GameOver()


screen.exitonclick()
