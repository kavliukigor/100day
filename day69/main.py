from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_required, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
import os
from dotenv import load_dotenv
from typing import List
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
login_manager=LoginManager()
login_manager.init_app(app)
Bootstrap5(app)

@login_manager.user_loader
def load_user(user_id):
    user=db.get_or_404(User,user_id)
    return user

def admin_acces(func):
    @wraps(func)
    def wraper(*args,**kwargs):
        if current_user.id==1:
            res=func(*args,**kwargs)
            return res
        else:
            abort(403)
    return wraper

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    author:Mapped['User']=relationship(back_populates='posts')
    author_id:Mapped[int]=mapped_column(Integer, db.ForeignKey('users.id'))
    comments:Mapped[List['Comment']]=relationship(back_populates='parent_post')

class User(db.Model,UserMixin):
    __tablename__='users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]=mapped_column(String(250), nullable=False)
    email: Mapped[str]=mapped_column(String(250), nullable=False, unique=True)
    password: Mapped[str]=mapped_column(String(250),nullable=False)
    posts: Mapped[List['BlogPost']]=relationship(back_populates='author')
    comments:Mapped[List['Comment']]=relationship(back_populates='author')

class Comment(db.Model):
    __tablename__='comments'
    id:Mapped[int]=mapped_column(Integer, primary_key=True)
    text:Mapped[str]=mapped_column(String(1000),nullable=False)
    author:Mapped['User']=relationship(back_populates='comments')
    author_id:Mapped[int]=mapped_column(Integer, db.ForeignKey('users.id'))
    parent_post:Mapped['BlogPost']=relationship(back_populates='comments')
    post_id:Mapped[str]=mapped_column(Integer, db.ForeignKey('blog_posts.id'))

with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET','POST'])
def register():
    form=RegisterForm()
    if request.method=='GET':
        return render_template("register.html",form=form,logged_in=current_user.is_authenticated)
    elif request.method=='POST':
        email=form.email.data
        user=db.session.execute(db.select(User).where(User.email==email)).scalar()
        if user!= None:
            flash('This email already taken')
            return redirect(url_for('login'))
        new_user=User(
            name=form.name.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data,method='pbkdf2:sha256',salt_length=8)
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('get_all_posts'))

@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if request.method=='GET':
        return render_template("login.html", form=form,logged_in=current_user.is_authenticated)
    elif request.method=='POST':
        email=form.email.data
        user=db.session.execute(db.select(User).where(User.email==email)).scalar()
        if user==None:
            flash('No such email in register')
            return redirect(url_for('register'))   
        else:
            password=form.password.data
            if check_password_hash(user.password,password):
                login_user(user)
                return redirect(url_for('get_all_posts'))
            else:
                flash('Wrong password')
                return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))

@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts,logged_in=current_user.is_authenticated)

@app.route("/post/<int:post_id>", methods=['GET','POST'])
def show_post(post_id):
    form=CommentForm()
    requested_post = db.get_or_404(BlogPost, post_id)
    if request.method=='GET':
        return render_template("post.html", form=form, post=requested_post,logged_in=current_user.is_authenticated)
    if request.method=="POST":
        if current_user.is_authenticated:
            new_coment=Comment(
                text=form.comment.data,
                author=current_user,
                parent_post=requested_post
            )
            db.session.add(new_coment)
            db.session.commit()
            return redirect(url_for('show_post', post_id=post_id))

@app.route('/new-post',methods=['GET','POST'])
@admin_acces
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form,logged_in=current_user.is_authenticated)

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_acces
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True,logged_in=current_user.is_authenticated)

@app.route("/delete/<int:post_id>")
@admin_acces
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

@app.route("/about")
def about():
    return render_template("about.html",logged_in=current_user.is_authenticated)

@app.route("/contact")
def contact():
    return render_template("contact.html",logged_in=current_user.is_authenticated)

if __name__ == "__main__":
    app.run(debug=True, port=5002)