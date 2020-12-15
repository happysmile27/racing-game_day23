from turtle import Turtle

FINISH_LINE_Y = 260


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.left(90)

    def move_up(self):
        self.forward(20)
        
    def move_down(self):
        self.backward(20)

    def go_to_start(self):
        self.goto(0, -280)

    def level_up(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
