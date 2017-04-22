# -*- coding: UTF-8 -*-
"""
用户管理页面相关操作
"""
import json
from flask import render_template
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


@app.route('/user/<int:cid>/page/', methods=['POST'])
def show_user(cid):
    """
    {
        curr:<int>,
        next:<bool>,
        prev:<bool>,
        page:<int>
    }
    :param cid:
    :return: json.dumps(info)
    """
    # info = db_user.db_show_user(cid)
    if cid < 0:
        return "Fail", "没有权限"
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


@app.route('/user/<int:cid>/add', methods=['POST'])
def add_user(cid):
    """

    :param cid:
    :return:
    """
    print "dad"
    return "add_user"


@app.route('/user/<int:cid>/modify', methods=['POST'])
def modify_user(cid):
    """

    :param cid:
    :return: json.dumps(info)
    """
    print "modify"
    return "modify_user"


@app.route('/user/<int:cid>/delete', methods=['POST'])
def delete_user(cid):
    """

    :param cid:
    :return: json.dumps(info)
    """
    print "dadddd"
    return "add_user"


@app.route('/user/filter', methods=['POST'])
def filter_user(cid):
    """

    :param cid:
    :return: json.dumps(info)
    """
    return "filter_user"
