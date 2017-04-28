# -*- coding: UTF-8 -*-
"""
任务页面所有的数据库操作
"""
__author__ = 'sonnyhcl'
import sqlite3
import traceback
from flask import session
from webapp.mylog import log

class Mission(object) :
    def add_mission(self, u_name, i_name, m_amount):
        conn = sqlite3.connect("demo.db")
        param = (o_amount, o_money, p_id,)
        try:
            conn.execute('INSERT INTO order(o_amount, o_money, p_id)'
                         'VALUES (?, ?, ?);', param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success", ""

    def delete_mission(self, o_id):
        conn = sqlite3.connect("demo.db")
        param = (o_id,)
        try:
            conn.execute('DELETE FROM order WHERE o_id = ?;', param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success", ""

    def update_mission(self, o_id, p_id, c_id, amount):
        pass

    def get_mission_by_cid(self, c_id):
        conn = sqlite3.connect("demo.db")
        param = (c_id,)
        try:
            if c_id == 0:
                response = conn.execute('SELECT * FROM mission;')
            else:
                response = conn.execute('SELECT * FROM mission '
                                        'WHERE u_id IN '
                                        '(SELECT u_id FROM user '
                                        'WHERE c_id = ?);', param)
            response = response.fetchall()
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()

        conn.close()
        return "Success", response