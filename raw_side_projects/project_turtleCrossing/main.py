import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, GameOver

# ---------- Initialization ----------
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)
screen.bgpic(picname="")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
game_over = GameOver()

screen.listen()
screen.onkey(fun=player.move_up, key="w")

# ---------- Main ----------
game_is_on = True
time_wait = 0
new_time_wait = 9
while game_is_on:
    time.sleep(0.1)
    screen.update()
    time_wait += 1

    car_manager.move_forwards()

    # Finish Line (INCREASE LEVEL)
    if player.finish_line():
        car_manager.increase_speed()
        scoreboard.level += 1

        # Reset positions
        player.reset_pos()
        car_manager.reset_cars()
        scoreboard.scoreboard_refresh()

    # Game Over
    if car_manager.collision_player(player):
        game_is_on = False
        game_over.display_game_over()

    # Create new car
    if time_wait == new_time_wait:
        car_manager.create_car()
        new_time_wait += 9

# Display Game Over
screen.exitonclick()
