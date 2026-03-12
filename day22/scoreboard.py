from turtle import Turtle

class Score(Turtle):
    def __init__(self, x_position): 
        super().__init__()
        self.points = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x_position, 260)  
        self.update_score()  
        
    def update_score(self):
        self.clear()
        self.write(self.points, align="center", font=("Arial", 24, "normal"))
    
    def add_point(self):
        self.points += 1
        self.update_score()