# -*- coding: UTF-8 -*-
"""
首页、登录相关操作以及其它杂七杂八的操作
"""
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
    """
    返回首页
    :return:
    """
    return render_template('views/index.html')


@app.route('/log_out', methods=['GET'])
def log_out():
    """
    登出，立刻跳转到首页(此时会被重定向到登录页面)
    :return:
    """
    log(session['u_name'] + "log_out")
    session['logged_in'] = False
    session['u_name'] = 'guest'
    session['u_role'] = 'guest'
    session['c_id'] = -1
    session['u_id'] = -1
    return redirect('index')


def validate_user(u_name, u_password):
    """
    验证(u_name, u_password)
    :param u_name:
    :param u_password:
    :return: True, [user_info] or False, ""
    """
    log("validate_user" + u_name)
    if not u_name or not u_password:
        return False, ""
    status, info = user.get_all_user()
    if not status:
        return False, "guest"

    for i in info:
        if (u_name, u_password) == (i[1], i[3]):
            return True, i

    return False, "guest"


@app.route('/log_in', methods=['POST'])
def log_in():
    u_name = request.form.get('username', None)
    u_password = request.form.get('password', None)
    next_url = request.form.get('next', url_for('index'))
    if next_url in ('log_out', '/log_out', url_for('log_out')):
        next_url = url_for('index')
    status, info = validate_user(u_name, u_password)
    if status:
        # TODO 下一步把跟前端交互cid的参数都删除了
        session['logged_in'] = True
        session['u_id'] = info[0]
        session['u_name'] = info[1]
        session['u_role'] = info[2]
        session['c_id'] = info[5]
        return redirect(next_url)

    error_msg = "wrong username or password"
    return render_template('login.html', error=error_msg, next=next_url)


@app.route('/login', methods=['GET'])
def login():
    """
    返回登录页面
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
    """
    默认的error界面
    :return: templates
    """
    return render_template('error.html')


@app.errorhandler(404)
def not_found(e):
    """
    默认的404 not found页面
    :param e:
    :return: templates
    """
    return render_template('404.html'), 404


@app.route('/show_web_log', methods=['GET'])
def show_web_log():
    """
    给运维预留的日志接口
    :return: txt
    """
    log_dir = os.path.join(app.config['PROJECT_PATH'], "logs")
    log_file = os.path.join(log_dir, "webapp.log")
    resp = make_response(open(log_file).read())
    resp.headers["Content-type"] = "application/txt:charset=UTF-8"
    return resp


@app.route('/show_db_log', methods=['GET'])
def show_db_log():
    """
    给超管预留的数据库操作流水接口
    :return: txt
    """
    log_dir = os.path.join(app.config['PROJECT_PATH'], "logs")
    log_file = os.path.join(log_dir, "db_operator.log")
    resp = make_response(open(log_file).read())
    resp.headers["Content-type"] = "application/txt:charset=UTF-8"
    return resp
