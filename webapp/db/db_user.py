# -*- coding: UTF-8 -*-
"""
数据库表中的增改删操作都要log
用户页面所有数据库相关操作
"""
import sqlite3
from flask import session
from webapp.mylog import log


class User(object):
    def add_user(self, u_name, u_role, u_password, u_phone, c_id):
        """
        add_user
        :param u_name:
        :param u_role:
        :param u_password:
        :param u_phone:
        :param c_id:
        :return: 'Success', '' or 'Fail', 'error_msg'
        """
        # TODO 名字判重
        log("%s: add_user: %s %s %s %s %s"
            % (session['u_name'], u_name, u_role, u_password, u_phone, c_id))
        conn = sqlite3.connect("test.db")
        param = (u_name, u_role, u_password, u_phone, c_id,)
        conn.execute(
            'INSERT INTO user(u_name, u_role, u_password, u_phone, c_id) VALUES (?, ?, ?, ?, ?);',
            param)
        conn.commit()
        conn.close()
        return "Success"

    def delete_user(self, u_id):
        """
        delete_user
        :param u_id:
        :return: 'Success', '' or 'Fail', 'error_msg'
        """
        log("%s: delete_user: %s" % (session['u_name'], u_id))
        conn = sqlite3.connect("test.db")
        param = (u_id,)
        conn.execute('DELETE FROM user WHERE u_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    def update_user(self, u_id, u_name=None, u_role=None,
                    u_password=None, u_phone=None, c_id=None):
        """
        update_user
        :param u_id:
        :param u_name:
        :param u_role:
        :param u_password:
        :param u_phone:
        :param c_id:
        :return: 'Success', '' or 'Fail', 'error_msg'
        """
        log("%s: update_user: %s %s %s %s %s %s" %
            (session['u_name'], u_id, u_name, u_role, u_password, u_phone,
            c_id))
        conn = sqlite3.connect("test.db")
        param = (u_id,)
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
            'UPDATE user SET u_id = ?, u_name = ?, u_role = ?, u_password = ?, u_phone = ?, c_id = ? WHERE u_id = ?;',
            param)
        conn.commit()
        conn.close()
        return "Success"

    def get_user_by_uid(self, u_id):
        """

        :param u_id:
        :return: 'Success', <response> or 'Fail', 'error_msg'
        """
        conn = sqlite3.connect("test.db")
        param = (u_id,)
        response = conn.execute('SELECT * FROM user WHERE u_id = ?;', param)
        response = response.fetchall()
        conn.close()
        return "Success", response

    def get_user_by_cid(self, c_id):
        """
        get_user_by_cid
        :param c_id:
        :return: 'Success', <response> or 'Fail', 'error_msg'
        """
        conn = sqlite3.connect("test.db")
        param = (c_id,)
        if c_id == 0:
            response = conn.execute('SELECT * FROM user')
        else:
            response = conn.execute('SELECT * FROM user WHERE c_id = ?;', param)
        response = response.fetchall()
        conn.close()
        return "Success", response

    def get_all_user_info(self):
        """

        :return: 'Success', <response> or 'Fail', 'error_msg'
        """
        conn = sqlite3.connect("test.db")
        response = conn.execute('SELECT * FROM user;')
        response = response.fetchall()
        conn.close()
        return "Success", response


user = User()
