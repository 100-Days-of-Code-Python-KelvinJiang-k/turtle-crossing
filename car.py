from turtle import Turtle
import random
INITIAL_CAR_SPEED = 10


def random_color():
    r = random.uniform(0, 0.9)
    g = random.uniform(0, 0.9)
    b = random.uniform(0, 0.9)
    return r, g, b


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.car_speed = INITIAL_CAR_SPEED
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(310, 20 * random.randint(-12, 12))
        self.color(random_color())

    def move_left(self):
        self.setx(self.xcor() - self.car_speed)
