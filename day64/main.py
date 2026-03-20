from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from typing import Optional
import requests
import os
from dotenv import load_dotenv
load_dotenv()

import pyperclip

class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)

class Movies(db.Model):
    __tablename__='movies'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str]=mapped_column(String(250), nullable=False,unique=True)
    year: Mapped[int]=mapped_column(Integer, nullable=False)
    description: Mapped[str]=mapped_column(String(250),nullable=False)
    rating: Mapped[float]=mapped_column(Float, nullable=False)
    ranking: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    review: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str]=mapped_column(String(500), nullable=False)

class EditRate(FlaskForm):
    rating=FloatField('New rating', validators=[DataRequired()])
    review=StringField('New review', validators=[DataRequired()])
    submit=SubmitField('Change')

class AddFrom(FlaskForm):
    title=StringField("Film name", validators=[DataRequired()])
    submit=SubmitField('Add')
    
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
api_key=os.getenv('API_KEY')
link=os.getenv('LINK')
link_movie=os.getenv('LINK_MOVIE')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///movies.db'
db.init_app(app)
Bootstrap5(app)
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    all_movies=db.session.execute(db.select(Movies).order_by(Movies.title)).scalars()
    return render_template("index.html", movies=all_movies)

@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    movie=db.get_or_404(Movies,id)
    form = EditRate(data={'rating': movie.rating, 'review': movie.review})
    if request.method=='GET':
        return render_template('edit.html',movie=movie, form=form)
    elif request.method=='POST':
        movie.rating=form.rating.data
        movie.review=form.review.data
        db.session.commit()
        return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    movie=db.get_or_404(Movies,id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['GET','POST'])
def add():
    form=AddFrom()
    if request.method=='GET':
        return render_template('add.html',form=form)
    elif request.method=='POST':
        title=form.title.data
        params={
            'api_key': api_key,
            'query': title
        }
        res=requests.get(url=link,params=params).json()
        movie_list=res['results']
        return render_template('select.html',movies=movie_list)
        
@app.route('/select/<int:movie_id>')
def select(movie_id):
    pyperclip.copy(str(movie_id))
    res=requests.get(url=f'{link_movie}/{movie_id}',params={'api_key': api_key}).json()
    new_film=Movies(
        title=res.get('title'),
        year=res.get('release_date'),
        description=res.get('overview'),
        rating=round(res.get('vote_average'), 1) if res.get('vote_average') else 0.0,
        img_url=f"https://image.tmdb.org/t/p/w500{res.get('poster_path')}"
        )
    db.session.add(new_film)
    db.session.commit()
    return redirect(url_for('edit', id=new_film.id))

if __name__ == '__main__':
    app.run(debug=True)