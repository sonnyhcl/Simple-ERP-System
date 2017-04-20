# -*- coding: UTF-8 -*-
import sqlite3
"""
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


class User(object):
    """
    用户信息表
    """

    def __init__(self, conn) :
        self.__conn = conn
    def add_user(self, _u_id, _u_name, _u_role, _u_password, _u_phone, _c_id):
        param = (_u_id, _u_name, _u_role, _u_password, _u_phone, _c_id,)
        self.__conn.execute('insert into user values (?, ?, ?, ?, ?, ?);', param)
        return "Success"

    def delete_user(self, _u_id):
        param = (_u_id,)
        self.__conn.execute('delete from user where u_id = ?;', param)
        return "Success"

    def update_user(self, _u_id, _u_name = None, _u_role = None, _u_password = None, _u_phone = None, _c_id = None):
        param = (_u_id,)
        response = self.__conn.execute('select * from user where u_id = ?;', param)
        origin = response.fetchall()[0]
        origin = list(origin)
        if _u_name          is not None :
            origin[1] = _u_name
        if _u_role          is not None :
            origin[2] = _u_role
        if _u_password      is not None :
            origin[3] = _u_password
        if _u_phone         is not None :
            origin[4] = _u_phone
        if _c_id            is not None :
            origin[5] = _c_id

        param = tuple(origin) + (_u_id,)
        self.__conn.execute('update user set u_id = ?, u_name = ?, u_role = ?, u_password = ?, u_phone = ?, c_id = ? where u_id = ?;', param)
        return "Success"

    def get_user(self, _u_id):
        param = (_u_id,)
        response = self.__conn.execute('select * from user where u_id = ?;', param)
        return "Success", response

    def get_all(self, ):
        response = self.__conn.execute('select * from user;')
        return "Success", response

def validate_user(username, password):
    """
    验证数据库中是否存在(username, password)
    :param username:
    :param password:
    :return:
    """
    if not username or not password:
        return False
    cur = {('hcl', 'hcl'), ('root', 'root'), ('admin', 'admin'), ('user',
                                                                  'user')}
    if (username, password) in cur:
        return True
    return False


def db_get_user_role(u_id):
    """
    根据u_id返回user role,从而控制权限
    :param u_id:
    :return: 'root' or 'admin' or 'user'
    """
    pass


def db_show_user(cid, page):
    """
    显示社区id为cid的社区人员信息,二十个人/页
    :param cid: 社区id
    :param page: 第几页
    :return: 'Success', array(tuple(info)) or 'Fail', 'error_msg'
    """
    info = [(0, u'高科苑', u'hcl', u'hclphone'),
            (1, u'高科苑', u'admin', u'adminphone')]
    return info


def db_add_user(user_info):
    """
    根据传进来的user_info在数据库中增加一个user
    :param user_info: { u_name, u_role, u_password, u_phone, c_id }
    :return: 'Success', '' or 'Fail', 'error_msg'
    """
    pass


def db_delete_user(u_id):
    """
    删除一个user
    :param u_id:
    :return: 'Success', '' or 'Fail', 'error_msg'
    """
    pass


def db_modify_user(user_info):
    """
    修改一个user信息
    :param user_info: { u_name, u_role, u_password, u_phone, c_id }
    :return: 'Success', '' or 'Fail', 'error_msg'
    """
    pass


def db_filter_user(cid):
    """
    根据社区id返回该社区所有人信息
    :param cid:
    :return: 'Success', array(tuple(info)) or 'Fail', 'error_msg'
    """
    pass
