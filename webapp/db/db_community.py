# -*- coding: UTF-8 -*-
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
    def add_community(self, conn, _c_id, _c_name = ""):
        param = (_c_id, _c_name,)
        conn.execute('insert into community values (?);', param)
        return "Success"

    def delete_community(self, conn, _c_id):
        param = (_c_id,)
        conn.execute('delete from community where c_id = ?;', param)
        return "Success"

    def update_production(self, conn, _c_id, _new_c_name):
        param = (_new_c_name, _c_id,)
        conn.execute('update community set c_name = ? where c_id = ?;', param)
        return "Success"

    def get_production(self, conn, _c_id):
        param = (_C_id,)
        response = conn.execute('select * from community where c_name = ?;', param)
        return "Success", response

    def get_all(self):
        response = conn.execute('select * from community;')
        return "Success", response
