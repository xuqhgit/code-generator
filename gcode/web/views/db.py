from flask import Blueprint
from web.ui import *
from web.util import config_util
from web.db import mysql


bp = Blueprint('db', __name__, template_folder='template', static_folder='static', url_prefix='/db')


@bp.route("/getDatabase", methods=['post', 'get'])
@json_view
def get_database():
    args =  get_args()
    code = args.get("code")
    config, config_ext = config_util.get_extend_config_json(code)
    try:
        db = mysql.Mysql(**config.get("mysql"))
        return db.get_database()
    except Exception as e:
        print(e)
    return []



@bp.route("/getFields/<table>", methods=['post', 'get'])
@json_view
def get_fields():
    args = get_args()
    try:
        pass

    except Exception as e:
        pass
    return ""

@bp.route("/getTables/<database>", methods=['post', 'get'])
@json_view
def get_tables(database):
    args = get_args()
    code = args.get("code")
    config, config_ext = config_util.get_extend_config_json(code)
    try:
        db = mysql.Mysql(**config.get("mysql"))
        return db.get_table(database)
    except Exception as e:
        print(e)
    return []

def get_args():
    args = request.args
    if request.method == 'POST':
        args = request.form
    return args