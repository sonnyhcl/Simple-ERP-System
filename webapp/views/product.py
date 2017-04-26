# -*- coding: UTF-8 -*-
import json
from flask import render_template
from webapp import app
from auth.login_required import login_required

__author__ = 'sonnyhcl'


@app.route('/product', methods=['GET'])
@login_required
def product():
    return render_template('product.html')


@app.route('/product/table', methods=['POST'])
@login_required
def get_all_products_detail():
    ret = {"data": [], "status": 'Success', "msg": ""}
    # TODO status, info = products.get_all_products_detail()
    ret['data'] = [
        {'p_name': '产品A', 'i_name': "产品A的工艺1",
         'i_unit_price': 10.0, 'p_author_name': '设计师A', 'i_ref_time': 100},
        {'p_name': '产品A', 'i_name': "产品A的工艺2",
         'i_unit_price': 20.0, 'p_author_name': '设计师A', 'i_ref_time': 200},
        {'p_name': '产品B', 'i_name': "产品B的工艺1",
         'i_unit_price': 30.0, 'p_author_name': '设计师A', 'i_ref_time': 300},
        {'p_name': '产品B', 'i_name': "产品B的工艺2",
         'i_unit_price': 40.0, 'p_author_name': '设计师A', 'i_ref_time': 400},
    ]
    return json.dumps(ret)


@app.route('/product/add', methods=['POST'])
@login_required
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
@login_required
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
@login_required
def delete_product():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = products.delete_product(p_id)
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)

