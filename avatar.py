from turtle import Turtle
TURTLE_SPEED = 10
START_LINE = (0, -280)


class Avatar(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.refresh()

    def move_up(self):
        self.forward(TURTLE_SPEED)

    def refresh(self):
        self.goto(START_LINE)
