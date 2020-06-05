import logging
from .db import DB
try:
    import pymysql
except Exception as e:
    logging.error(e)

class Mysql(DB):
    """
    mysql处理
    """

    def __init__(self,db_config):
        self.conn = None
        self.connect_config = {'host': db_config.get("host"),
                               'port': int(db_config.get("port", 3306)),
                               'user': db_config.get("user"),
                               'password': db_config.get("password"),
                               'charset': 'utf8'}

    def get_one(self, sql):
        pass

    def get_all(self, sql):
        """

        :param sql:
        :return:

        """
        cursor = self.connect().cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        return data

    def get_database(self):
        sql = "SHOW DATABASES"
        cursor = self.connect().cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        result_list = [j[0] for j in data]
        self.close_connect()
        return result_list

    def get_table(self, database):
        sql = "select t.TABLE_NAME as tableName,t.TABLE_COMMENT as tableComment" \
              " from information_schema.tables t where table_schema='%s'" % database
        result = self.get_all(sql)
        self.close_connect()
        return result

    def get_fields(self, database, table_name):
        sql = "select  COLUMN_NAME as columnName,COLUMN_COMMENT as columnComment,DATA_TYPE as columnType" \
              ",CHARACTER_MAXIMUM_LENGTH as charLength,IS_NULLABLE as isNullable  " \
              "FROM information_schema.`COLUMNS` where TABLE_NAME = '%s'  and TABLE_SCHEMA='%s' " \
              % (table_name, database)
        return self.get_all(sql)

    def close_connect(self):
        self.conn.close()

    def connect(self):
        if self.conn is None:
            self.conn = pymysql.connect(**self.connect_config)
        return self.conn