# -*- coding: UTF-8 -*-
"""
社区页面的路由操作
"""
import json
from flask import render_template, session, request
from webapp import app
from db.db_community import *
__author__ = 'sonnyhcl'


@app.route('/community', methods=['GET'])
def community_index():
    """
    返回社区页面
    :return: 
    """
    return render_template('community.html')


@app.route('/community/<int:c_id>', methods=['POST'])
def get_community_detail(c_id):
    """
    根据c_id返回社区的信息
    c_id=0意味着返回所有社区的信息，否则只返回该c_id社区的信息。
    :param c_id: 
    :return: {"data": [{'c_id':, 'c_name':,'u_name':,'u_phone':}], 
                "status": status, "msg":""}
    """
    status, info = community.get_community_detail(c_id)
    ret = {"data": [], "status": status, "msg":""}
    if status == "Success":
        _ = [ret['data'].append({'c_id':i[0], 'c_name':i[1],
                                 'u_name': i[2],'u_phone': i[3]}) for i in info]
    else:
        ret['msg'] = info
    return json.dumps(ret, ensure_ascii=False)


@app.route('/community/get_all_admin', methods=['POST'])
def get_all_admin():
    """
    返回所有权限为admin & root的人的信息
    
    :return: {"data": [{'u_id':, 'u_name':}], 
                "status": status, "msg":""}
    """
    # TODO 返回所有admin以及root权限的人的{u_id, u_name}
    response = {'data': [{'u_id':0, 'u_name':'hcl'},
                     {'u_id':1, 'u_name':'Alice'}],
                'status': 'Success', 'msg': "error_msg" }
    return json.dumps(response, ensure_ascii=False)



@app.route('/community/add', methods=['POST'])
def add_community():
    """
    根据传入的{c_name, u_id}添加一个社区信息
    :return: {"status": "Success", "msg":"error_msg"}
    """
    c_name = request.form.get('c_name')
    u_id = request.form.get('u_id')
    # TODO 添加一个社区
    status = community.add_community(c_name)
    return json.dumps({"status": status, "msg":"error_msg"})


@app.route('/community/modify', methods=['POST'])
def modify_community():
    """
    根据传入的{c_name, c_id, u_id}修改一个社区信息
    :return: {"status": "Success", "msg":"error_msg"}
    """
    c_name = request.form.get('c_name')
    c_id = request.form.get('c_id')
    u_id = request.form.get('u_id')
    status = community.update_community(c_id=c_id, new_c_name=c_name, u_id=u_id)
    return json.dumps({"status": status, "msg":"error_msg"})


@app.route('/community/delete', methods=['POST'])
def delete_community():
    """
    根据传入的{c_name}删除一个社区信息
    :return: {"status": "Success", "msg":"error_msg"}
    """
    c_id = request.form.get('c_id')
    status = community.delete_community(c_id)
    return json.dumps({"status": status, "msg":"error_msg"})


