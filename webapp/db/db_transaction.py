# -*- coding: UTF-8 -*-
"""
流水页面所有数据库的操作
"""
__author__ = 'sonnyhcl'
import traceback
import sqlite3


class Transactions(object):
    """
    流水信息表
    """

    # def __init__(self) :
    #     self.__counter = 0
    def add_transactions(self, u_id, c_id, p_id, i_id, amount=0):
        conn = sqlite3.connect("demo.db");
        param = (None, u_id, c_id, p_id, i_id, amount,)
        try:
            conn.execute(
                'INSERT INTO transactions(t_id, u_id, c_id, p_id, i_id, amount) VALUES (?, ?, ?, ?, ?, ?);',
                param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success"

    def delete_transactions(self, t_id):
        conn = sqlite3.connect("demo.db");

        param = (t_id,)
        try:
            conn.execute('DELETE FROM transactions WHERE t_id = ?;', param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success"

    def update_transactions(self, t_id, u_id=None, c_id=None, p_id=None,
                            i_id=None):
        conn = sqlite3.connect("demo.db");

        param = (t_id,)
        try:
            response = conn.execute('SELECT * FROM transactions WHERE t_id = ?;',
                                    param)
            origin = response.fetchall()[0]
            origin = list(origin)
            if u_id is not None:
                origin[1] = u_id
            if c_id is not None:
                origin[2] = c_id
            if p_id is not None:
                origin[3] = p_id
            if i_id is not None:
                origin[4] = i_id

            param = tuple(origin) + (t_id,)
            conn.execute(
                'UPDATE transactions SET t_id = ?, u_id =  ?, c_id =  ?, p_id =  ?, i_id = ? WHERE t_id = ?;',
                param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success"

    def get_transactions(self, t_id):
        conn = sqlite3.connect("demo.db");

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
        conn = sqlite3.connect("demo.db");

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
        conn = sqlite3.connect("demo.db");

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
        conn = sqlite3.connect("demo.db");
        try:
            response = conn.execute('SELECT * FROM transactions;')
            response = response.fetchall()
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.close()
        return "Success", response
