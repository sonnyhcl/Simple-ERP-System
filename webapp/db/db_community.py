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

    #def __init__(self, conn) :
    #    conn = conn
    def add_community(self, _c_id, _c_name = ""):
        conn = sqlite3.connect("test.db");
        param = (_c_id, _c_name,)
        conn.execute('insert into community values (?, ?)', param)
        conn.commit()
        conn.close()
        return "Success"

    def delete_community(self, _c_id):
        conn = sqlite3.connect("test.db");
        param = (_c_id,)
        conn.execute('delete from community where c_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    def update_community(self, _c_id, _new_c_name):
        conn = sqlite3.connect("test.db");
        param = (_new_c_name, _c_id,)
        conn.execute('update community set c_name = ? where c_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    def get_community(self, _c_id):
        conn = sqlite3.connect("test.db");
        param = (_c_id,)
        response = conn.execute('select * from community where c_id = ?;', param)
        return "Success", response

    def get_all(self, ):
        conn = sqlite3.connect("test.db");
        response = conn.execute('select * from community;')
        return "Success", response
