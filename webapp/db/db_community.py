# -*- coding: UTF-8 -*-
import sqlite3
__author__ = 'sonnyhcl'
'''
    c_id            int         not null,
    c_name          char(30)    not null,
    primary key     (c_id)
'''
class Community(object):
    """
    社区信息表
    """

    def __init__(self, conn) :
        self.__conn = conn
    def add_community(self, _c_id, _c_name = ""):
        param = (_c_id, _c_name,)
        self.__conn.execute('insert into community values (?, ?)', param)
        return "Success"

    def delete_community(self, _c_id):
        param = (_c_id,)
        self.__conn.execute('delete from community where c_id = ?;', param)
        return "Success"

    def update_community(self, _c_id, _new_c_name):
        param = (_new_c_name, _c_id,)
        self.__conn.execute('update community set c_name = ? where c_id = ?;', param)
        return "Success"

    def get_community(self, _c_id):
        param = (_c_id,)
        response = self.__conn.execute('select * from community where c_id = ?;', param)
        return "Success", response

    def get_all(self, ):
        response = self.__conn.execute('select * from community;')
        return "Success", response
