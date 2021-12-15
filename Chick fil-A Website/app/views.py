from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/order')
def order():
    return render_template("order.html")

@app.route('/about')
def about():
    return render_template("about.html")
    
@app.route('/signin')
def signin():
    return render_template("signin.html")
@app.route('/contact')
def contact():
    return render_template("contact1.html")
