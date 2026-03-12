from turtle import Turtle, Screen
import random

is_race_on =False
screen = Screen()

screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "color")
colors = ['red', 'green', 'blue', 'yellow']
positions = [-75, -25, 25,75]
all_turtles = []

for turtle_num in range(0,4):
    jora = Turtle('turtle')
    jora.penup()
    jora.goto(-230, positions[turtle_num])
    jora.color(colors[turtle_num])
    all_turtles.append(jora)

if user_bet:
    is_race_on = True

while is_race_on:
    for jora in all_turtles:
        if jora.xcor() > 230:
            is_race_on = False
            win = jora.pencolor()
            if win == user_bet:
                print('Your bet win')
            else:
                print(f'Winner is {win}')

        dist = random.randint(0,15)
        jora.forward(dist)
        
screen.exitonclick()