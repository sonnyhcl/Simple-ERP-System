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
        self.__counter = 0
    def add_product(self, p_name, author_name = ""):
        conn = sqlite3.connect("test.db");
        param = (None, p_name, author_name,)
        conn.execute('insert into product values (?, ?, ?);', param)
        conn.commit()
        conn.close()
        return "Success"

    def delete_product(self, p_id):
        conn = sqlite3.connect("test.db");

        param = (p_id,)
        conn.execute('delete from product where p_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    def update_product(self, p_id, p_name = None, author_name = None):
        conn = sqlite3.connect("test.db");

        param = (p_id,)
        response = conn.execute('select * from product where p_id = ?;', param)
        origin = response.fetchall()[0]
        origin = list(origin)
        if p_name          is not None :
            origin[1] = p_name
        if author_name     is not None :
            origin[2] = author_name
        param = tuple(origin) + (p_id,)
        conn.execute('update product set p_id = ?, p_name = ?, author_name = ? where p_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    def get_product(self, p_id):
        conn = sqlite3.connect("test.db");

        param = (p_id,)
        response = conn.execute('select * from product where p_id = ?;', param)
        response = response.fetchall()
        conn.close()
        return "Success", response

    def get_all(self, ):
        conn = sqlite3.connect("test.db");

        response = conn.execute('select * from product;')
        response = response.fetchall()
        conn.close()
        return "Success", response
