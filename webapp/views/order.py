# -*- coding: UTF-8 -*-
import json
from flask import render_template, request
from webapp import app
from auth.login_required import login_required
from db.db_order import *

__author__ = 'sonnyhcl'


@app.route('/order', methods=['GET'])
@login_required
def order_index():
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
    c_id = request.form.get('c_id')
    print c_id
    status, info = order.get_order_by_cid(c_id)
    print info
    if ret['status'] == 'Success':
        _ = [ret['data'].append(
            {'o_id': i[0], 'o_amount': i[1], "o_money": i[2],
             "o_timestamp": i[3], "o_note": i[4], 'p_name': i[5],
             "c_name": i[6]}) for i in info]
    else:
        ret['msg'] = info
    print ret
    # ret['data'] = [
    #     {'o_id': 1, 'p_name': '产品A', 'o_amount': 10, 'o_money': 1000,
    #      'o_note': '无'},
    #     {'o_id': 2, 'p_name': '产品B', 'o_amount': 20, 'o_money': 20000,
    #      'o_note': '无'},
    # ]

    return json.dumps(ret, ensure_ascii=False)


@app.route('/order/add', methods=['POST'])
@login_required
def add_order_for_cid():
    """
    为社区c_id添加一个订单
    :return: {"status": "Success", "msg":"error_msg"}
    """
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)


@app.route('/order/modify', methods=['POST'])
@login_required
def modify_order():
    """
    修改社区c_id的订单
    :return: {"status": "Success", "msg":"error_msg"}
    """
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)


@app.route('/order/delete', methods=['POST'])
@login_required
def delete_order():
    """
    删除社区c_id的订单
    :return: {"status": "Success", "msg":"error_msg"}
    """
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)
