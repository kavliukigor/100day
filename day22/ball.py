from turtle import Turtle
from Padle_player import Padle
from Enemy import Enemy
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5,0.5)
        self.color('blue')
        self.setheading(90)
        self.goto(0,0)
        self.movement = 20
        self.turn = 0
        self.bounce = 0

    def direction(self):
        side = random.randint(1,2)
        if side == 1:
            self.turn = random.randint(35,145)
            self.right(self.turn)
            
        elif side ==2:
            self.turn = random.randint(35,145)
            self.left(self.turn)
            

        if self.turn > 90:
            self.turn = 180-self.turn
    
    def border(self):
        if self.ycor() >=275 or self.ycor() <= -275:
            self.setheading(360 - self.heading())
            self.bounce+=1
        
        self.forward(self.movement)
    
    def padle(self):
        self.setheading(180- self.heading())

    def add_speed(self):
        if self.bounce>=5:
            self.movement +=10
            self.bounce =0

    def reset(self):
        self.movement = 20
        self.bounce = 0