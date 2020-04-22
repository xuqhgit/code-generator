# -*- coding: utf-8 -*-
import importlib
import os
from web import app


def init():

    for p, f, file_list in os.walk(os.path.abspath(os.path.join(os.path.dirname(__file__), os.curdir))):
        for  _file in file_list:
            arr = _file.split(".")
            file_name = arr[0]
            file_type = arr[1]
            if file_type == "py" and file_name != "__init__":
                module = importlib.import_module("."+file_name,package=__name__)
                app.register_blueprint(module.bp)

init()
