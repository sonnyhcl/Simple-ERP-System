# -*- coding: UTF-8 -*-
import os
from flask import render_template, request, session, \
    url_for, redirect, make_response
from auth.login_required import login_required
from webapp import app
from db.db_user import *
from webapp.mylog import log
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
    session['username'] = 'guest'
    session['role'] = 'guest'
    session['c_id'] = -1
    return redirect('index')


def validate_user(u_name, u_password):
    """
    验证(u_name, u_password)
    :param u_name:
    :param u_password:
    :return: bool
    """
    if not u_name or not u_password:
        return False
    user = User()
    status, response = user.get_validate_info()
    if not status:
        return False
    if (u_name, u_password) in response.fetchall():
        return True
    return False


@app.route('/log_in', methods=['POST'])
def log_in():
    u_name = request.form.get('username', None)
    u_password = request.form.get('password', None)
    next_url = request.form.get('next', url_for('index'))
    if next_url in ('log_out', '/log_out', url_for('log_out')):
        next_url = url_for('index')
    if validate_user(u_name, u_password):
        # TODO 下一步把跟前端交互cid的参数都删除了
        session['logged_in'] = True
        session['username'] = u_name
        session['c_id'] = 1
        session['role'] = 'root'
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
    log('next: ' + next_url)
    return render_template('login.html', error=error_msg, next=next_url)


@app.route('/error')
@login_required
def error():
    return render_template('error.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@app.route('/show_web_log', methods=['GET'])
def show_flask_log():
    log_dir = os.path.join(app.config['PROJECT_PATH'], "logs")
    log_file = os.path.join(log_dir, "webapp.log")
    resp = make_response(open(log_file).read())
    resp.headers["Content-type"] = "application/txt:charset=UTF-8"
    return resp


@app.route('/show_db_log', methods=['GET'])
def show_log():
    log_dir = os.path.join(app.config['PROJECT_PATH'], "logs")
    log_file = os.path.join(log_dir, "db_operator.log")
    resp = make_response(open(log_file).read())
    resp.headers["Content-type"] = "application/txt:charset=UTF-8"
    return resp
