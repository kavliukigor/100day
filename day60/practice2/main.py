from flask import Flask, render_template, request
import requests 
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

email=os.getenv('my_email')
password=os.getenv('password')
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method=="GET":
        return render_template("contact.html", msg_sent=False)
    elif request.method=='POST':
        with smtplib.SMTP('smtp.gmail.com')as connection:
                connection.starttls()
                connection.login(user='kavliukigor@gmail.com',password=password)
                connection.sendmail(
                    from_addr='igor2018kavl@gmail.com',
                    to_addrs=request.form['eamil'],
                    msg=f'Subject: Your letter!\n\nName: {request.form['name']}\nEmail: {request.form['email']}\nPhone: {request.form['phone']}\nMessge: {request.form['message']}'
                    )        
        return render_template("contact.html", msg_sent=True)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

app.run(debug=True)