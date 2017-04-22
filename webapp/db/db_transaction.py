# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'
import sqlite3
'''
        create table transactions
        (
            t_id            integer         primary key autoincrement,
            u_id            int         not null,
            c_id            int         not null,
            p_id            int         not null,
            i_id            int         not null,
            amount          int,
            timestamp       datetime    default('now', 'localtime'),
            foreign key     (u_id)      references   user(u_id),
            foreign key     (c_id)      references   community(c_id),
            foreign key     (p_id)      references   product(p_id),
            foreign key     (i_id)      references   item(i_id)
        )
        ;
'''



class Transactions(object):
    """
    流水信息表
    """

    # def __init__(self) :
    #     self.__counter = 0
    def add_transactions(self, u_id, c_id, p_id, i_id, amount = 0):
        conn = sqlite3.connect("test.db");
        param = (None, u_id, c_id, p_id, i_id, amount, )
        conn.execute('insert into transactions(t_id, u_id, c_id, p_id, i_id, amount) values (?, ?, ?, ?, ?, ?);', param)
        conn.commit()
        conn.close()
        return "Success"

    def delete_transactions(self, t_id):
        conn = sqlite3.connect("test.db");

        param = (t_id,)
        conn.execute('delete from transactions where t_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    def update_transactions(self, t_id, u_id = None, c_id = None, p_id = None, i_id = None):
        conn = sqlite3.connect("test.db");

        param = (t_id,)
        response = conn.execute('select * from transactions where t_id = ?;', param)
        origin = response.fetchall()[0]
        origin = list(origin)
        if u_id          is not None :
            origin[1] = u_id
        if c_id            is not None :
            origin[2] = c_id
        if p_id            is not None :
            origin[3] = p_id
        if i_id            is not None :
            origin[4] = i_id

        param = tuple(origin) + (t_id,)
        conn.execute('update transactions set t_id = ?, u_id =  ?, c_id =  ?, p_id =  ?, i_id = ? where t_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    def get_transactions(self, t_id):
        conn = sqlite3.connect("test.db");

        param = (t_id,)
        response = conn.execute('select * from transactions where t_id = ?;', param)
        response = response.fetchall()
        conn.close()
        return "Success", response

    def get_all(self, ):
        conn = sqlite3.connect("test.db");

        response = conn.execute('select * from transactions;')
        response = response.fetchall()
        conn.close()
        return "Success", response
