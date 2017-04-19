# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'
import sqlite3
'''
        create table product
        (
            p_id        int         not null,
            p_name      char(60)    not null,
            author_name char(10),
            primary key (p_id)
        )
        ;
'''

class Product(object):
    """
    产品信息表
    """

    def __init__(self) :
        self.__conn = sqlite3.connect('test.db')
    def add_product(self, _p_id, _p_name, _author_name = ""):
        param = (_p_id, _p_name, _author_name,)
        self.__conn.execute('insert into product values (?, ?, ?);', param)
        return "Success"

    def delete_product(self, _p_id):
        param = (_p_id,)
        self.__conn.execute('delete from product where p_id = ?;', param)
        return "Success"

    def update_product(self, _p_id, _p_name = None, _author_name = None):
        param = (_p_id,)
        response = self.__conn.execute('select * from product where p_id = ?;', param)
        origin = response.fetchall()[0]
        origin = list(origin)
        if _p_name          is not None :
            origin[1] = _p_name
        if _author_name     is not None :
            origin[2] = _author_name
        param = tuple(origin) + (_p_id,)
        self.__conn.execute('update product set p_id = ?, p_name = ?, author_name = ? where p_id = ?;', param)
        return "Success"

    def get_product(self, _p_id):
        param = (_p_id,)
        response = self.__conn.execute('select * from product where p_id = ?;', param)
        return "Success", response

    def get_all(self, ):
        response = self.__conn.execute('select * from product;')
        return "Success", response
