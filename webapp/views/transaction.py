# -*- coding: UTF-8 -*-
import json
from flask import render_template
from webapp import app
from auth.login_required import login_required

__author__ = 'sonnyhcl'


@app.route('/transaction', methods=['GET'])
@login_required
def transaction():
    return render_template('transaction.html')


@app.route('/transaction/table', methods=['POST'])
@login_required
def get_transaction_by_uid():
    ret = {"data": [], "status": 'Success', "msg": ""}
    ret['data'] = [
        {'o_timestamp': '2017-04-25 11:38:35', 'o_id': 1, 'c_name': '社区A',
         'p_name': "产品A", 'i_name': '产品A的工艺1', 'i_note': '无',
         'm_amount': 10, 'i_unit_price': 100,
         't_timestamp': '2017-04-25 11:38:35', 'u_name': 'hcl', 't_note': '无'}
    ]
    return json.dumps(ret)


@app.route('/transaction/add', methods=['POST'])
@login_required
def add_transaction():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)


@app.route('/transaction/modify', methods=['POST'])
@login_required
def modify_transaction():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = transactions.modify_transaction(u_name, i_name, m_amount)
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)


@app.route('/transaction/delete', methods=['POST'])
@login_required
def delete_transaction():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = transactions.delete_transaction(m_id)
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)
