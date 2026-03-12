from turtle import Turtle

class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_padle()

    def create_padle(self):
        pos = [40, 20, 0]
        for i in pos:
            jora = Turtle('square')
            jora.color('white')
            jora.penup()
            jora.goto(480,i)
            jora.setheading(90)
            self.segments.append(jora)

    def ball_bounce(self,ball):
        for segment in self.segments:
            if segment.distance(ball)<25:
                ball.padle()
                ball.bounce +=1
                ball.add_speed()
                break
                    
    def follow(self, ball):
        if ball.ycor()>self.segments[1].ycor():
            if self.segments[0].ycor()<280:
                for i in range(0, len(self.segments)):
                    self.segments[i].setheading(90)
                    self.segments[i].forward(20)
        elif ball.ycor()<self.segments[1].ycor():
            if self.segments[-1].ycor()>-280:
                for i in range(0, len(self.segments)):
                    self.segments[i].setheading(270)
                    self.segments[i].forward(20)