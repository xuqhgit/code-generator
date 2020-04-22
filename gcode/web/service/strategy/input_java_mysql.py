
from web.service.strategy.input_handle_strategy import InputHandleStrategy
from web.db import  mysql
from web.util import string_util,config_util


class JavaMysqlStrategy(InputHandleStrategy):
    """
    mysql 数据处理
    """
    def __init__(self):
        pass
    def handle(self,data,config):
        mysql_json = config["mysql"]
        cfg = {'host': mysql_json["host"],
               'port': int(mysql_json["port"]),
               'user': mysql_json["user"],
               'password': mysql_json["password"]
               }
        my = mysql.Mysql(**cfg)
        mysql_java_convert = config_util.get_sys_config_json("mysql_java_convert")
        mysql_convert_jdbc_json= mysql_java_convert["mysql_convert_jdbc"]
        jdbc_convert_java_json= mysql_java_convert["jdbc_convert_java"]
        base_field_arr = []
        result = []
        rows = data['data']['rows']
        for r in rows:
            field_list  = my.get_fields(r['database'],r['tableName'])
            if bool(field_list) is False:
                raise Exception("无法获取[%s][%s]字段数据" % (r['database'],r['tableName']))
            for f in field_list:
                f['field'] = string_util.property_to_field(f['columnName'])
                f['isBaseField'] = f['field'] in base_field_arr and 'true' or 'false'
                f['jdbcType'] = f['columnType'] and f['columnType'].upper() or None
                if f['jdbcType'] in mysql_convert_jdbc_json:
                    f['jdbcType'] = mysql_convert_jdbc_json[f['jdbcType']]
                f['type'] = 'String'
                if f['jdbcType'] in jdbc_convert_java_json:
                    f['type'] = jdbc_convert_java_json[f['jdbcType']]

            j = {'tableName': r['tableName'],'database':r['database'], 'className': r['className'], 'fields': field_list,
                 'tableAlias': r["tableAlias"], "description": r["description"], 'basePackage': data['data']["info"]['basePackage']}
            result.append(j)
        return result

    def strategy_name(self):
        return "java-mysql"
