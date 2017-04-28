# -*- coding: UTF-8 -*-
"""
流水页面所有数据库的操作
"""
import traceback
import sqlite3

__author__ = 'sonnyhcl'


class Transactions(object):
    def add_transactions(self, m_id, amount=0):
        conn = sqlite3.connect("demo.db")
        param = (None, m_id, amount,)
        try:
            conn.execute(
                'INSERT INTO transactions(m_id, t_amount) VALUES (?, ?);',
                param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success"

    def delete_transactions(self, t_id, amount=None, timestamp=None, notes=None, m_id=None):
        conn = sqlite3.connect("demo.db")
        param = (t_id,)
        try:
            response = conn.execute('SELECT * FROM transactions WHERE t_id = ?;', param)
            origin = response.fetchall()[0]
            origin = list(origin)
            if amount is not None:
                origin[1] = amount
            if timestamp is not None:
                origin[2] = timestamp
            if notes is not None:
                origin[3] = notes
            if m_id is not None:
                origin[4] = m_id

            param = tuple(origin) + (t_id,)
            conn.execute(
                'UPDATE transactions '
                'SET t_id = ?, t_amount = ?, t_timestamp = ?, t_notes = ?, m_id = ?'
                'WHERE t_id = ?;',
                param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success", ""

    def get_transactions(self, t_id):
        conn = sqlite3.connect("demo.db")

        param = (t_id,)
        try:
            response = conn.execute('SELECT * FROM transactions WHERE t_id = ?;',
                                    param)
            response = response.fetchall()
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.close()
        return "Success", response

    def get_transactions_by_cid(self, c_id):
        conn = sqlite3.connect("demo.db")

        param = (c_id,)
        try:
            response = conn.execute('SELECT * FROM transactions WHERE c_id = ?;',
                                    param)
            response = response.fetchall()
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.close()
        return "Success", response

    def get_transactions_by_uid(self, u_id):
        conn = sqlite3.connect("demo.db")

        param = (u_id,)
        try:
            response = conn.execute('SELECT * FROM transactions WHERE u_id = ?;',
                                    param)
            response = response.fetchall()
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.close()
        return "Success", response

    def get_all(self, ):
        conn = sqlite3.connect("demo.db")
        try:
            response = conn.execute('SELECT * FROM transactions;')
            response = response.fetchall()
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.close()
        return "Success", response

transaction = Transactions()