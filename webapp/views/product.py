# -*- coding: UTF-8 -*-
import json
from flask import render_template
from webapp import app

__author__ = 'sonnyhcl'


@app.route('/product', methods=['GET'])
def product():
    return render_template('product.html')


@app.route('/product/table', methods=['POST'])
def get_all_products_detail():
    # TODO status, info = products.get_all_products_detail()
    return json.dumps("ddadad")


@app.route('/product/add', methods=['POST'])
def add_product():
    """
    这里需要添加多个工艺，所以item是个数组
    :return: {"status": "Success", "msg":"error_msg"}
    """
    # item = [{i_name, i_unit_price, i_ref_time},...]
    # TODO status, info = products.add_product(p_name, p_author_name, item)
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)


@app.route('/product/modify', methods=['POST'])
def modify_product():
    """
    需要判断是否增加了工艺或者删除了工艺，同时更新产品表和工艺表
    :return: {"status": "Success", "msg":"error_msg"}
    """
    # item = [{i_name, i_unit_price, i_ref_time},...]
    # TODO status, info = products.modify_product(p_name, p_author_name, item)
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)


@app.route('/product/delete', methods=['POST'])
def delete_product():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = products.delete_product(p_id)
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)

