# -*- coding: UTF-8 -*-
# TODO 待删
import sqlite3

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
    Item信息表
    """

    def __init__(self):
        self.__counter = 0

    def add_item(self, i_name, i_minutes, i_unitprices, i_prices, p_id):
        conn = sqlite3.connect("demo.db");
        param = (None, i_name, i_minutes, i_unitprices, i_prices, p_id,)
        conn.execute('INSERT INTO item VALUES (?, ?, ?, ?, ?, ?);', param)
        conn.commit()
        conn.close()
        return "Success"

    def delete_item(self, i_id):
        conn = sqlite3.connect("demo.db");

        param = (i_id,)
        conn.execute('DELETE FROM item WHERE i_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    def update_item(self, i_id, _i_name=None, _i_minutes=None,
                    _i_unitprices=None, _i_prices=None, _p_id=None):

        conn = sqlite3.connect("demo.db");

        param = (i_id,)
        response = conn.execute('SELECT * FROM item WHERE i_id = ?;', param)
        origin = response.fetchall()[0]
        origin = list(origin)
        if _i_name is not None:
            origin[1] = _i_name
        if _i_minutes is not None:
            origin[2] = _i_minutes
        if _i_unitprices is not None:
            origin[3] = _i_unitprices
        if _i_prices is not None:
            origin[4] = _i_prices
        if _p_id is not None:
            origin[5] = _p_id
        param = tuple(origin) + (i_id,)
        conn.execute(
            'UPDATE item SET i_id = ?, i_name = ?, i_minutes = ?, i_unitprices = ?, i_prices = ?, p_id = ? WHERE i_id = ?;',
            param)
        conn.commit()
        conn.close()
        return "Success"

    def get_item(self, i_id):
        conn = sqlite3.connect("demo.db");

        param = (i_id,)
        response = conn.execute('SELECT * FROM item WHERE i_id = ?;', param)
        response = response.fetchall()
        conn.close()
        return "Success", response

    def get_all(self, ):
        conn = sqlite3.connect("demo.db");
        response = conn.execute('SELECT * FROM item;')
        response = response.fetchall()
        conn.close()
        return "Success", response
