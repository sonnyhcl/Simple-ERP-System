# -*- coding: UTF-8 -*-
"""
产品页面所有数据库的相关操作
涉及到产品表和工艺表
"""
__author__ = 'sonnyhcl'
import sqlite3


class Product(object):
    def add_product(self, p_name, i_name, i_unit_price, i_ref_time,
                    author_name="", ):
        conn = sqlite3.connect("demo.db")
        try:
            param = (p_name, author_name,)
            conn.execute('INSERT INTO product VALUES (p_name, author_name);',
                         param)
            response = conn.execute(
                'SELECT p_id FROM product WHERE p_name = ? AND author_name = ?;',
                param)
            response = response.fetchall()
            p_id = response[0][0]
            param = (i_name, i_unit_price, i_ref_time, p_id,)
            conn.execute(
                'INSERT INTO item VALUES (i_name = ?, i_unit_price = ?, i_ref_time = ?, p_id = ?);',
                param)
        except Exception:
            conn.close()
            return "Fail", Exception
        conn.commit()
        conn.close()
        return "Success"

    def delete_product(self, p_id):
        conn = sqlite3.connect("demo.db")
        param = (p_id,)
        try:
            conn.execute('DELETE FROM item WHERE p_id = ?;', param)
            conn.execute('DELETE FROM product WHERE p_id = ?;', param)
        except Exception:
            conn.close()
            return "Fail", Exception
        conn.commit()
        conn.close()
        return "Success"

    def update_product(self, p_id, i_id, p_name=None, author=None,
                       i_name=None, i_unit_price=None, i_ref_time=None,
                       i_note=None):
        conn = sqlite3.connect("demo.db")
        try:
            param = (p_id,)
            response = conn.execute('SELECT * FROM product WHERE p_id = ?;',
                                    param)
            origin = response.fetchall()[0]
            origin = list(origin)
            if p_name is not None:
                origin[1] = p_name
            if author is not None:
                origin[2] = author
            param = tuple(origin) + (p_id,)
            conn.execute(
                'UPDATE product SET p_id = ?, p_name = ?, p_author = ? '
                'WHERE p_id = ?;',
                param)
            param = (i_id,)
            response = conn.execute('SELECT * FROM item WHERE i_id = ?;', param)
            origin = response.fetchall()[0]
            origin = list(origin)
            if i_name is not None:
                origin[1] = i_name
            if i_unit_price is not None:
                origin[2] = i_unit_price
            if i_ref_time is not None:
                origin[3] = i_ref_time
            param = tuple(origin) + (i_id,)
            conn.execute(
                'UPDATE item SET i_id = ?, i_name = ?, i_unit_price = ?, i_ref_time = ? WHERE i_id = ?;',
                param)
        except Exception:
            conn.close()
            return "Fail", Exception
        conn.commit()
        conn.close()
        return "Success", ""

    def get_product(self, p_id):
        conn = sqlite3.connect("demo.db")

        param = (p_id,)
        response = conn.execute('SELECT * FROM product WHERE p_id = ?;', param)
        response = response.fetchall()
        conn.close()
        return "Success", response

    def get_all(self, ):
        conn = sqlite3.connect("demo.db")
        try:
            response = conn.execute(
                'SELECT * FROM product, item WHERE product.p_id = item.p_id;')
            response = response.fetchall()
        except Exception:
            return "Fail", Exception
        conn.close()
        return "Success", response

products = Product()
