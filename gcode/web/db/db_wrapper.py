
from .db import DB

from .. import db
class DBWrapper(DB):
    """
    db
    """
    def __init__(self,config):
        self.config = config
        db_config = config.get(config.get("generate").get("db_config"))
        self.db = db.db_map.get(db_config.get("db")).get("class")(db_config)
    def get_all(self, sql):
        return self.db.get_all(sql)

    def get_one(self, sql):
        return self.db.get_one(sql)

    def get_database(self):
        database = self.config.get("project",{}).get("database")
        database_exclude = self.config.get("project",{}).get("databaseExclude",[])
        database_list = []
        if bool(database):
            if isinstance(database, str):
                database_list.append(database)
            else:
                database_list.extend(database)
        databases = self.db.get_database()
        data = [j for j in databases if j not in database_exclude]
        exist_list = []
        for i in data:
            if i in database_list:
                data.remove(i)
                exist_list.append(i)
        for i in database_list:
            if i not in exist_list:
                database_list.remove(i)
        database_list.extend(data)
        return database_list


    def get_table(self, database):
        return self.db.get_table(database)

    def get_fields(self, database, table_name):


        return self.db.get_fields(database,table_name)


    def close_connect(self):
        self.db.close_connect()
    def connect(self):
        self.db.connect()