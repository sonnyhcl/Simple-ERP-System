# -*- coding: UTF-8 -*-
"""
生成一份可供测试的完善的数据库demo.db
"""
import os
import sqlite3

filename = os.path.join('..', '..', 'demo.db')
if os.path.exists(filename):
    os.remove(filename)
conn = sqlite3.connect(filename)
print "Open Database Successfully!"

"""
产品（产品编号，产品名，设计师）
"""
conn.execute(
    '''
        CREATE TABLE product
        (
            p_id          INTEGER     PRIMARY KEY    AUTOINCREMENT,
            p_name        char(60)    NOT NULL,
            p_author      char(10)    DEFAULT 'hcl'
        )
        ;
    '''
)
print "product info table created Successfully!"

"""
工艺（工艺编号，工艺名，分钟单价，参考时间，工艺规格，产品编号）
这里还是按照工艺编号实现好了 | 工艺规格就是工艺的备注
"""
conn.execute(
    '''
        CREATE TABLE item
        (
            i_id            INTEGER     PRIMARY KEY    AUTOINCREMENT,
            i_name          char(90)    NOT NULL,
            i_unit_price    FLOAT       DEFAULT 0,
            i_ref_time      INT         DEFAULT 0,
            i_note          INT         DEFAULT '无',
            p_id            INT         NOT NULL,
            FOREIGN KEY     (p_id)      REFERENCES      product(p_id)
        )
        ;
    '''
)
print "item info table created Successfully!"

"""
社区（社区编号，社区名，管理员编号）
"""
conn.execute(
    '''
        CREATE TABLE community
        (
            c_id            INTEGER     PRIMARY KEY    AUTOINCREMENT,
            c_name          char(30)    UNIQUE NOT NULL,
            u_id            INT         DEFAULT 0,
            FOREIGN KEY     (u_id)      REFERENCES   user(u_id)
        )
        ;
    '''
)
print "community info table created Successfully!"

"""
用户（用户编号，用户名，身份，密码，联系方式，社区编号）
"""
conn.execute(
    '''
        CREATE TABLE user
        (
            u_id            INTEGER     PRIMARY KEY    AUTOINCREMENT,
            u_name          char(30)    UNIQUE NOT NULL,
            u_role          char(10)    DEFAULT 'user',
            u_password      char(30)    DEFAULT '123456',
            u_phone         char(30)    NOT NULL,
            c_id            INT         DEFAULT 0,
            FOREIGN KEY     (c_id)      REFERENCES   community(c_id)
        )
        ;
    '''
)
print "user info table created Successfully!"

"""
订单（订单编号，数量, 开单时间，金额，订单备注, 产品编号)
#TODO 最后交付时间先不放
"""
conn.execute(
    '''
        CREATE TABLE orders
        (
            o_id            INTEGER     PRIMARY KEY AUTOINCREMENT,
            o_amount        INT         DEFAULT 0,
            o_money         FLOAT       DEFAULT 0,
            o_timestamp     DATETIME    DEFAULT (datetime('now', 'localtime')),
            o_note          CHAR(50)    DEFAULT '无',
            p_id            INT         NOT NULL,
            c_id            INT         DEFAULT 0,
            FOREIGN KEY     (p_id)      REFERENCES   product(p_id),
            FOREIGN KEY     (c_id)      REFERENCES   community(c_id)
        )
        ;
    '''
)
print "orders info table created Successfully!"

"""
任务（任务编号，用户编号，工艺编号，订单编号，分配数量，任务备注）
"""
conn.execute(
    '''
        CREATE TABLE mission
        (
            m_id            INTEGER     PRIMARY KEY AUTOINCREMENT,
            m_amount        INT         DEFAULT 0,
            m_note          CHAR(50)    DEFAULT '无',
            u_id            INT         NOT NULL,
            i_id            INT         NOT NULL,
            o_id            INT         NOT NULL,
            FOREIGN KEY     (u_id)      REFERENCES   user(u_id),
            FOREIGN KEY     (i_id)      REFERENCES   item(i_id),
            FOREIGN KEY     (o_id)      REFERENCES   orders(o_id)
        )
        ;
    '''
)
print "mission info table created Successfully!"

"""
流水（流水编号，数量，交付日期，流水备注，任务编号）
"""
conn.execute(
    '''
        CREATE TABLE transactions
        (
            t_id            INTEGER     PRIMARY KEY AUTOINCREMENT,
            t_amount        INT         DEFAULT 0,
            t_timestamp     DATETIME    DEFAULT (datetime('now', 'localtime')),
            t_note          CHAR(50)    DEFAULT '无',
            m_id            INT         NOT NULL,
            FOREIGN KEY     (m_id)      REFERENCES   mission(m_id)
        )
        ;
    '''
)
print "transactions info table created Successfully!"

##############################################################################
"""
添加社区信息（社区id，社区名，社区管理员id）
默认社区管理员为u_id=0的人
"""
conn.execute(
    """
    INSERT INTO community(c_id, c_name)
    VALUES  (0, '彩虹桥');
    """
)

"""
添加用户信息（用户编号，用户名，身份，密码，联系方式，社区编号）
默认超管的c_id为0
"""
conn.execute(
    """
    INSERT INTO user(u_id, u_name, u_role, u_password, u_phone, c_id)
    VALUES  (0, 'hcl',     'root',     'hcl',  '12345678910',   0);
    """
)

conn.commit()
conn.close()
