from turtle import Turtle
game_is_on = True

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        pass

    def create_snake(self):
        pos = [0, -20, -40]
        for i in pos:
            jora = Turtle('square')
            jora.color('white')
            jora.penup()
            jora.goto(i,0)
            self.segments.append(jora)

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x,y)
        self.segments[0].forward(20)
    
    def turn_left(self):
        self.segments[0].left(90)

    def turn_right(self):
        self.segments[0].right(90)
    
    def game(self):
        if -280 <self.segments[0].xcor() <280 and -280 <self.segments[0].ycor() <280:
            return game_is_on == True
        else:
            return game_is_on == False
    
    def new(self):
        new = Turtle('square')
        new.color('white')
        new.penup()
        new.goto(self.segments[-1].xcor(),self.segments[-1].ycor())
        self.segments.append(new)

    def tail(self):
        for tail in self.segments[1:]:
            if self.segments[0].distance(tail)<10:
                return False
        return True

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()           