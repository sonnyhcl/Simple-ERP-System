# -*- coding: UTF-8 -*-
"""
首页、登录相关操作以及其它杂七杂八的操作
"""
from flask import render_template, request, session, \
    url_for, redirect, make_response
from auth.login_required import login_required
from webapp import app
from db.db_index import *
from webapp.mylog import log

__author__ = 'sonnyhcl'


@app.route('/')
def index_():
    return redirect('index')


@app.route('/index')
@login_required
def index_index():
    """
    返回首页
    :return:
    """
    d = {'root': u"主管理员", 'admin': u"社区管理员", 'user': u"员工"}
    status, info = index.get_index_info_by_uid(session['u_id'])
    print info
    user_info = {'u_name': 'error', 'u_role': 'user',
                 'c_name': 'error', 'u_phone': 'error'}
    if status == 'Success':
        user_info = {'u_name': info[0][0], 'u_role': d[info[0][1]],
                     'c_name': info[0][2], 'u_phone': info[0][3]}

    return render_template('index.html', user_info=user_info)


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
