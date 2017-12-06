# -*- coding: utf-8 -*-
# author: Administrator
# createTime: 2017/5/9


import os
import sys

import mysql.connector as connor
import config
import cx_Oracle

reload(sys)
sys.setdefaultencoding('utf8')
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'



or_col_sql = "select COLUMN_NAME as DBFIELD,comments as COMMENTS from user_col_comments where Table_Name='%s' "

my_col_sql = "select  COLUMN_NAME as DBFIELD,COLUMN_COMMENT as COMMENTS,DATA_TYPE as dataType  FROM information_schema.`COLUMNS` where TABLE_NAME = '%s'  and TABLE_SCHEMA='%s' "

db_type = str(config.get('db', 'type')).upper()
host = config.get('db', 'host')
user = config.get('db', 'user')
password = config.get('db', 'password')
database = config.get('db', 'database')
port = config.get('db', 'port')
conn = None


def getColInfo(table):
    if db_type == 'ORACLE':

        conn = cx_Oracle.connect('%s/%s@%s' % (user, password, host))
        cursor = conn.cursor()
        sql = or_col_sql
        _sql = sql % table.upper()
        pass
    elif db_type == 'MYSQL':
        cfg={'host': host, 'user': user, 'password': password, 'port': port,
                                        'database': database, 'charset': 'utf8'}
        conn = connor.connect(**cfg)
        # conn = MySQLdb.connect(host=host,user=user,passwd=password, db=db, charset="utf8")
        cursor = conn.cursor(dictionary=True)
        sql = my_col_sql
        _sql = sql % (table, database)
    # 使用cursor()方法获取操作游标


    # 使用execute方法执行SQL语句
    cursor.execute(_sql)
    data = cursor.fetchall()
    dict_rows = []
    if db_type == 'ORACLE':
        dict_keys = [r[0] for r in cursor.description]
        for row in data:
            if row[1]:
                r = (row[0], row[1].decode('gbk'))
            else:
                r = (row[0], row[1])
            dict_rows.append(dict(zip(dict_keys, r)))
        data = dict_rows
    cursor.close()
    conn.close()
    return data



