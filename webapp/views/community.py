# -*- coding: UTF-8 -*-
import json
from flask import render_template
from webapp import app
from db.db_community import *
__author__ = 'sonnyhcl'


@app.route('/community', methods=['GET'])
def community_index():
    return render_template('views/community.html', role='root')


@app.route('/community/<int:c_id>', methods=['POST'])
def get_community(c_id):
    status, info = community.get_community(c_id)
    ret = {"data": [], "status": status, "msg":""}
    if status == "Success":
        _ = [ret['data'].append({'c_id':i[0],
                                 'c_name':i[1]}) for i in info]
    else:
        ret['msg'] = info
    return json.dumps(ret, ensure_ascii=False)

@app.route('/community/page/', methods=['POST'])
def show_community():
    """
    next=1 or prev=1 or page=?
    :param :
    :return:
    """
    return "show_community"


@app.route('/community/add', methods=['POST'])
def add_community():
    return "add_community"


@app.route('/community/modify', methods=['POST'])
def modify_community():
    return "modify_community"


@app.route('/community/delete', methods=['POST'])
def delete_community():
    return "add_community"


