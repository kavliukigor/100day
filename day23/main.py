import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
manager = CarManager()
scoreboard = Scoreboard()
scoreboard.score()
manager.first_gen()

screen.listen()
screen.onkeypress(player.move, 'w')
screen.onkeypress(player.level_up, 'space')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor()>=280:
        player.level_up()
        scoreboard.level_update(player)
        manager.level_up_speed() 
        manager.gen_cars(player)        
        scoreboard.clear()              
        scoreboard.score()
    
    game_is_on = manager.colission(player)
    if not game_is_on:
        scoreboard.game_over()
    
    manager.move()

screen.exitonclick()