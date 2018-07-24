#!/usr/bin/env python

# -*- coding: utf-8 -*-

import pymysql

# db = pymysql.connect('localhost', 'root', '123456', 'zhongmiao')

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'zhongmiao',
    'charset': 'utf8'
}
db = pymysql.connect(**config)

cursor = db.cursor()

# cursor.execute("select version()")

sql = 'SELECT weibo_id,weibo_name,url FROM `k_kol` LIMIT 5'
cursor.execute(sql)

data = cursor.fetchall()

# print(dir(data))
print(data)

db.close()
# print( dir(cursor) )
