# -*- coding: UTF-8 -*-
"""
产品页面所有数据库的相关操作
涉及到产品表和工艺表
"""
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
    def add_product(self, p_name, author_name = "", i_name, i_unit_price, i_ref_time):
        conn = sqlite3.connect("demo.db");
        try :
            param = (p_name, author_name,)
            conn.execute('insert into product values (p_name, author_name);', param)
            response = conn.execute('select p_id from product where p_name = ? and author_name = ?;', param)
            response = response.fetchall()
            p_id = response[0][0]
            param = (i_name, i_unit_price, i_ref_time, p_id,)
            conn.execute('insert into item values (i_name = ?, i_unit_price = ?, i_ref_time = ?, p_id = ?);', param)
        except Exception:
            conn.close()
            return "Fail", Exception
        conn.commit()
        conn.close()
        return "Success"

    def delete_product(self, p_id):
        conn = sqlite3.connect("demo.db");

        param = (p_id,)
        try :
            conn.execute('delete from item where p_id = ?;', param)
            conn.execute('delete from product where p_id = ?;', param)
        except Exception:
            conn.close()
            return "Fail", Exception
        conn.commit()
        conn.close()
        return "Success"

    def update_product(self, p_id, p_name = None, author_name = None, i_id, i_name = None, i_unit_price = None, i_ref_time = None):
        conn = sqlite3.connect("demo.db");
        try:
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
            param = (i_id,)
            response = conn.execute('select * from item where i_id = ?;', param)
            origin = response.fetchall()[0]
            origin = list(origin)
            if i_name           is not None :
                origin[1] = i_name
            if i_unit_price     is not None :
                origin[2] = i_unit_price
            if i_ref_time       is not None:
                origin[3] = i_ref_time
            param = tuple(origin) + (i_id,)
            conn.execute('update item set i_id = ?, i_name = ?, i_unit_price = ?, i_ref_time = ? where i_id = ?;', param)
        except Exception:
            conn.close()
            return "Fail", Exception
        conn.commit()
        conn.close()
        return "Success"

    def get_product(self, p_id):
        conn = sqlite3.connect("demo.db");

        param = (p_id,)
        response = conn.execute('select * from product where p_id = ?;', param)
        response = response.fetchall()
        conn.close()
        return "Success", response

    def get_all(self, ):
        conn = sqlite3.connect("demo.db");

        response = conn.execute('select * from product;')
        response = response.fetchall()
        conn.close()
        return "Success", response
