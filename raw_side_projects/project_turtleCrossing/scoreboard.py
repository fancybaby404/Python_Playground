from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT2 = ("Comic Sans MS", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.ht()

        self.level = 0
        self.scoreboard_refresh()

    def scoreboard_refresh(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)


class GameOver:
    def __init__(self):
        self.text = Turtle()
        self.text.penup()
        self.text.ht()
        self.text.color("red")

    def display_game_over(self):
        self.text.goto(0, 0)
        self.text.write("Game Over.", align="center", font=FONT2)
