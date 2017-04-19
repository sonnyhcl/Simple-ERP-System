# -*- coding: UTF-8 -*-
from flask import render_template
import json
from webapp import app
from db import db_user
__author__ = 'sonnyhcl'


@app.route('/user', methods=['GET'])
def user():
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
    :return:
    """
    page = 1
    info = db_user.db_show_user(cid, page)
    # print json.dumps(info)
    return json.dumps(info)


@app.route('/user/<int:cid>/add', methods=['POST'])
def add_user(cid):

    return "add_user"


@app.route('/user/<int:cid>/modify', methods=['POST'])
def modify_user(cid):
    return "modify_user"


@app.route('/user/<int:cid>/delete', methods=['POST'])
def delete_user(cid):
    return "add_user"


@app.route('/user/filter', methods=['POST'])
def filter_user():
    return "filter_user"
