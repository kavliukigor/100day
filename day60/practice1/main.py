from flask import Flask, render_template, request


app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def post_info():
    if request.method == 'POST':
        return f"<h1>{request.form['name']}  {request.form['password']}</h1>"

app.run(debug=True)