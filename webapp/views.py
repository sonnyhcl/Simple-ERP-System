from webapp import app
from flask import render_template
__author__ = 'sonnyhcl'


@app.route('/')
@app.route('/index')
def index():
    return "hello world"


@app.route('/login')
def login():
    return render_template('login.html')
