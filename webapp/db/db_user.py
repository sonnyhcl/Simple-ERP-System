# -*- coding: UTF-8 -*-


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


def db_show_user(cid, page):
    """
    显示社区id为cid的社区人员信息,二十个人/页
    :param cid: 社区id
    :param page: 第几页
    :return: array(tuple(info))
    """
    info = [(u'高科苑', u'hcl', u'hclphone'), (u'高科苑', u'admin', u'adminphone')]
    return info
