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

    def __init__(self, conn):
        self.__conn = conn

    def add_user(self, _u_id, _u_name, _u_role, _u_password, _u_phone, _c_id):
        param = (_u_id, _u_name, _u_role, _u_password, _u_phone, _c_id,)
        self.__conn.execute('insert into user values (?, ?, ?, ?, ?, ?);', param)
        return "Success"

    def delete_user(self, _u_id):
        param = (_u_id,)
        self.__conn.execute('delete from user where u_id = ?;', param)
        return "Success"

    def update_user(self, _u_id, _u_name=None, _u_role=None, _u_password=None, _u_phone=None, _c_id=None):
        param = (_u_id,)
        response = self.__conn.execute('select * from user where u_id = ?;', param)
        origin = response.fetchall()[0]
        origin = list(origin)
        if _u_name is not None:
            origin[1] = _u_name
        if _u_role is not None:
            origin[2] = _u_role
        if _u_password is not None:
            origin[3] = _u_password
        if _u_phone is not None:
            origin[4] = _u_phone
        if _c_id is not None:
            origin[5] = _c_id

        param = tuple(origin) + (_u_id,)
        self.__conn.execute(
            'update user set u_id = ?, u_name = ?, u_role = ?, u_password = ?, u_phone = ?, c_id = ? where u_id = ?;',
            param)
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
    info = [(0, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (1, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (2, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (3, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (4, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (5, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (6, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (7, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (8, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (9, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (10, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (11, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (12, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (13, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (14, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (15, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (16, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (17, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (18, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (19, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (20, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (21, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (22, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (23, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (24, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (25, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (26, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (27, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (28, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (29, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (30, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (31, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (32, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (33, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (34, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (35, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (36, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (37, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (38, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (39, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (40, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (41, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (42, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (43, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (44, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (45, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (46, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (47, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (48, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (49, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (50, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (51, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (52, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (53, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (54, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (55, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (56, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (57, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (58, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (59, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (60, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (61, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (62, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (63, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (64, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (65, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (66, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (67, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (68, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (69, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (70, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (71, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (72, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (73, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (74, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (75, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (76, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (77, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (78, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (79, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (80, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (81, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (82, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (83, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (84, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (85, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (86, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (87, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (88, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (89, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (90, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (91, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (92, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (93, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (94, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (95, u'张江校区', u'cjm', u'root', u'cjmphone'),
            (96, u'邯郸校区', u'hcl', u'admin', u'hclphone'),
            (97, u'江湾校区', u'cjj', u'user', u'cjjphone'),
            (98, u'枫林校区', u'lb ', u'user', u'l bphone'),
            (99, u'张江校区', u'cjm', u'root', u'cjmphone'),
            ]

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
