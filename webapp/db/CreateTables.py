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
            i_unitprices    FLOAT       NOT NULL,
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
            c_name          char(30)    NOT NULL,
            u_id            int,
            FOREIGN KEY     (u_id)      REFERENCES   user(u_id)
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

conn.execute(
    '''
        SELECT * FROM item;
    '''
)


conn.execute(
    """
    INSERT INTO community(c_name)
    VALUES  ('community_a'),
            ('community_b');
    """
)

conn.execute(
    """
    INSERT INTO user(u_name, u_role, u_password, u_phone, c_id)
    VALUES  ('hcl',     'root',     'hcl',  'hclphone', 1),
            ('Alice',   'admin',    'a',    'aphone',   1),
            ('Bob',     'user',     'a',    'bphone',   1);
    """
)


conn.execute(
    """
    INSERT INTO product(p_name, author_name)
    VALUES  ('prod_a',  'Alice'),
            ('prod_b',  'Bob');
    """
)

conn.execute(
    """
    INSERT INTO item(i_name, i_unitprices, p_id)
    VALUES  ('item_a',  1,  1),
            ('item_b',  1,  1);
    """
)

conn.execute(
    """
    INSERT INTO transactions(u_id, c_id, p_id, i_id, amount)
    VALUES  (1, 1,  1,  1,  1),
            (1, 1,  1,  1,  1);
    """
)



conn.commit()
conn.close()
