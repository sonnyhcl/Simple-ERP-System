# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'
'''
        create table item
        (
            i_id            int         not null,
            i_name          char(90)    not null,
            i_minutes       int         not null,
            i_unitprices    float       not null,
            i_prices        float       not null,
            p_id            int         not null,
            foreign key     (p_id)      references      product(p_id),
            primary key     (i_id)
        )
        ;
'''

class Item(object):
    """
    社区信息表
    """
    def add_item(self, conn, _i_id, _i_name, _i_minutes, _i_unitprices, _p_id):
        param = (_i_id, _i_name, _i_minutes, _i_unitprices, _p_id,)
        conn.execute('insert into item values (?);', param)
        return "Success"

    def delete_item(self, conn, _i_id):
        param = (_i_id,)
        conn.execute('delete from item where i_id = ?;', param)
        return "Success"

    def update_item(self, conn, _i_id, _i_name = None, _i_minutes = None, _i_unitprices = None, _p_id = None):
        param = (_i_id,)
        response = conn.execute('select * from item where i_id = ?', param)
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
