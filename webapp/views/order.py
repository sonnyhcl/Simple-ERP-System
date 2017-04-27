# -*- coding: UTF-8 -*-
import json
from flask import render_template
from webapp import app
from auth.login_required import login_required

__author__ = 'sonnyhcl'


@app.route('/order', methods=['GET'])
@login_required
def order():
    return render_template('order.html')


@app.route('/order/table', methods=['POST'])
@login_required
def get_orders_by_cid():
    """
    返回社区c_id拥有的订单信息
    如果cid=0则返回所有订单信息
    :return: {"data": [], "status": 'Success', "msg": ""}
    """
    ret = {"data": [], "status": 'Success', "msg": ""}
    # TODO status, info = orders.get_orders_by_cid()
    ret['data'] = [
        {'o_id': 1, 'p_name': '产品A', 'o_amount': 10, 'o_money': 1000,
         'o_note': '无'},
        {'o_id': 2, 'p_name': '产品B', 'o_amount': 20, 'o_money': 20000,
         'o_note': '无'},
    ]
    return json.dumps(ret)


@app.route('/order/add', methods=['POST'])
@login_required
def add_order_for_cid():
    """
    为社区c_id添加一个订单
    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = orders.add_order(o_amount, o_money, p_id)
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)


@app.route('/order/modify', methods=['POST'])
@login_required
def modify_order():
    """
    修改社区c_id的订单
    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = orders.modify_order(o_amount, o_money, p_id)
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)


@app.route('/order/delete', methods=['POST'])
@login_required
def delete_order():
    """
    删除社区c_id的订单
    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = orders.delete_order(i_id)
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)
