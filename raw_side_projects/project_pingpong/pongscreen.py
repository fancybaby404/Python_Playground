from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Unispace", 50, "normal")


class DashedLine(Turtle):
    def __init__(self):
        super().__init__()
        self.dashed_lines()

    def dashed_lines(self):
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, -260)
        self.speed("fastest")
        for lines in range(0, 14):
            self.color("white")
            self.pendown()
            self.seth(90)
            self.forward(20)
            self.penup()
            self.forward(20)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

    def scoreboard_refresh(self, player1_score, player2_score):
        self.clear()
        self.penup()
        self.color("white")
        self.ht()
        self.goto(0, 200)
        self.write(f"{player1_score}     {player2_score}", move=False, align=ALIGNMENT, font=FONT)
