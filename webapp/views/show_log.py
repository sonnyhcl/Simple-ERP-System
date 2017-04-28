# -*- coding: UTF-8 -*-
import os
from flask import render_template, request, session, \
    url_for, redirect, make_response
from auth.login_required import login_required
from webapp import app
__author__ = 'sonnyhcl'


@app.route('/show_web_log', methods=['GET'])
@login_required
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
@login_required
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
