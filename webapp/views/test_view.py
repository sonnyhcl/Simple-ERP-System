# -*- coding: UTF-8 -*-
from flask import render_template
from webapp import app
from auth.login_required import login_required
from db.db_user import *
from db.db_product import *
from db.db_community import *
from db.db_item import *
from db.db_transaction import *
__author__ = 'sonnyhcl'


@login_required
@app.route('/test')
def test():
    """
    该url纯供测试
    :return: 一个空白base模版
    """
    user = User()
    flag, response = user.get_all_user()
    print flag, response
    community = Community()
    community.add_community(c_name='fuck community')
    flag = community.add_community_admin(c_id=1, u_id=2)
    print flag
    flag, response = community.get_community_detail(c_id=1)
    print flag, response
    # user = User()
    # user.add_user(u_name='a', u_password='b', u_phone='c', u_role='d', c_id=1)
    # flag, response = user.get_all_user()
    # print flag, response
    # prod = Product()
    # prod.add_product(p_name='fuck')
    # flag, response = prod.get_all()
    # item = Item()
    # item.add_item(i_name='fuck', i_minutes=1, i_prices=1, i_unitprices=1, p_id=1)
    # flag, response = item.get_all()
    # print flag, response
    #
    # transactions = Transactions()
    # transactions.add_transactions(u_id=1,c_id=1,p_id=1,i_id=1)
    # flag, response = transactions.get_all()
    # print flag, response
    return render_template('test.html')


@app.route('/task')
def task_index():
    return render_template('task.html')

@app.route('/order')
def order_index():
    return "helloworld"
