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

    u_id = request.form.get('u_id')
    status, info = transaction.get_transaction_by_uid(u_id)
    if status == "Success":
        _ = [ret['data'].append(
            {'t_id': i[0], 't_amount': i[1], 't_timestamp': i[2],
             't_note': i[3], 'm_id': i[5], 'm_amount': i[6], 'm_note': i[7],
             'o_id': i[11], 'o_amount': i[12], 'o_money': i[13],
             'o_timestamp': i[14], 'o_note': i[15], 'p_id': i[16],
             'p_name': i[19], 'p_author': i[20], 'u_name': i[22],
             'u_role': i[23], 'c_name': i[28], 'i_name': i[31], 'i_note': i[34],
             'i_unit_price': i[32]
             }) for i in info]
    else:
        ret['msg'] = info

    return json.dumps(ret, ensure_ascii=False)


@app.route('/transaction/get_cid_table', methods=['POST'])
def get_transaction_by_cid():
    """
    根据cid显示该社区所有人员的流水信息
    cid=0意味着返回所有社区的所有流水信息
    :return: 
    """
    ret = {"data": [], "status": 'Success', "msg": ""}

    c_id = request.form.get('c_id')
    status, info = transaction.get_transactions_by_cid(c_id)
    if status == "Success":
        # TODO 前端数据不够再加
        _ = [ret['data'].append(
            {'t_id': i[0], 't_amount': i[1], 't_timestamp': i[2],
             't_note': i[3], 'm_id': i[5], 'm_amount': i[6], 'm_note': i[7],
             'o_id': i[11], 'o_amount': i[12], 'o_money': i[13],
             'o_timestamp': i[14], 'o_note': i[15], 'p_id': i[16],
             'p_name': i[19], 'p_author': i[20], 'u_name': i[22],
             'u_role': i[23], 'c_name': i[28], 'i_name': i[31], 'i_note': i[34],
             'i_unit_price': i[32]
             }) for i in info]
    else:
        ret['msg'] = info
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
    t_note = request.form.get('t_note')
    ret['status'], ret['msg'] = \
        transaction.add_transactions(m_id, t_amount, t_note)

    return json.dumps(ret, ensure_ascii=False)


@app.route('/transaction/modify', methods=['POST'])
@login_required
def modify_transaction():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    ret = {"status": "Success", "msg": "error_msg"}

    t_id = request.form.get('t_id')
    m_id = request.form.get('m_id')
    t_amount = request.form.get('t_amount')
    t_note = request.form.get('t_note')
    ret['status'], ret['msg'] = \
        transaction.update_transactions(t_id, t_amount, t_note, m_id)

    return json.dumps(ret, ensure_ascii=False)


@app.route('/transaction/delete', methods=['POST'])
@login_required
def delete_transaction():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    ret = {"status": "Success", "msg": "error_msg"}

    t_id = request.form.get('t_id')
    ret['status'], ret['msg'] = transaction.delete_transactions(t_id)

    return json.dumps(ret, ensure_ascii=False)
