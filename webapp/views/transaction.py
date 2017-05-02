# -*- coding: UTF-8 -*-
import json
from flask import render_template, request
from webapp import app
from auth.login_required import login_required
from db.db_transaction import transaction
__author__ = 'sonnyhcl'


@app.route('/transaction', methods=['GET'])
@login_required
def transaction_index():
    return render_template('transaction.html')


@app.route('/transaction/table', methods=['POST'])
@login_required
def get_transaction_by_uid():
    """
    显示该uid人员的所有流水信息
    :return: 
    """
    ret = {"data": [], "status": 'Success', "msg": ""}

    ret['data'] = [
        {'o_timestamp': '2017-04-25 11:38:35', 'o_id': 1, 'c_name': '社区A',
         'p_name': "产品A", 'i_name': '产品A的工艺1', 'i_note': '无',
         'm_amount': 10, 'i_unit_price': 100,
         't_timestamp': '2017-04-25 11:38:35', 'u_name': 'hcl', 't_note': '无'}
    ]
    # u_id = request.form.get('u_id')
    # status, info = transaction.get_transaction_by_uid(u_id)
    # if status == "Success":
    #       _ = [ret['data'].append({}) for i in info]
    # else:
    #       ret['msg'] = info

    return json.dumps(ret, ensure_ascii=False)


@app.route('/transaction/get_cid_table', methods=['POST'])
def get_transaction_by_cid():
    """
    根据cid显示该社区所有人员的流水信息
    cid=0意味着返回所有社区的所有流水信息
    :return: 
    """
    ret = {"data": [], "status": 'Success', "msg": ""}

    ret['data'] = [
        {'o_timestamp': '2017-04-25 11:38:35', 'o_id': 1, 'c_name': '社区A',
         'p_name': "产品A", 'i_name': '产品A的工艺1', 'i_note': '无',
         'm_amount': 10, 'i_unit_price': 100,
         't_timestamp': '2017-04-25 11:38:35', 'u_name': 'hcl', 't_note': '无'}
    ]
    # c_id = request.form.get('c_id')
    # status, info = transaction.get_transaction_by_cid(c_id)
    # if status == "Success":
    #       _ = [ret['data'].append({}) for i in info]
    # else:
    #       ret['msg'] = info

    return json.dumps(ret, ensure_ascii=False)


@app.route('/transaction/add', methods=['POST'])
@login_required
def add_transaction():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    ret = {"status": "Success", "msg": "error_msg"}
    m_id = request.form.get('m_id')
    t_amount = request.form.get('t_amount')
    ret['status'], ret['msg'] = transaction.add_transaction(m_id, t_amount)

    return json.dumps(ret, ensure_ascii=False)


@app.route('/transaction/modify', methods=['POST'])
@login_required
def modify_transaction():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = transactions.modify_transaction(u_name, i_name, m_amount)
    ret = {"status": "Success", "msg": "error_msg"}

    t_id = request.form.get('t_id')
    m_id = request.form.get('m_id')
    t_amount = request.form.get('t_amount')
    t_note = request.form.get('t_note')
    ret['status'], ret['msg'] = transaction.update_transaction(t_id, m_id, t_amount, t_note)

    return json.dumps(ret, ensure_ascii=False)


@app.route('/transaction/delete', methods=['POST'])
@login_required
def delete_transaction():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = transactions.delete_transaction(m_id)
    ret = {"status": "Success", "msg": "error_msg"}

    t_id = request.form.get('t_id')
    ret['status'], ret['msg'] = transaction.delete_transactions(t_id)

    return json.dumps(ret, ensure_ascii=False)
