# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'
import sqlite3
'''
        create table transactions
        (
            t_id            int         not null,
            u_id            int         not null,
            c_id            int         not null,
            p_id            int         not null,
            i_id            int         not null,
            foreign key     (u_id)      references   user(u_id),
            foreign key     (c_id)      references   community(c_id),
            foreign key     (p_id)      references   product(p_id),
            foreign key     (i_id)      references   item(i_id),
            primary key     (t_id)
        )
        ;
'''



class Transactions(object):
    """
    流水信息表
    """

    def __init__(self) :
        self.__conn = sqlite3.connect('test.db')
    def add_transactions(self, _t_id, _u_id, _c_id, _p_id, _i_id):
        param = (_t_id, _u_id, _c_id, _p_id, _i_id,)
        self.__conn.execute('insert into transactions values (?, ?, ?, ?, ?);', param)
        return "Success"

    def delete_transactions(self, _t_id):
        param = (_t_id,)
        self.__conn.execute('delete from transactions where t_id = ?;', param)
        return "Success"

    def update_transactions(self, _t_id, _u_id = None, _c_id = None, _p_id = None, _i_id = None):
        param = (_t_id,)
        response = self.__conn.execute('select * from transactions where t_id = ?;', param)
        origin = response.fetchall()[0]
        origin = list(origin)
        if _u_id          is not None :
            origin[1] = _u_id
        if _c_id            is not None :
            origin[2] = _c_id
        if _p_id            is not None :
            origin[3] = _p_id
        if _i_id            is not None :
            origin[4] = _i_id

        param = tuple(origin) + (_t_id,)
        self.__conn.execute('update transactions set t_id = ?, u_id =  ?, c_id =  ?, p_id =  ?, i_id = ? where t_id = ?;', param)
        return "Success"

    def get_transactions(self, _t_id):
        param = (_t_id,)
        response = self.__conn.execute('select * from transactions where t_id = ?;', param)
        return "Success", response

    def get_all(self, ):
        response = self.__conn.execute('select * from transactions;')
        return "Success", response
