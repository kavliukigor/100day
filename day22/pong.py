from turtle import Turtle, Screen
from Padle_player import Padle
from ball import Ball
from scoreboard import Score

from Enemy import Enemy
import time

screen = Screen()
screen.setup(1000,600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

player = Padle()
enemy = Enemy()
ball = Ball()
player_score = Score(-100)
enemy_score = Score(100)
ball.direction()

screen.listen()
screen.onkeypress(player.up, 'w')
screen.onkeypress(player.down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    enemy.follow(ball)
    player.ball_bounce(ball)
    enemy.ball_bounce(ball)
    
    if ball.xcor()<=-475:
        enemy_score.add_point()
        ball.goto(0,0)
        ball.reset()
        ball.direction()
    
    if ball.xcor()>475:
        player_score.add_point()
        ball.goto(0,0)
        ball.reset()
        ball.direction()
    
    ball.border()
    time.sleep(0.1)
    
screen.exitonclick()