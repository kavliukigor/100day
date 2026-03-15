from flask import Flask, render_template
from post import Post
post=Post()
posts=post.request()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",posts=posts)

@app.route('/blog/<int:number>')
def get_blog(number):
    for post in posts:
        if post['id']==number:
            return render_template('post.html',post=post)

@app.route('/blog/about')
def about_page():
    return render_template('about.html')

@app.route('/blog/contact')
def contact_page():
    return render_template('contact.html')

app.run(debug=True)