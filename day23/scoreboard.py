from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.complete_levels =0
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)  
        
    def level_update(self,player):
        self.clear()
        self.level+=1
        self.complete_levels+=1
        self.write(f"Level: {self.level}")

    def score(self):
        self.write(f'Level:{self.level}', font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f'Score:{self.complete_levels}', align ='center', font=("Courier", 24, "normal"))
    
