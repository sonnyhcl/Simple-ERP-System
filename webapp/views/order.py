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

    # TODO 这里要返回产品名、设计师名和社区名，而不是id
    status, info = order.get_order_by_cid(c_id)
    if ret['status'] == 'Success':
        _ = [ret['data'].append(
            {'o_id': i[0], 'o_amount': i[1], "o_money": i[2],
             "o_timestamp": i[3], "o_note": i[4], 'p_name': u"产品名",
             'p_author': u"设计者", "c_name": u"社区名"}) for i in info]
    else:
        ret['msg'] = info

    return json.dumps(ret, ensure_ascii=False)


@app.route('/order/add', methods=['POST'])
@login_required
def add_order_for_cid():
    """
    为社区c_id添加一个订单
    :return: {"status": "Success", "msg":"error_msg"}
    """

    ret = {"status": "Success", "msg": "error_msg"}
    o_amount = request.form.get('o_amount')
    o_money = 0 # request.form.get('o_money')
    p_id = request.form.get('p_id')
    c_id = request.form.get('c_id')
    ret['status'], ret['msg'] = \
        order.add_order(o_amount, p_id, c_id)

    return json.dumps(ret, ensure_ascii=False)


@app.route('/order/modify', methods=['POST'])
@login_required
def modify_order():
    """
    修改社区c_id的订单
    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO: 去掉金额
    ret = {"status": "Success", "msg": "error_msg"}
    o_id = request.form.get('o_id')
    o_amount = request.form.get('o_amount')
    o_money = 0 # request.form.get('o_money')
    p_id = request.form.get('p_id')
    c_id = request.form.get('c_id')
    ret['status'], ret['msg'] = \
        order.update_order(o_id, o_amount, o_money, p_id, c_id)

    return json.dumps(ret, ensure_ascii=False)


@app.route('/order/delete', methods=['POST'])
@login_required
def delete_order():
    """
    删除社区c_id的订单
    :return: {"status": "Success", "msg":"error_msg"}
    """
    ret = {"status": "Success", "msg": "error_msg"}
    o_id = request.form.get('o_id')
    ret['status'], ret['msg'] = order.delete_order(o_id)

    return json.dumps(ret, ensure_ascii=False)
