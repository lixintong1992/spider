# coding=utf-8

import MySQLdb

_author__ = 'Lust'


def my_function():
    conn = MySQLdb.Connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='imooc', charset='utf8')
    cursor = conn.cursor()

    # sql = 'select * from user'
    sql_create = "CREATE TABLE music(music_id INT(20) NOT NULL,music_name VARCHAR(100) DEFAULT NULL,PRIMARY KEY(music_id))"
    sql_insert = "INSERT INTO music(music_id,music_name) VALUES(-1,'e2')"
    sql_update = "update user set username='name91' where userid=4"
    sql_delete = "delete from user where userid>6"
    try:
        # cursor.execute(sql)
        # cursor.execute(sql_create)
        cursor.execute(sql_insert)
        # print cursor.rowcount
        # cursor.execute(sql_update)
        # print cursor.rowcount
        # cursor.execute(sql_delete)
        # print cursor.rowcount
        conn.commit()
    except Exception as e:
        print e
        conn.rollback()

    # rs = cursor.fetchone()
    # rs = cursor.fetchmany(3)
    # rs = cursor.fetchall()
    # print rs

    cursor.close()
    conn.close()
    # return rs

if __name__ == '__main__':
    # rs = my_function()
    my_function()
