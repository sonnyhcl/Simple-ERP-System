# -*- coding: UTF-8 -*-
from flask import render_template, request, session, url_for, redirect
from auth.login_required import login_required
from db.db_user import *
from webapp import app

__author__ = 'sonnyhcl'


@app.route('/')
def index_():
    return redirect('index')


@app.route('/index')
@login_required
def index():
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
    # next_url = request.args.get('next') or \
    #        request.referrer or \
    #        url_for('index')

    return render_template('login.html', error=error_msg, next=next_url)


@app.route('/error')
@login_required
def error():
    return render_template('error.html')


@app.route('/test')
def test():
    # return redirect(url_for('static', filename='images/gold.png'))
    return render_template('test.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
