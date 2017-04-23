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

    def __init__(self) :
        self.__counter = 0
    def add_community(self, c_name):
        conn = sqlite3.connect("test.db")
        param = (c_name,)
        conn.execute('insert into community(c_name) values (?);', param)
        conn.commit()
        conn.close()
        return "Success"

    def delete_community(self, c_id):
        conn = sqlite3.connect("test.db")
        param = (c_id,)
        conn.execute('delete from community where c_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    def update_community(self, c_id, new_c_name):
        conn = sqlite3.connect("test.db")
        param = (new_c_name, c_id,)
        conn.execute('update community set c_name = ? where c_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    def get_community(self, c_id):
        conn = sqlite3.connect("test.db")
        param = (c_id,)
        if c_id == 0:
            response = conn.execute('select * from community;')
        else:
            response = conn.execute('select * from community where c_id = ?;', param)
        response = response.fetchall()
        conn.close()
        return "Success", response

    def get_all(self, ):
        conn = sqlite3.connect("test.db")
        response = conn.execute('select * from community;')
        response = response.fetchall()
        conn.close()
        return "Success", response

community = Community()
