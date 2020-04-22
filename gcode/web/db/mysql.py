import logging

try:
    import pymysql
except Exception as e:
    logging.error(e)
class Mysql(object):
    """
    mysql处理
    """
    def __init__(self,host=None,port=None,user=None,password=None):
        cfg = {'host': host,
               'port': int(port),
               'user': user,
               'password': password,
               'charset': 'utf8'}
        self.connect_config = cfg


    def get_all(self,sql,dict_cursor = True):
        """

        :param sql:
        :return:

        """
        conn = pymysql.connect(**self.connect_config)
        if dict_cursor:
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        else:
            cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def get_database(self):
        sql="SHOW DATABASES"
        result = self.get_all(sql)
        return result


    def get_table(self,database):
        sql = "select t.TABLE_NAME as tableName,t.TABLE_COMMENT as tableComment" \
              " from information_schema.tables t where table_schema='%s'" % database
        return self.get_all(sql)


    def get_fields(self,database,table_name):
        sql = "select  COLUMN_NAME as columnName,COLUMN_COMMENT as columnComment,DATA_TYPE as columnType" \
              ",CHARACTER_MAXIMUM_LENGTH as charLength,IS_NULLABLE as isNullable  " \
              "FROM information_schema.`COLUMNS` where TABLE_NAME = '%s'  and TABLE_SCHEMA='%s' " % (table_name,database)
        return self.get_all(sql)