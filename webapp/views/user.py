# -*- coding: UTF-8 -*-
"""
用户管理页面相关操作
"""
import json
from flask import render_template, session, request
from webapp import app
from db.db_user import *
from db.db_community import *
from auth.login_required import login_required

__author__ = 'sonnyhcl'


@app.route('/user', methods=['GET'])
@login_required
def user_index():
    return render_template('user.html')


@app.route('/user/<int:u_id>', methods=['POST'])
@login_required
def get_user_by_uid(u_id):
    """
    根据u_id获取用户信息
    :param u_id: 
    :return: {"data": [{'u_id': info[0][0], 'u_name': info[0][1],
                       "u_role": info[0][2], "u_phone": info[0][4],
                       'c_id': info[0][5] }], "status": status, "msg":""}
    """
    status, info = user.get_user_by_uid(u_id)
    ret = {"data": [], "status": status, "msg": ""}
    if status == "Success":
        ret['data'] = {'u_id': info[0][0], 'u_name': info[0][1],
                       "u_role": info[0][2], "u_phone": info[0][4],
                       'c_id': info[0][5]}
    else:
        ret['msg'] = info
    return json.dumps(ret, ensure_ascii=False)


@app.route('/user/table', methods=['POST'])
@login_required
def get_users_by_cid():
    """
    人员管理页面
    cid=0意味着查询所有社区的人员信息，否则就是返回该c_id社区的人员信息
    :return: {"data": [{'u_id':i[0], 'u_name':i[1], "u_role":i[2],
              "u_phone": i[4], 'c_id': i[5] }], "status": status, "msg": ""}
    """
    cid = session['c_id']
    status, info = user.get_user_by_cid(cid)
    ret = {"data": [], "status": status, "msg": ""}
    d = {'root': u"主管理员", 'admin': u"管理员", 'user': u"员工"}
    if status == "Success":
        _ = [ret['data'].append({'u_id': i[0], 'u_name': i[1], "u_role": i[2],
                                 "u_phone": i[4], 'c_id': i[5]}) for i in info]
        for r in ret['data']:
            r['c_name'] = community.get_community_by_cid(r['c_id'])[1][0][1]
            r['u_role'] = d[r['u_role']]
    else:
        ret['msg'] = info
    return json.dumps(ret, ensure_ascii=False)


@app.route('/user/add', methods=['POST'])
@login_required
def add_user():
    """
    添加用户{u_name, u_phone, u_role, c_id} 默认密码为'123456'
    :return: {"status": "Success", "msg":"error_msg"}
    """
    u_name = request.form.get("u_name")
    u_phone = request.form.get("u_phone")
    u_role = request.form.get("u_role")
    c_id = request.form.get("c_id")
    u_password = '123456'
    status = user.add_user(u_name, u_role, u_password, u_phone, c_id)
    return json.dumps(status)


@app.route('/user/modify', methods=['POST'])
@login_required
def modify_user():
    """

    :param cid:
    :return: {"status": "Success", "msg":"error_msg"}
    """

    u_name = request.form.get("u_name")
    u_phone = request.form.get("u_phone")
    u_role = request.form.get("u_role")
    c_id = request.form.get("c_id")
    u_id = request.form.get("u_id")
    status = user.update_user(u_id=u_id, u_name=u_name, u_role=u_role,
                              u_phone=u_phone, c_id=c_id)
    return json.dumps(status)


@app.route('/user/delete', methods=['POST'])
@login_required
def delete_user():
    """
    删除用户
    :return: {"status": "Success", "msg":"error_msg"}
    """
    u_id = request.form.get('u_id')
    if u_id == session['u_id']:
        return "Fail"
    status = user.delete_user(u_id)
    return json.dumps(status)
