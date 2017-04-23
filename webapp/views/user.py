# -*- coding: UTF-8 -*-
"""
用户管理页面相关操作
"""
import json
from flask import render_template, session, request
from webapp import app
from db.db_user import *
__author__ = 'sonnyhcl'


@app.route('/user', methods=['GET'])
def user_index():
    """
    返回用户管理页面
    :return: templates
    """
    return render_template('views/user.html')

@app.route('/user/<int:u_id>', methods=['POST'])
def get_user(u_id):
    """
    
    :param u_id: 
    :return: 
    """
    status, info = user.get_user_by_uid(u_id)
    ret = {"data": [], "status": status, "msg":""}
    if status == "Success":
        ret['data'] = {'u_id':info[0][0], 'u_name':info[0][1], "u_role":info[0][2],
                            "u_phone": info[0][4], 'c_id': info[0][5] }
    else:
        ret['msg'] = info
    return json.dumps(ret, ensure_ascii=False)


@app.route('/user/page/', methods=['POST'])
def show_users():
    """
    :param cid:
    :return: json.dumps(info)
    """
    cid = session['c_id']
    status, info = user.get_user_by_cid(cid)
    ret = {"data": [], "status": status, "msg":""}
    if status == "Success":
        _ = [ret['data'].append({'u_id':i[0], 'u_name':i[1], "u_role":i[2],
                            "u_phone": i[4], 'c_id': i[5] })  for i in info]
    else:
        ret['msg'] = info
    return json.dumps(ret, ensure_ascii=False)


@app.route('/user/add', methods=['POST'])
def add_user():
    """

    :param cid:
    :return:
    """
    u_name = request.form.get("u_name")
    u_phone = request.form.get("u_phone")
    u_role = request.form.get("u_role")
    c_id = request.form.get("c_id")
    print request.form
    return "Success"


@app.route('/user/modify', methods=['POST'])
def modify_user():
    """

    :param cid:
    :return: json.dumps(info)
    """
    print "modify"
    return "Success"


@app.route('/user/delete', methods=['POST'])
def delete_user():
    """

    :param cid:
    :return: json.dumps(info)
    """
    u_id = request.form.get('u_id')
    if u_id == session['u_id']:
        return "Fail"
    status = user.delete_user(u_id)
    return status
