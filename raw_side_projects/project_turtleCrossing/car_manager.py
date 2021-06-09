from time import sleep
from turtle import Turtle
from random import randint, randrange


STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def rand_rgb():
    return randrange(1, 255), randrange(1, 255), randrange(1, 255)


class CarManager:
    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        self.car = Turtle()
        self.car.penup()
        self.car.color(rand_rgb())
        self.car.goto(320, randint(-220, 210))
        self.car.shape("square")
        self.car.shapesize(2, 1)
        self.car.seth(90)
        self.car_list.append(self.car)

    def increase_speed(self):
        self.speed += 10

    def move_forwards(self):
        for car in self.car_list:
            car.setpos(car.xcor() - self.speed, car.ycor())

    def collision_player(self, player):
        for car in self.car_list:
            if player.distance(car) < 20:
                return True

    def reset_cars(self):
        for car in self.car_list:
            car.setpos(0, 2000)
            car.clear()
            car.ht()
