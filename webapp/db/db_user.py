# -*- coding: UTF-8 -*-
"""
数据库表中的增改删操作都要log
用户页面所有数据库相关操作
"""
import sqlite3
import traceback
from flask import session
from webapp.mylog import log


class User(object):
    def add_user(self, u_name, u_role, u_password, u_phone, c_id):
        """
        add_user
        :return: 'Success', '' or 'Fail', 'error_msg'
        """
        log("add_user: %s %s %s %s %s"
            % (u_name, u_role, u_password, u_phone, c_id))
        conn = sqlite3.connect("demo.db")
        param = (u_name, u_role, u_password, u_phone, c_id,)
        try:
            conn.execute(
                'INSERT INTO user(u_name, u_role, u_password, u_phone, c_id) '
                'VALUES (?, ?, ?, ?, ?);',
                param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success", ""

    def delete_user(self, u_id):
        """
        delete_user
        :return: 'Success', '' or 'Fail', 'error_msg'
        """
        log("delete_user: %s" % (u_id))
        conn = sqlite3.connect("demo.db")
        param = (u_id,)
        try:
            conn.execute('DELETE FROM user WHERE u_id = ?;', param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success", ""

    def update_user(self, u_id, u_name=None, u_role=None,
                    u_password=None, u_phone=None, c_id=None):
        """
        update_user
        :return: 'Success', '' or 'Fail', 'error_msg'
        """
        log("update_user: %s %s %s %s %s %s" %
            (u_id, u_name, u_role, u_password, u_phone, c_id))
        conn = sqlite3.connect("demo.db")
        param = (u_id,)
        try:
            if c_id is not None and u_role == 'admin':
                param = (c_id,)
                response = conn.execute('SELECT u_id FROM community WHERE c_id = ?', param)
                response = response.fetchall()[0][0]
                if response is not None:
                    return "Fail", "Community %s already has an administrator." % c_id
            response = conn.execute('SELECT * FROM user WHERE u_id = ?;', param)
            origin = response.fetchall()[0]
            origin = list(origin)
            if u_name is not None:
                origin[1] = u_name
            if u_role is not None:
                origin[2] = u_role
            if u_password is not None:
                origin[3] = u_password
            if u_phone is not None:
                origin[4] = u_phone
            if c_id is not None:
                origin[5] = c_id

            param = tuple(origin) + (u_id,)
            conn.execute(
                'UPDATE user '
                'SET u_id = ?, u_name = ?, u_role = ?, u_password = ?, '
                'u_phone = ?, c_id = ? '
                'WHERE u_id = ?;',
                param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success", ""

    def get_user_by_uid(self, u_id):
        """
        get_user_by_uid
        :return: 'Success', <response> or 'Fail', 'error_msg'
        """
        conn = sqlite3.connect("demo.db")
        param = (u_id,)
        try:
            response = conn.execute('SELECT * FROM user WHERE u_id = ?;', param)
            response = response.fetchall()
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.close()
        return "Success", response

    def get_user_by_cid(self, c_id):
        """
        get_user_by_cid
        :return: 'Success', <response> or 'Fail', 'error_msg'
        """
        conn = sqlite3.connect("demo.db")
        param = (c_id,)
        try:
            if c_id == 0:
                response = conn.execute('SELECT * FROM user')
            else:
                response = conn.execute('SELECT * FROM user WHERE c_id = ?;', param)
            response = response.fetchall()
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()

        conn.close()
        return "Success", response

    def get_all_user_info(self):
        """
        get_all_user_info
        :return: 'Success', <response> or 'Fail', 'error_msg'
        """
        try:
            conn = sqlite3.connect("demo.db")
            response = conn.execute('SELECT * FROM user;')
            response = response.fetchall()
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.close()
        return "Success", response


user = User()
