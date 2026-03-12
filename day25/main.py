import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S states game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

read = pandas.read_csv('50_states.csv')
t = turtle.Turtle()
t.hideturtle()
t.penup()

score = turtle.Turtle()
score.hideturtle()
score.penup()
score.goto(-200,260)

points=0
strike =0
guesed_states = []

game_is_on = True
while game_is_on:
    score.clear()
    score.write(f'Score:{points} Strike:{strike}',align='center', font=("Courier", 24, "normal"))
    guess= screen.textinput('Guess','Your guess')
    if not guess:
        game_is_on = False
        continue
    guess=guess.title()
    res = read[read['state'] == guess]
    if len(res)>0:
        if res['state'].values[0] not in guesed_states:
            x = res['x'].values[0]
            y = res['y'].values[0]
            state_name = res['state'].values[0]
            t.goto(x,y)
            t.write(state_name,align='center')
            points+=1
            guesed_states.append(state_name)
            if points>strike:
                strike =points
        else:
            strike = 0
    elif guess== 'Exit' :
        game_is_on = False        
    elif len(res)==0:
        points =0
    
    if len(guesed_states) ==50:
        score.goto(0,0)
        score.write(f'You win!! Score is:{points} and strike:{strike}', align='center', font=("Courier", 24, "normal"))
        game_is_on = False

screen.exitonclick()