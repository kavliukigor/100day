from turtle import Screen, Turtle
import random
import turtle

jora = Turtle()
jora.shape('turtle')

turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b

# list = [90,180,360,270]
# def walk(walk_time):
#     for i in range(walk_time):
#         jora.color(random_color())
#         jora.forward(20)
#         jora.setheading(random.choice(list))

def spinograph(circ_num):
    twist = 360/circ_num
    jora.speed(0)
    for i in range(circ_num):
        jora.color(random_color())
        jora.circle(50)
        jora.left(twist)

spinograph(300)

screen = Screen()
screen.exitonclick()