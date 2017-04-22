import sqlite3

conn = sqlite3.connect('test.db')

#print "Open Database Successfully!"

"""
product info table
"""

conn.execute(
    '''
        create table product
        (
            p_id        integer     primary key    autoincrement,
            p_name      char(60)    not null,
            author_name char(10)
        )
        ;
    '''
)

#print "product info table created Successfully!"

"""
item info table
"""

conn.execute(
    '''
        create table item
        (
            i_id            integer         primary key    autoincrement,
            i_name          char(90)    not null,
            i_minutes       int         not null,
            i_unitprices    float       not null,
            i_prices        float       not null,
            p_id            int         not null,
            foreign key     (p_id)      references      product(p_id)
        )
        ;
    '''
)

#print "item info table created Successfully!"

"""
product / item info table
"""

conn.execute(
    '''
        create table pi
        (
            i_id            int         not null,
            p_id            int         not null,
            foreign key     (p_id)      references      product(p_id),
            foreign key     (i_id)      references      item(i_id),
            primary key     (i_id, p_id)
        )
        ;
    '''
)

#print "product / item info table created Successfully!"

"""
community info table
"""

conn.execute(
    '''
        create table community
        (
            c_id            integer         primary key    autoincrement,
            c_name          char(30)    not null
        )
        ;
    '''
)

#print "community info table created Successfully!"


"""
user info table
"""


conn.execute(
    '''
        create table user
        (
            u_id            integer         primary key    autoincrement,
            u_name          char(30)    not null,
            u_role          char(10)    not null,
            u_password      char(30)    not null,
            u_phone         char(30)    not null,
            c_id            int         not null,
            foreign key     (c_id)      references   community(c_id)
        )
        ;
    '''
    )

#print "user info table created Successfully!"

"""
transactions info table
"""


conn.execute(
    '''
        create table transactions
        (
            t_id            integer         primary key autoincrement,
            u_id            int         not null,
            c_id            int         not null,
            p_id            int         not null,
            i_id            int         not null,
            amount          int,
            timestamp       datetime    default(datetime('now', 'localtime')),
            foreign key     (u_id)      references   user(u_id),
            foreign key     (c_id)      references   community(c_id),
            foreign key     (p_id)      references   product(p_id),
            foreign key     (i_id)      references   item(i_id)
        )
        ;
    '''
    )

#print "transactions info table created Successfully!"


"""
admin info table
"""

conn.execute(
    '''
        create table admin
        (
            c_id            int         not null,
            u_id            int         not null,
            foreign key     (c_id)      references      community(c_id),
            foreign key     (u_id)      references      user(u_id),
            primary key     (c_id, u_id)
        )
        ;
    '''
)

#print "admin info table created Successfully!"

conn.execute(
    '''
        select * from item;
    '''
    )
