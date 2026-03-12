from turtle import Screen
from Snake_1 import Snake
from food import Food
from scoreboard import Score
import time

score = Score()
screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)

snake = Snake()
food = Food()

def restart():
    global game_is_on
    snake.reset()
    score.reset()
    food.refresh()
    game_is_on = True

screen.listen()
screen.onkey(snake.turn_left, 'a')
screen.onkey(snake.turn_right, 'd')
screen.onkey(restart, 'space')

game_is_on = True
game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.game()
    
    if game_is_on:
        snake.move()
        game_is_on = snake.game()

        if not snake.tail():
            game_is_on = False
        
        if snake.segments[0].distance(food)<15:
            food.refresh()
            snake.new()
            score.score_update()
    
    if not game_is_on:
        score.game_over()

print(f'Your score is: {score.points}.')    

screen.exitonclick()