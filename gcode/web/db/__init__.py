import importlib
import os
from . import db
from . import db_wrapper

db_map={}
def init():
    for p, f, file_list in os.walk(os.path.abspath(os.path.join(os.path.dirname(__file__), os.curdir))):
        for _file in file_list:
            arr = _file.split(".")
            file_name = arr[0]
            file_type = arr[1]
            if file_type == "py" and file_name != "__init__" and file_name != "db" and file_name != "db_wrapper":
                importlib.import_module("."+file_name,package=__name__)
    for cl in db.DB.__subclasses__():
        if cl.__name__!=db_wrapper.DBWrapper.__name__:
            db_map[cl.__name__]={"code":cl.__name__,"name":cl.__name__,"class":cl}


init()