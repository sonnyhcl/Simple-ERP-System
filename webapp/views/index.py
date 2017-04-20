# -*- coding: UTF-8 -*-
import os
from flask import render_template, request, session, url_for, redirect, make_response
from auth.login_required import login_required
from db.db_user import *
from webapp import app
from webapp import log
__author__ = 'sonnyhcl'


@app.route('/')
def index_():
    return redirect('index')


@app.route('/index')
@login_required
def index():
    log("test")
    return render_template('views/index.html')


@app.route('/log_out', methods=['GET'])
def log_out():
    session['logged_in'] = False
    return redirect('index')


@app.route('/log_in', methods=['POST'])
def log_in():
    user_name = request.form.get('username', None)
    pass_word = request.form.get('password', None)
    next_url = request.form.get('next', url_for('index'))
    if validate_user(user_name, pass_word):
        session['logged_in'] = True
        session['username'] = user_name
        return redirect(next_url)

    error_msg = "wrong username or password"
    return render_template('login.html', error=error_msg, next=next_url)


@app.route('/login', methods=['GET'])
def login():
    """
    http://localhost:5000/login?next=http%3A%2F%2Flocalhost%3A5000%2Ferror
    :return: templates
    """
    error_msg = None
    next_url = request.args.get('next', 'index')
    print 'next: ' + next_url
    return render_template('login.html', error=error_msg, next=next_url)


@app.route('/error')
@login_required
def error():
    return render_template('error.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@app.route('/test')
def test():
    """
    TODO: to be deleted
    :return:
    """
    return render_template('test.html')


@app.route('/show_flask_log', methods=['GET'])
def show_flask_log():
    log_dir = os.path.join(app.config['PROJECT_PATH'], "logs")
    log_file = os.path.join(log_dir, "webapp.log")
    resp = make_response(open(log_file).read())
    resp.headers["Content-type"]="application/txt:charset=UTF-8"
    return resp


@app.route('/show_log', methods=['GET'])
def show_log():
    log_dir = os.path.join(app.config['PROJECT_PATH'], "logs")
    log_file = os.path.join(log_dir, "webapp.log")
    resp = make_response(open(log_file).read())
    resp.headers["Content-type"] = "application/txt:charset=UTF-8"
    return resp
