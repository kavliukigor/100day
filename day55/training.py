from flask import Flask, url_for

app = Flask(__name__)

def make_bold(function):
    def wraper():
        res = f'<b>{function()}</b>'
        return res
    return wraper

def make_italic(function):
    def wraper():
        res = f'<em>{function()}</em>'
        return res
    return wraper

def make_underlined(function):
    def wraper():
        res = f'<u>{function()}</u>'
        return res
    return wraper

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">NIGA</h1>'\
    '<p>Sosi bibu</p>'\
    '<img src=https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHhoNzBzeTFvZTIxanE4eGEwYW1rajB0bW1qNmpyZzJ2emR5bGVveiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/05QJ5G5MMfhJEhUOJi/giphy.gif>'

@app.route('/bye')
@make_bold
@make_underlined
def say_bye(): 
    return 'Bye'

@app.route('/<name>/<int:number>')
def greet(name, number):
    print(f'{name} {number}')
    return f"Hello {name} {number}"

app.run(debug=True)