# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, redirect, request, session
import logging
from web.ui import *
from web.util import  file_util
from web import result
bp = Blueprint('user', __name__, template_folder='template', static_folder='static', url_prefix='/user')



@bp.route("/getLatestZip", methods=['post', 'get'])
@json_view
def create():
    args = request.args
    if request.method == 'POST':
        args = request.form
    zip_list = []
    try:
        user_zip_list = file_util.get_user_zip(args.get("token","00001"))
        for z in user_zip_list:
            zip_list.append({"path":z[0]+"/"+z[1],"name":z[1]})
    except Exception as e:
        logging.error(e)
        return result.error(message=e)
    return result.success(data=zip_list)
