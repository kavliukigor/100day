from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap=Bootstrap5(app)

class Form(FlaskForm):
    email=StringField(label='Email',validators=[DataRequired(), Email()])
    password=PasswordField(label='Password',validators=[DataRequired(),Length(min=8)])
    submit=SubmitField(label='Log in')

app.secret_key='Ultra_mega_secret'

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form=Form()
    if request.method=='GET':
        return render_template('login.html',form=form)
    elif request.method=='POST':
        if form.validate_on_submit():
            if form.email.data=='igor2018kavl@gmail.com' and form.password.data=='147258369':
                return render_template('success.html')
            else:
                return render_template('denied.html')
        return render_template('login.html',form=form)

app.run(debug=True)