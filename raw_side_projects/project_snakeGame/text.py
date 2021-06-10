from turtle import Turtle

from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "data.txt")


ALIGNMENT = "center"
FONT = ("Comic Sans MS", 20, "normal")


class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.scoreboard_refresh()

    def get_high_score(self):
        with open(file_path, mode="r") as data:
            self.high_score = data.read()
        return self.high_score

    def new_high_score(self, score):
        with open(file_path, mode="w") as data:
            data.write(str(self.score))

    def scoreboard_refresh(self):
        self.clear()
        self.penup()
        self.color("white")
        self.ht()
        self.goto(0, 260)
        self.write(f"Score: {self.score} | High Score: {self.get_high_score()}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            self.new_high_score(self.score)
        self.score = 0
        self.scoreboard_refresh()

    # def game_over(self):
    #     self.penup()
    #     self.color("white")
    #     self.ht()
    #     self.write("Game Over.", align="center", font=FONT)
