from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-280, 280)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def points(self):
        self.score += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
