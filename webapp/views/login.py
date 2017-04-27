# -*- coding: UTF-8 -*-
import json
from flask import render_template, request, session, \
    url_for, redirect, make_response
from webapp import app
from webapp.mylog import log
from db.db_user import *
from db.db_index import *
__author__ = 'sonnyhcl'


def validate_user(u_name, u_password):
    """
    验证(u_name, u_password)
    :param u_name:
    :param u_password:
    :return: True, [user_info] or False, ""
    """
    log("validate_user %s" % u_name)
    if not u_name or not u_password:
        return False, ""
    status, info = user.get_all_user_info()
    if not status:
        return False, "guest"

    for i in info:
        if (u_name, u_password) == (i[1], i[3]):
            return True, i

    return False, "guest"


@app.route('/log_out', methods=['GET'])
def log_out():
    """
    登出，立刻跳转到首页(此时会被重定向到登录页面)
    :return:
    """
    log("%s log_out" % (session['u_name']))
    session['logged_in'] = False
    session['u_id'] = -1
    session['u_name'] = 'guest'
    session['u_role'] = 'guest'
    session['c_id'] = -1
    return redirect('index')


@app.route('/log_in', methods=['POST'])
def log_in():
    u_name = request.form.get('username', None)
    u_password = request.form.get('password', None)
    next_url = request.form.get('next', 'index')
    if next_url in ('log_out', '/log_out', url_for('log_out')):
        next_url = url_for('index')
    status, info = validate_user(u_name, u_password)
    if status:
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
    next_url = request.args.get('next', 'index')
    return render_template('login.html', error=None, next=next_url)


@app.route('/reset_password', methods=["POST"])
def reset_password():
    ret = {}
    old_pass = request.form.get('old_password')
    new_pass = request.form.get('new_password')
    u_name = request.form.get('username')
    ret["status"], ret["msg"] = validate_user(u_name, old_pass)

    if ret["status"]:
        u_id = ret["msg"][0]
        ret["status"], ret["msg"] = \
            user.update_user(u_id, u_name=u_name, u_password=new_pass)
    else:
        ret["status"] = "False"
        ret["msg"] = "Validate Error"

    return json.dumps(ret, ensure_ascii=False)
