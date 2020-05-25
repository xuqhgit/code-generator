# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, redirect, request, session

from web.ui import *
from web.util import  file_util

bp = Blueprint('user', __name__, template_folder='template', static_folder='static', url_prefix='/user')



@bp.route("/getLatestZip", methods=['post', 'get'])
@json_view
def create():
    args = request.args
    if request.method == 'POST':
        args = request.form
    zip_list = []
    try:
        _list = file_util.get_user_zip(args.get("user","00001"))
        for z in _list:
            zip_list.append({"path":z[0]+"/"+z[1],"name":z[1]})
    except Exception as e:
        print(e)
    return {"code":0,"data":zip_list}
