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

# TODO: just4test
def db_show_user(cid):
    """
    显示社区id为cid的社区人员信息
    :param cid: 社区id
    :return: 'Success', array(tuple(info)) or 'Fail', 'error_msg'
    """
    log("db_show_user")
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
# -*- coding: UTF-8 -*-
import sqlite3
from webapp.mylog import log
"""
数据库表中的所有操作都要通过log保存一份记录
"""









