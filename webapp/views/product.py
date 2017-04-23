# -*- coding: UTF-8 -*-
from flask import render_template
from webapp import app

__author__ = 'sonnyhcl'


@app.route('/product', methods=['GET'])
def product():
    return render_template('product.html', role='root')


@app.route('/product/<int:cid>/page/', methods=['POST'])
def show_product(cid):
    """
    next=1 or prev=1 or page=?
    :param cid:
    :return:
    """
    return "show_product"


@app.route('/product/<int:cid>/add', methods=['POST'])
def add_product(cid):
    return "add_product"


@app.route('/product/<int:cid>/modify', methods=['POST'])
def modify_product(cid):
    return "modify_product"


@app.route('/product/<int:cid>/delete', methods=['POST'])
def delete_product(cid):
    return "add_product"


@app.route('/product/filter', methods=['POST'])
def filter_product():
    return "filter_product"
