from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, URL, NumberRange
import os
from dotenv import load_dotenv
import csv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRETKEY')
Bootstrap5(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url=StringField('Location Url', validators=[DataRequired(),URL()])
    open_time=StringField('Open time', validators=[DataRequired()])
    close_time=StringField('Close time', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=['✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'])
    wifi = SelectField('Wifi Rating', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    power = SelectField('Power Outlet', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add',methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if request.method=='GET':
        return render_template('add.html', form=form)
    elif request.method=='POST':
        if form.validate_on_submit():
            with open('cafe-data.csv','a', newline='',encoding='utf-8') as file:
                writer=csv.writer(file)
                writer.writerow([form.cafe.data, form.location_url.data, form.open_time.data, form.close_time.data, form.coffee.data, form.wifi.data, form.power.data])
    return redirect(url_for('add_cafe'))

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

app.run(debug=True)