# -*- coding: UTF-8 -*-
import sqlite3
from webapp.mylog import log
"""
数据库表中的所有操作都要通过log保存一份记录
"""


class User(object):
    """
    封装了与用户信息表相关的所有操作：增删改 + 查
    create table user
    (
        u_id            int         not null,
        u_name          char(30)    not null,
        u_role          char(10)    not null,
        u_password      char(30)    not null,
        u_phone         char(30)    not null,
        c_id            int         not null,
        foreign key     (c_id)      references   community(c_id),
        primary key     (u_id)
    )
    ;
    """

    # def __init__(self) :
    #     self.__counter = 0
    #@staticmethod
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
        log("add user")
        conn = sqlite3.connect("test.db")

        param = (u_name, u_role, u_password, u_phone, c_id,)
        conn.execute('insert into user(u_name, u_role, u_password, u_phone, c_id) values (?, ?, ?, ?, ?);', param)
        conn.commit()
        conn.close()
        return "Success"

    #@staticmethod
    def delete_user(self, u_id):
        """
        delete_user
        :param u_id:
        :return: 'Success', '' or 'Fail', 'error_msg'
        """
        log("delete_user")
        conn = sqlite3.connect("test.db")
        param = (u_id,)
        conn.execute('delete from user where u_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    #@staticmethod
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
        log("update_user")
        conn = sqlite3.connect("test.db")
        param = (u_id,)
        response = conn.execute('select * from user where u_id = ?;', param)
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
            'update user set u_id = ?, u_name = ?, u_role = ?, u_password = ?, u_phone = ?, c_id = ? where u_id = ?;',
            param)
        conn.commit()
        conn.close()
        return "Success"

    #@staticmethod
    def get_user_by_uid(self, u_id):
        """

        :param u_id:
        :return: 'Success', <cursor> or 'Fail', 'error_msg'
        """
        log("get_user_by_uid")
        conn = sqlite3.connect("test.db")
        param = (u_id,)
        response = conn.execute('select * from user where u_id = ?;', param)
        response = response.fetchall()
        conn.close()
        return "Success", response

    #@staticmethod
    def get_user_by_cid(self, c_id):
        """
        get_user_by_cid
        :param c_id:
        :return: 'Success', <cursor> or 'Fail', 'error_msg'
        """
        log("get_user_by_cid")
        conn = sqlite3.connect("test.db")
        param = (c_id,)
        if c_id == 0:
            response = conn.execute('select * from user')
        else:
            response = conn.execute('select * from user where c_id = ?;', param)
        response = response.fetchall()
        conn.close()
        return "Success", response

    #@staticmethod
    def get_all_user(self):
        """

        :return: 'Success', <cursor> or 'Fail', 'error_msg'
        """
        log("get_all_user")
        conn = sqlite3.connect("test.db")
        response = conn.execute('select * from user;')
        response = response.fetchall()
        conn.close()
        return "Success", response

user = User()
