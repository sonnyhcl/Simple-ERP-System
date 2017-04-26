# -*- coding: UTF-8 -*-
import json
from flask import render_template
from webapp import app

__author__ = 'sonnyhcl'


@app.route('/order', methods=['GET'])
def order():
    return render_template('order.html')


@app.route('/order/table', methods=['POST'])
def get_all_orders():
    """
    获取所有订单信息
    :return: 
    """
    ret = {"data": [], "status": 'Success', "msg": ""}
    # TODO status, info = orders.get_all_orders()
    ret['data'] = [
        {'o_id': 1, 'p_name': '产品A', 'o_amount': 10, 'o_money': 1000,
         'o_note': '无'},
        {'o_id': 2, 'p_name': '产品B', 'o_amount': 20, 'o_money': 20000,
         'o_note': '无'},
    ]
    return json.dumps(ret)


@app.route('/order/add', methods=['POST'])
def add_order():
    """
    
    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = orders.add_order(o_amount, o_money, p_id)
    info = {"status": "Success", "msg":"error_msg"}
    return json.dumps(info, ensure_ascii=False)


@app.route('/order/modify', methods=['POST'])
def modify_order():
    """
    
    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = orders.modify_order(o_amount, o_money, p_id)
    info = {"status": "Success", "msg":"error_msg"}
    return json.dumps(info, ensure_ascii=False)


@app.route('/order/delete', methods=['POST'])
def delete_order():
    """
    
    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = orders.delete_order(i_id)
    info = {"status": "Success", "msg":"error_msg"}
    return json.dumps(info, ensure_ascii=False)

