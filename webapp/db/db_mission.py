# -*- coding: UTF-8 -*-
"""
任务页面所有的数据库操作
"""
import sqlite3
import traceback
from flask import session
from webapp.mylog import log

__author__ = 'sonnyhcl'


class Mission(object):
    def add_mission(self, u_id, i_id, o_id, m_amount):
        conn = sqlite3.connect("demo.db")
        param = (u_id, i_id, o_id, m_amount,)
        try:
            conn.execute('INSERT INTO mission(u_id, i_id, o_id, m_amount)'
                         'VALUES (?, ?, ?, ?);', param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success", ""

    def delete_mission(self, m_id):
        conn = sqlite3.connect("demo.db")
        param = (m_id,)
        try:
            conn.execute('DELETE FROM mission WHERE m_id = ?;', param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success", ""

    def update_mission(self, m_id, amount=None, notes=None, u_id=None, i_id=None, o_id=None):
        conn = sqlite3.connect("demo.db")
        param = (m_id,)
        try:
            response = conn.execute('SELECT * FROM mission WHERE m_id = ?;', param)
            origin = response.fetchall()[0]
            origin = list(origin)
            if amount is not None:
                origin[1] = amount
            if notes is not None:
                origin[2] = notes
            if u_id is not None:
                origin[3] = u_id
            if i_id is not None:
                origin[4] = i_id
            if o_id is not None:
                origin[5] = o_id

            param = tuple(origin) + (m_id,)
            conn.execute(
                'UPDATE mission '
                'SET m_id = ?, m_amount = ?, m_notes = ?, u_id = ?, i_id = ?, o_id = ?'
                'WHERE m_id = ?;',
                param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success", ""

    def get_mission_by_cid(self, c_id):
        conn = sqlite3.connect("demo.db")
        param = (c_id,)
        try:
            if c_id == 0:
                response = conn.execute('SELECT * FROM mission;')
            else:
                response = conn.execute('SELECT * FROM mission '
                                        'WHERE o_id IN '
                                        '(SELECT o_id FROM orders '
                                        'WHERE c_id = ?);', param)
            response = response.fetchall()
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()

        conn.close()
        return "Success", response


mission = Mission()
