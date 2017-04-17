# -*- coding: UTF-8 -*-
from flask import render_template
from webapp import app

__author__ = 'sonnyhcl'


@app.route('/community', methods=['GET'])
def community():
    return render_template('views/community.html', role='root')


@app.route('/community/page/', methods=['POST'])
def show_community():
    """
    next=1 or prev=1 or page=?
    :param :
    :return:
    """
    return "show_community"


@app.route('/community/add', methods=['POST'])
def add_community():
    return "add_community"


@app.route('/community/modify', methods=['POST'])
def modify_community():
    return "modify_community"


@app.route('/community/delete', methods=['POST'])
def delete_community():
    return "add_community"


