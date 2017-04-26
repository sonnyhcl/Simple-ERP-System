# -*- coding: UTF-8 -*-
"""
首页所有数据库相关的操作
"""

import sqlite3
from flask import session
from webapp.mylog import log
__author__ = 'sonnyhcl'


class Index(object):

    def get_index_info_by_uid(self, u_id):
        """
        在首页上需要显示username, user_role, community_name, user_phone, 
        :return: 
        """
        # TODO 返回格式status, msg = ..... 以及异常处理
        conn = sqlite3.connect("demo.db")
        param = (u_id, )
        response = conn.execute('SELECT u_name, u_role, c_name, u_phone '
                                'FROM user, community '
                                'WHERE user.u_id = ? '
                                'and community.c_id = user.c_id',
                                param)
        response = response.fetchall()
        conn.commit()
        conn.close()
        return "Success", response

index = Index()