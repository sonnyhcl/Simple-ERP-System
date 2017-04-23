# -*- coding: UTF-8 -*-
from flask import render_template
from webapp import app

__author__ = 'sonnyhcl'


@app.route('/transaction', methods=['GET'])
def transaction():
    return render_template('transaction.html')


@app.route('/transaction/<int:cid>/page/', methods=['POST'])
def show_transaction(cid):
    """
    next=1 or prev=1 or page=?
    :param cid:
    :return:
    """
    return "show_transaction"


@app.route('/transaction/<int:cid>/add', methods=['POST'])
def add_transaction(cid):
    return "add_transaction"


@app.route('/transaction/<int:cid>/modify', methods=['POST'])
def modify_transaction(cid):
    return "modify_transaction"


@app.route('/transaction/<int:cid>/delete', methods=['POST'])
def delete_transaction(cid):
    return "add_transaction"


@app.route('/transaction/filter', methods=['POST'])
def filter_transaction():
    return "filter_transaction"
