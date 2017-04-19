# -*- coding: UTF-8 -*-
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
    info = [(u'高科苑', u'hcl', u'hclphone'), (u'高科苑', u'admin', u'adminphone')]
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
