import sqlite3

conn = sqlite3.connect('test.db')

# print "Open Database Successfully!"

"""
product info table
"""

conn.execute(
    '''
        CREATE TABLE product
        (
            p_id        INTEGER     PRIMARY KEY    AUTOINCREMENT,
            p_name      char(60)    NOT NULL,
            author_name char(10)
        )
        ;
    '''
)

# print "product info table created Successfully!"

"""
item info table
"""

conn.execute(
    '''
        CREATE TABLE item
        (
            i_id            INTEGER         PRIMARY KEY    AUTOINCREMENT,
            i_name          char(90)    NOT NULL,
            i_minutes       INT         NOT NULL,
            i_unitprices    FLOAT       NOT NULL,
            i_prices        FLOAT       NOT NULL,
            p_id            INT         NOT NULL,
            FOREIGN KEY     (p_id)      REFERENCES      product(p_id)
        )
        ;
    '''
)

# print "item info table created Successfully!"

"""
product / item info table
"""

conn.execute(
    '''
        CREATE TABLE pi
        (
            i_id            INT         NOT NULL,
            p_id            INT         NOT NULL,
            FOREIGN KEY     (p_id)      REFERENCES      product(p_id),
            FOREIGN KEY     (i_id)      REFERENCES      item(i_id),
            PRIMARY KEY     (i_id, p_id)
        )
        ;
    '''
)

# print "product / item info table created Successfully!"

"""
community info table
"""

conn.execute(
    '''
        CREATE TABLE community
        (
            c_id            INTEGER         PRIMARY KEY    AUTOINCREMENT,
            c_name          char(30)    NOT NULL
        )
        ;
    '''
)

# print "community info table created Successfully!"


"""
user info table
"""

conn.execute(
    '''
        CREATE TABLE user
        (
            u_id            INTEGER         PRIMARY KEY    AUTOINCREMENT,
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

# print "user info table created Successfully!"

"""
transactions info table
"""

conn.execute(
    '''
        CREATE TABLE transactions
        (
            t_id            INTEGER         PRIMARY KEY AUTOINCREMENT,
            u_id            INT         NOT NULL,
            c_id            INT         NOT NULL,
            p_id            INT         NOT NULL,
            i_id            INT         NOT NULL,
            amount          INT,
            timestamp       DATETIME    DEFAULT(datetime('now', 'localtime')),
            FOREIGN KEY     (u_id)      REFERENCES   user(u_id),
            FOREIGN KEY     (c_id)      REFERENCES   community(c_id),
            FOREIGN KEY     (p_id)      REFERENCES   product(p_id),
            FOREIGN KEY     (i_id)      REFERENCES   item(i_id)
        )
        ;
    '''
)

# print "transactions info table created Successfully!"


"""
admin info table
"""

conn.execute(
    '''
        CREATE TABLE admin
        (
            c_id            INT         NOT NULL,
            u_id            INT         NOT NULL,
            FOREIGN KEY     (c_id)      REFERENCES      community(c_id),
            FOREIGN KEY     (u_id)      REFERENCES      user(u_id),
            PRIMARY KEY     (c_id, u_id)
        )
        ;
    '''
)

# print "admin info table created Successfully!"

conn.execute(
    '''
        SELECT * FROM item;
    '''
)

conn.execute(
    """
    INSERT INTO user(u_name, u_role, u_password, u_phone)
    VALUES ('hcl', 'root', 'hcl', 'hclphone')
    """
)
