# -*- coding: UTF-8 -*-
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

    def __init__(self, conn) :
        self.__conn = conn
    def add_item(self, _i_id, _i_name, _i_minutes, _i_unitprices, _i_prices, _p_id):
        param = (_i_id, _i_name, _i_minutes, _i_unitprices, _i_prices, _p_id,)
        self.__conn.execute('insert into item values (?, ?, ?, ?, ?, ?);', param)
        return "Success"

    def delete_item(self, _i_id):
        param = (_i_id,)
        self.__conn.execute('delete from item where i_id = ?;', param)
        return "Success"

    def update_item(self, _i_id, _i_name = None, _i_minutes = None, _i_unitprices = None, _i_prices = None, _p_id = None):
        param = (_i_id,)
        response = self.__conn.execute('select * from item where i_id = ?;', param)
        origin = response.fetchall()[0]
        origin = list(origin)
        if _i_name          is not None :
            origin[1] = _i_name
        if _i_minutes       is not None :
            origin[2] = _i_minutes
        if _i_unitprices    is not None :
            origin[3] = _i_unitprices
        if _i_prices        is not None :
            origin[4] = _i_prices
        if _p_id            is not None :
            origin[5] = _p_id
        param = tuple(origin) + (_i_id,)
        self.__conn.execute('update item set i_id = ?, i_name = ?, i_minutes = ?, i_unitprices = ?, i_prices = ?, p_id = ? where i_id = ?;', param)
        return "Success"

    def get_item(self, _i_id):
        param = (_i_id,)
        response = self.__conn.execute('select * from item where i_id = ?;', param)
        return "Success", response

    def get_all(self, ):
        response = self.__conn.execute('select * from item;')
        return "Success", response
