# -*- coding: UTF-8 -*-
"""
用户管理页面相关操作
"""
import json
from flask import render_template, session
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


@app.route('/user/page/', methods=['POST'])
def show_user():
    """
    :param cid:
    :return: json.dumps(info)
    """
    cid = session['c_id']
    status, info = user.get_user_by_cid(cid)
    if status == "Success":
        ret = dict()
        ret['data'] = []
        for i in info:
            tmp = dict()
            tmp['u_id'] = i[0]
            tmp['u_name'] = i[1]
            tmp['u_role'] = i[2]
            tmp['u_phone'] = i[4]
            tmp['c_id'] = i[5]
            ret['data'].append(tmp)
        # print ret
        return json.dumps(ret, ensure_ascii=False)
    else:
        return json.dumps({"data": []}, ensure_ascii=False)


@app.route('/user/add', methods=['POST'])
def add_user():
    """

    :param cid:
    :return:
    """
    print "dad"
    return "add_user"


@app.route('/user/modify', methods=['POST'])
def modify_user():
    """

    :param cid:
    :return: json.dumps(info)
    """
    print "modify"
    return "modify_user"


@app.route('/user/delete', methods=['POST'])
def delete_user():
    """

    :param cid:
    :return: json.dumps(info)
    """
    print "dadddd"
    return "add_user"
