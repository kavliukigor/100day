from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
login_manager=LoginManager()
login_manager.init_app(app)
db.init_app(app)

class User(db.Model,UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template("register.html")
    elif request.method=='POST':
        email=request.form['email']
        user=user=db.session.execute(db.select(User).where(User.email==email)).scalar()
        if user!= None:
            flash('This email already taken')
            return redirect(url_for('login'))
        new_user=User(
            email=request.form['email'],
            password=generate_password_hash(request.form['password'],method='pbkdf2:sha256',salt_length=8),
            name=request.form['name']
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('secrets'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template("login.html")
    if request.method=='POST':
        email=request.form['email']
        user=db.session.execute(db.select(User).where(User.email==email)).scalar()
        if user is None:
            flash('No same email in base')
            return redirect(url_for('login'))
        password=request.form['password']
        if check_password_hash(user.password,password):
            login_user(user)
            flash('You logined succesfully')
            return redirect(url_for('secrets'))
        else:
            flash('Incorect password')
            return redirect(url_for('login'))

@app.route('/secrets')
@login_required
def secrets():
    name=current_user.name.capitalize()
    return render_template("secrets.html",name=name)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download')
@login_required
def download():
    directory=app.root_path+'/static/files'
    return send_from_directory(directory=directory, path='cheat_sheet.pdf', as_attachment=True)

@login_manager.user_loader
def load_user(user_id):
    user=db.get_or_404(User,user_id)
    return user

if __name__ == "__main__":
    app.run(debug=True, port=5000)