# -*- coding: UTF-8 -*-
import sqlite3

__author__ = 'sonnyhcl'


class Community(object):
    """
    社区信息表
    create table community
    (
        c_id            integer         primary key    autoincrement,
        c_name          char(30)    not null
    )
    """

    def __init__(self):
        self.__counter = 0

    def add_community(self, c_name):
        # TODO: 社区判重
        conn = sqlite3.connect("test.db")
        param = (c_name,)
        conn.execute('INSERT INTO community(c_name) VALUES (?);', param)
        conn.commit()
        conn.close()
        return "Success"

    def delete_community(self, c_id):
        conn = sqlite3.connect("test.db")
        param = (c_id,)
        conn.execute('DELETE FROM community WHERE c_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    def update_community(self, c_id, new_c_name):
        conn = sqlite3.connect("test.db")
        param = (new_c_name, c_id,)
        conn.execute('UPDATE community SET c_name = ? WHERE c_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    def get_community(self, c_id):
        conn = sqlite3.connect("test.db")
        param = (c_id,)
        if c_id == 0:
            response = conn.execute('SELECT * FROM community;')
        else:
            response = conn.execute('SELECT * FROM community WHERE c_id = ?;',
                                    param)
        response = response.fetchall()
        conn.close()
        return "Success", response

    def get_all(self, ):
        conn = sqlite3.connect("test.db")
        response = conn.execute('SELECT * FROM community;')
        response = response.fetchall()
        conn.close()
        return "Success", response


community = Community()
