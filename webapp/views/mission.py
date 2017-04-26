# -*- coding: UTF-8 -*-
import json
from flask import render_template, session, request
from webapp import app
from db.db_community import *
from auth.login_required import login_required

__author__ = 'sonnyhcl'

@app.route('/mission', methods=['GET'])
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
    # TODO status, info = mission.get_mission_by_cid()
    ret['data'] = [
        {'o_id': 1, 'p_name': "产品A", 'i_name': '产品A的工艺1',
         'u_name': 'hcl', 'm_amount': 10, 'm_note': '无'},
        {'o_id': 2, 'p_name': "产品A", 'i_name': '产品A的工艺2',
         'u_name': 'hcl', 'm_amount': 20, 'm_note': '无'},
        {'o_id': 3, 'p_name': "产品B", 'i_name': '产品B的工艺1',
         'u_name': 'hcl', 'm_amount': 30, 'm_note': '无'},
        {'o_id': 4, 'p_name': "产品B", 'i_name': '产品B的工艺2',
         'u_name': 'hcl', 'm_amount': 40, 'm_note': '无'},
    ]
    return json.dumps(ret)


@app.route('/mission/add', methods=['POST'])
@login_required
def add_mission():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = missions.add_mission(u_name, i_name, m_amount)
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)


@app.route('/mission/modify', methods=['POST'])
@login_required
def modify_mission():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = missions.modify_mission(u_name, i_name, m_amount)
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)


@app.route('/mission/delete', methods=['POST'])
@login_required
def delete_mission():
    """

    :return: {"status": "Success", "msg":"error_msg"}
    """
    # TODO status, info = missions.delete_mission(m_id)
    info = {"status": "Success", "msg": "error_msg"}
    return json.dumps(info, ensure_ascii=False)

