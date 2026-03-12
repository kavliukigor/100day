from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        with open('day20/file.txt', 'r') as file:
            self.highscore = int(file.read())

        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.score()
            
    def score(self):
        self.clear()
        self.write(arg=f'Score is:{self.points} Record:{self.highscore}',move=False,align='center',font=('Arial',20,'normal'))

    def score_update(self):
        self.points+=1
        self.clear()
        self.write(arg=f'Score is :{self.points} Record:{self.highscore}',move=False,align='center',font=('Arial',20,'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game over! Score: {self.points}\nPress "space" to restart', align='center', font=("Courier", 16, "bold"))

    def reset(self):
        self.goto(0,260)
        if self.points >self.highscore:
            self.highscore = self.points

            with open('file.txt', 'w') as file:
                file.write(str(self.highscore))
        self.points = 0
        self.clear()
        self.score_update()