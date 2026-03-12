import colorgram
from turtle import Turtle, Screen
import random

rgb_colors = []
colors = colorgram.extract(r'C:\Users\Igor\Desktop\100day\day18\image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

screen = Screen()
screen.colormode(255)

jora = Turtle()
jora.penup()
start_x = -300
start_y = -300
dots_in_row = 15
dots_in_column = 15
jora.teleport(start_x, start_y)
for row in range(dots_in_column):
    for i in range(dots_in_row):
        jora.dot(15, random.choice(rgb_colors))
        jora.forward(40)
    
    jora.goto(start_x, start_y + (row + 1) * 40)

screen.exitonclick()
    