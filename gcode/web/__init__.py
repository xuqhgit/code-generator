# -*- coding: utf-8 -*-
import logging
import os
from flask import Flask




app = Flask(__name__,template_folder="templates")
app.secret_key = os.urandom(24)
app = Flask(__name__)



_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
web_dir = os.path.dirname(__file__)
_log_dir = os.path.join(_dir, 'logs')
template_module = web_dir+"/template_module"

template_fold = "template"
workplace = web_dir+"/static/workspace"

if not os.path.isdir(_log_dir):
    os.makedirs(_log_dir)
# 设置默认的level为DEBUG
# 设置log的格式
logging.basicConfig(
    level=logging.DEBUG,
    filename=_log_dir + '/gcode.log',
    filemode='w'
)
#################################################################################################
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)



from web import view
from web import views

