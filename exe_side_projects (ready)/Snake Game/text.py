from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 20, "normal")


class Text(Turtle):
    def __init__(self, score):
        super().__init__()

        self.score = score
        self.scoreboard_refresh(self.score)

    def scoreboard_refresh(self, score):
        self.clear()
        self.penup()
        self.color("white")
        self.ht()
        self.goto(0, 260)
        self.write(f"Score: {score}", move=False, align=ALIGNMENT, font=FONT)


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.game_over()

    def game_over(self):
        self.penup()
        self.color("white")
        self.ht()
        self.write("Game Over.", align="center", font=FONT)
