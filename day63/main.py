from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from sqlalchemy.exc import IntegrityError
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///books-collection.db'
db.init_app(app)
Bootstrap5(app)

class Book(db.Model):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

class BookShelf(FlaskForm):
    book_name=StringField('Book name', validators=[DataRequired()])
    book_author=StringField('Book author', validators=[DataRequired()])
    rating=FloatField('Rating', validators=[DataRequired()])
    submit=SubmitField('Add')

class EditRating(FlaskForm):
    rating=FloatField('New rating', validators=[DataRequired()])
    submit=SubmitField('Change')

@app.route('/')
def home():
    all_books=db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    return render_template('index.html',books=all_books)

@app.route('/add', methods=['GET','POST'])
def add():
    form = BookShelf()
    if request.method=='GET':
        return render_template('add.html',form=form)
    elif request.method=='POST':
        if form.validate_on_submit():
            new_book = Book(title=form.book_name.data, author=form.book_author.data, rating=form.rating.data)
            try:
                db.session.add(new_book)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                return render_template('add.html', form=form, error="Book already at bookshelf")
        return redirect(url_for('home'))

@app.route('/edit<int:id>', methods=['GET','POST'])
def edit(id):
    book=db.get_or_404(Book, id)
    form=EditRating()
    if request.method=='GET':
        return render_template('edit.html', book=book, form=form)
    elif request.method=='POST':
        if form.validate_on_submit():
            new_rating=request.form.get('rating')
            book.rating=new_rating
            db.session.commit()
            return redirect(url_for('home'))

@app.route('/delete<int:id>',methods=['GET','POST'])
def delete(id):
    book=db.get_or_404(Book, id)
    if request.method=='GET':
        return render_template('delete.html', book=book)
    elif request.method=='POST':
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('home'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)