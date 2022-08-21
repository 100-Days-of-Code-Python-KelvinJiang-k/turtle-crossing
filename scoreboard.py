from turtle import Turtle
FONT = ('Arial', 15, 'normal')
ALIGNMENT = 'right'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-195, 270)
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def update(self):
        self.score += 1
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ('Arial', 20, 'normal'))
