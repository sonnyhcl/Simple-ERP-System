# -*- coding: UTF-8 -*-
from flask import render_template
from webapp import app
from auth.login_required import login_required
from db.db_user import *
__author__ = 'sonnyhcl'


@login_required
@app.route('/test')
def test():
    """
    该url纯供测试
    :return: 一个空白base模版
    """
    user = User()
    user.add_user(_u_id=101, _u_name='a', _u_password='b', _u_phone='c',
                  _u_role='d', _c_id=1)
    flag, response = user.get_all()
    print flag, response.fetchall()
    return render_template('test.html')
