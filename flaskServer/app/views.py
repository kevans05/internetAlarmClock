__author__ = 'Kevans05'
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title = 'home')