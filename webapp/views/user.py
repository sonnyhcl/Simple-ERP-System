# -*- coding: UTF-8 -*-
from flask import render_template
from webapp import app

__author__ = 'sonnyhcl'


@app.route('/user', methods=['GET'])
def user():
    return render_template('views/user.html', role='root')


@app.route('/user/<int:cid>/page/', methods=['POST'])
def show_user(cid):
    """
    next=1 or prev=1 or page=?
    :param cid:
    :return:
    """
    return "show_user"


@app.route('/user/<int:cid>/add', methods=['POST'])
def add_user(cid):

    return "add_user"


@app.route('/user/<int:cid>/modify', methods=['POST'])
def modify_user(cid):
    return "modify_user"


@app.route('/user/<int:cid>/delete', methods=['POST'])
def delete_user(cid):
    return "add_user"


@app.route('/user/filter', methods=['POST'])
def filter_user():
    return "filter_user"
