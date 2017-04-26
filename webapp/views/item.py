# -*- coding: UTF-8 -*-
from flask import render_template
from webapp import app
from auth.login_required import login_required

__author__ = 'sonnyhcl'


@app.route('/item', methods=['GET'])
@login_required
def item():
    return render_template('', role='root')


@app.route('/item/<int:cid>/page/', methods=['POST'])
@login_required
def show_item(cid):
    """
    next=1 or prev=1 or page=?
    :param cid:
    :return:
    """
    return "show_item"


@app.route('/item/<int:cid>/add', methods=['POST'])
@login_required
def add_item(cid):
    return "add_item"


@app.route('/item/<int:cid>/modify', methods=['POST'])
@login_required
def modify_item(cid):
    return "modify_item"


@app.route('/item/<int:cid>/delete', methods=['POST'])
@login_required
def delete_item(cid):
    return "add_item"


@app.route('/item/filter', methods=['POST'])
@login_required
def filter_item():
    return "filter_item"
