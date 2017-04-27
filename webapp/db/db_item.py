# -*- coding: UTF-8 -*-
import sqlite3

__author__ = 'sonnyhcl'


class Item(object):
    def add_item_for_product(self, i_name, i_ref_time, i_unit_price, i_note, p_id):
        conn = sqlite3.connect("demo.db")
        param = (i_name, i_ref_time, i_unit_price, i_note, p_id)
        conn.execute('INSERT INTO item(i_name, i_unit_price, i_ref_time, i_note, p_id) '
                     'VALUES (?, ?, ?, ?, ?);', param)
        conn.commit()
        conn.close()
        return "Success", ""

    def delete_item_for_product(self, p_id, i_id):
        conn = sqlite3.connect("demo.db")

        param = (p_id,)
        response = conn.execute('SELECT count(*) from item WHERE p_id = ?;', param)
        count = response.fetchall()
        if count[0] == 0:
            return "Fail", "you can not delete the last item of this product"
        param = (i_id,)
        conn.execute('DELETE FROM item WHERE i_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success", ""

    def update_item(self, i_id, _i_name=None, _i_minutes=None,
                    _i_prices=None, _p_id=None):

        conn = sqlite3.connect("demo.db")

        param = (i_id,)
        response = conn.execute('SELECT * FROM item WHERE i_id = ?;', param)
        origin = response.fetchall()[0]
        origin = list(origin)
        if _i_name is not None:
            origin[1] = _i_name
        if _i_minutes is not None:
            origin[2] = _i_minutes
        if _i_prices is not None:
            origin[3] = _i_prices
        if _p_id is not None:
            origin[4] = _p_id
        param = tuple(origin) + (i_id,)
        conn.execute(
            'UPDATE item SET i_id = ?, i_name = ?, i_unit_price = ?, p_id = ? WHERE i_id = ?;',
            param)
        conn.commit()
        conn.close()
        return "Success"

    def get_item(self, i_id):
        conn = sqlite3.connect("demo.db")

        param = (i_id,)
        response = conn.execute('SELECT * FROM item WHERE i_id = ?;', param)
        response = response.fetchall()
        conn.close()
        return "Success", response

    def get_all(self, ):
        conn = sqlite3.connect("demo.db")
        response = conn.execute('SELECT * FROM item;')
        response = response.fetchall()
        conn.close()
        return "Success", response

item = Item()
