from flask import Flask
import random

guess=random.randint(0,9)

app=Flask(__name__)

def set_text_decorator(function):
    def wraper(number):
        function(number)
        if number == guess:
            return '<h3 style="color:green">Right guess</h3>'\
                '<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>'
        elif number>guess:
            return '<h3 style="color:red">Too high</h3>'\
                '<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>'
        elif number<guess:
            return '<h3 style="color:purple">Too low</h3>'\
                '<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>'
    return wraper

@app.route('/')
def start():
    return '<h3>Guess a number between 0 and 9</h3>'\
        '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'

@app.route('/<int:number>')
@set_text_decorator
def guessing(number):
    return f'{number}'

app.run(debug=True)