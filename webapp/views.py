from webapp import app
from flask import render_template, request
__author__ = 'sonnyhcl'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/error')
def error():
    return render_template('error.html')
