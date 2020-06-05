# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, redirect, request, session

from web.ui import *
from web import result
import logging
bp = Blueprint('template', __name__, template_folder='template', static_folder='static', url_prefix='/template')



@bp.route("/create", methods=['post', 'get'])
@json_view
def create():
    args = request.args

    if request.method == 'POST':
        args = request.form
    try:
        pass
    except Exception as e:
        logging.error(e)
        return result.error(message=e)
    return result.success()


@bp.route("/data", methods=['post'])
@json_view
def data():
    args = request.args
    if request.method == 'POST':
        args = request.form
    try:
        pass

    except Exception as e:
        pass
    return ""