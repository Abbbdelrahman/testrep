from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.x, self.y = position
        self.shape("square")
        self.penup()
        self.goto(position)
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)

    def move(self):
        self.forward(20)

    def up(self):
        self.setheading(90)

    def down(self):
        self.setheading(270)
