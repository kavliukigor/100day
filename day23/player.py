from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.move_dist = MOVE_DISTANCE

    def move(self):
        if self.ycor()<280:
            self.forward(self.move_dist)

    def level_up(self):
        if self.ycor()>=280:
            self.goto(STARTING_POSITION)