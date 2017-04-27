# -*- coding: UTF-8 -*-
"""
生成一份可供测试的完善的数据库demo.db
"""
import os
import sqlite3

filename = 'demo.db'
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
            p_author      char(10)
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
            i_unit_price    FLOAT       NOT NULL,
            i_ref_time      INT         NOT NULL,
            i_note          INT         DEFAULT('无'),
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
            c_name          char(30)    NOT NULL,
            u_id            INT,
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
            u_name          char(30)    NOT NULL,
            u_role          char(10)    NOT NULL,
            u_password      char(30)    NOT NULL,
            u_phone         char(30)    NOT NULL,
            c_id            INT         NOT NULL,
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
            o_amount        INT         NOT NULL,
            o_money         FLOAT       NOT NULL,
            o_timestamp     DATETIME    DEFAULT(datetime('now', 'localtime')),
            o_notes         CHAR(50)    DEFAULT('无'),
            p_id            INT         NOT NULL,
            FOREIGN KEY     (p_id)      REFERENCES   job(p_id)
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
            m_amount        INT,
            m_notes         CHAR(50)    DEFAULT('无'),
            u_id            INT,
            i_id            INT,
            o_id            INT,
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
            t_amount        INT,
            t_timestamp     DATETIME    DEFAULT(datetime('now', 'localtime')),
            t_notes         CHAR(50)    DEFAULT('无'),
            m_id            INT         NOT NULL,
            FOREIGN KEY     (m_id)      REFERENCES   mission(m_id)
        )
        ;
    '''
)
print "transactions info table created Successfully!"


##################################################
"""
添加社区信息（社区id，社区名，社区管理员id）
默认社区管理员为u_id=0的人
"""
conn.execute(
    """
    INSERT INTO community(c_id, c_name, u_id)
    VALUES  (0, '彩虹桥', 0), (1, '社区A',   0), ( 2, '社区B',  0);
    """
)

"""
添加用户信息（用户编号，用户名，身份，密码，联系方式，社区编号）
默认超管的c_id为0
"""
conn.execute(
    """
    INSERT INTO user(u_id, u_name, u_role, u_password, u_phone, c_id)
    VALUES  (0, 'hcl',     'root',     'hcl',  '12345678910',   0),
            (1, 'admin',   'admin',    'admin','12345678910',   1),
            (2, 'user',    'user',     'uer',  '12345678910',   1),
            (3, '管理员',   'admin',    'admin','12345678910',   2),
            (4, '用户',     'user',     'user', '12345678910',   2);
    """
)

"""
添加产品（产品编号，产品名，设计师）
"""
conn.execute(
    """
    INSERT INTO product(p_name, p_author)
    VALUES  ('产品A',  '设计师A'), ('产品B',  '设计师B');
    """
)

"""
添加工艺信息（工艺编号，工艺名，分钟单价，参考时间，产品编号）
"""
conn.execute(
    """
    INSERT INTO item(i_name, i_unit_price, i_ref_time, p_id)
    VALUES  ('产品A的工艺1',  10,  100, 1), ('产品A的工艺2',  20, 200, 1),
            ('产品B的工艺2',  30,  300, 2), ('产品B的工艺2',  40, 400, 2);
    """
)

"""
添加订单（数量, 金额，产品编号)
"""
conn.execute(
    """
    INSERT INTO orders(o_amount, o_money, p_id)
    VALUES (10, 1000, 1), (20, 20000, 2);
"""
)

"""
添加任务（任务编号，分配数量，用户编号，工艺编号，订单号）
"""
conn.execute(
    """
    INSERT INTO mission(m_amount, u_id, i_id, o_id)
    VALUES  (10, 1, 1, 1), (20, 2, 2, 1), (30, 1, 3, 2), (40, 2, 4, 2);
"""
)

"""
添加流水（流水编号，数量，交付时间戳，任务编号）
"""
conn.execute(
    """
    INSERT INTO transactions(t_amount, m_id)
    VALUES  (10, 1), (20, 2), (30, 3), (40, 4);
    """
)

conn.commit()
conn.close()
