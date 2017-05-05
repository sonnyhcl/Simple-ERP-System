# -*- coding: UTF-8 -*-
import json
from flask import render_template, session, request
from auth.login_required import login_required
from auth.permission_required import permission_required
from webapp import app
from webapp.mylog import log
from db.db_mission import *

__author__ = 'sonnyhcl'


@app.route('/mission', methods=['GET'])
@permission_required('admin')
@login_required
def mission_index():
    return render_template('mission.html')


@app.route('/mission/table', methods=['POST'])
@login_required
def get_mission_by_cid():
    """
    返回社区c_id的任务信息
    c_id=0意味着返回所有任务信息
    :return: 
    """
    ret = {"data": [], "status": 'Success', "msg": ""}
    c_id = session.get('c_id')
    status, info = mission.get_mission_by_cid(c_id)
    if status == "Success":
        _ = [ret['data'].append(
            {'m_id': i[0], 'm_amount': i[1], 'm_note': i[2],
             'u_id': i[3], "i_id": i[4], "o_id": i[6], "o_amount": i[7],
             'u_name': i[23], 'p_name': i[14], 'i_name': i[17]}) for i in info]
    else:
        ret['msg'] = info

    return json.dumps(ret, ensure_ascii=False)


@app.route('/mission/add', methods=['POST'])
@login_required
def add_mission():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    ret = {"status": "Success", "msg": "error_msg"}
    u_id = request.form.get('u_id')
    i_id = request.form.get('i_id')
    o_id = request.form.get('o_id')
    m_amount = request.form.get('m_amount')
    m_note = request.form.get('m_note')
    ret['status'], ret['msg'] = \
        mission.add_mission(u_id, i_id, o_id, m_amount, m_note)

    return json.dumps(ret, ensure_ascii=False)


@app.route('/mission/modify', methods=['POST'])
@login_required
def modify_mission():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    ret = {"status": "Success", "msg": "error_msg"}

    m_id = request.form.get('m_id')
    m_amount = request.form.get('m_amount')
    m_note = request.form.get('m_note')
    u_id = request.form.get('u_id')
    i_id = request.form.get('i_id')
    o_id = request.form.get('o_id')
    ret['status'], ret['msg'] = \
        mission.update_mission(m_id, m_amount, m_note, u_id, i_id, o_id)

    return json.dumps(ret, ensure_ascii=False)


@app.route('/mission/delete', methods=['POST'])
@login_required
def delete_mission():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    ret = {"status": "Success", "msg": "error_msg"}
    m_id = request.form.get('m_id')
    ret['status'], ret['msg'] = mission.delete_mission(m_id)

    return json.dumps(ret, ensure_ascii=False)
