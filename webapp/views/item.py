# -*- coding: UTF-8 -*-
from flask import render_template
from webapp import app

__author__ = 'sonnyhcl'


@app.route('/item', methods=['GET'])
def item():
    return render_template('item.html', role='root')


@app.route('/item/<int:cid>/page/', methods=['POST'])
def show_item(cid):
    """
    next=1 or prev=1 or page=?
    :param cid:
    :return:
    """
    return "show_item"


@app.route('/item/<int:cid>/add', methods=['POST'])
def add_item(cid):
    return "add_item"


@app.route('/item/<int:cid>/modify', methods=['POST'])
def modify_item(cid):
    return "modify_item"


@app.route('/item/<int:cid>/delete', methods=['POST'])
def delete_item(cid):
    return "add_item"


@app.route('/item/filter', methods=['POST'])
def filter_item():
    return "filter_item"
