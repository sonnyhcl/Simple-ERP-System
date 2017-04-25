# -*- coding: UTF-8 -*-
import json
from flask import render_template
from webapp import app

__author__ = 'sonnyhcl'


@app.route('/order/test', methods=['POST'])
def dsdaddd():
    return json.dumps("ddadad")


@app.route('/order', methods=['GET'])
def order():
    return render_template('order.html')


@app.route('/order/<int:cid>/page/', methods=['POST'])
def show_order(cid):
    """
    next=1 or prev=1 or page=?
    :param cid:
    :return:
    """
    return "show_order"


@app.route('/order/<int:cid>/add', methods=['POST'])
def add_order(cid):
    return "add_order"


@app.route('/order/<int:cid>/modify', methods=['POST'])
def modify_order(cid):
    return "modify_order"


@app.route('/order/<int:cid>/delete', methods=['POST'])
def delete_order(cid):
    return "add_order"


@app.route('/order/filter', methods=['POST'])
def filter_order():
    return "filter_order"
