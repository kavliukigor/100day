from turtle import Turtle, position
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_num = 0

    def first_gen(self):
        for i in range(1, 5):
                car = Turtle('square')
                car.shapesize(stretch_wid=1, stretch_len=2)  
                car.color(random.choice(COLORS))
                car.penup()
                car.setheading(180)
                car.goto(300, random.randint(-250, 250))
                car.speed_value = random.randint(self.car_speed, self.car_speed + 5)
                self.cars.append(car)

    def gen_cars(self,player):
        self.car_num +=2
        for i in range(self.car_num):
            car = Turtle('square')
            car.shapesize(stretch_wid=1, stretch_len=2)  
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto(300, random.randint(-250, 250))
            car.speed_value = random.randint(self.car_speed, self.car_speed + 5)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            if car.xcor()<=-300:
                y = car.ycor()
                car.goto(300,y)
        
        for car in self.cars:
            car.forward(car.speed_value)
    
    def colission(self,player):
        for car in self.cars:
            if car.distance(player)<20:
                return False
        return True
    
    def level_up_speed(self):
        self.car_speed += MOVE_INCREMENT



