from web.service.strategy.input_handle_strategy import InputHandleStrategy
from web.util import string_util, config_util
from web.db.db_wrapper import DBWrapper


class JavaDBStrategy(InputHandleStrategy):
    """
    db 处理
    """

    def __init__(self):
        pass

    def handle(self, data, config):
        try:
            db = DBWrapper(config)
            db_java_convert = config_util.get_sys_config_json("db_java_convert")
            db_convert_jdbc_json = db_java_convert.get("db_convert_jdbc", {})
            db_convert_java_json = db_java_convert.get("db_convert_java", {})
            base_field_arr = []
            result = []
            rows = data.get("data", {}).get("rows", [])
            for r in rows:
                field_list = db.get_fields(r.get('database'), r.get('tableName'))
                if bool(field_list) is False:
                    raise Exception("无法获取[%s][%s]字段数据" % (r.get('database'), r.get('tableName')))
                for f in field_list:
                    f['field'] = string_util.property_to_field(f['columnName'])
                    f['isBaseField'] = f['field'] in base_field_arr and 'true' or 'false'
                    f['jdbcType'] = f['columnType'] and f['columnType'].upper() or None
                    if f['jdbcType'] in db_convert_jdbc_json:
                        f['jdbcType'] = db_convert_jdbc_json[f['jdbcType']]
                    f['type'] = 'String'
                    if f['jdbcType'] in db_convert_java_json:
                        f['type'] = db_convert_java_json[f['jdbcType']]
                j = {'tableName': r['tableName'], 'database': r['database'], 'className': r['className'],
                     'fields': field_list,
                     'tableAlias': r["tableAlias"], "description": r["description"],
                     'basePackage': data['data']["info"]['basePackage']}
                result.append(j)
        finally:
            if db:
                db.close_connect()
        return result

    def strategy_name(self):
        return "java_db"
