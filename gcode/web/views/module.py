# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, redirect, request, session

from web.ui import *
import web
from web.util import config_util, template_util, file_util
from web.service import generator

import os

bp = Blueprint('module', __name__, template_folder='template', static_folder='../' + web.template_module,
               static_url_path='/static', url_prefix='/module')


@bp.route("/page/get", methods=['post', 'get'])
def create():
    args = request.args
    ctx = {}
    if request.method == 'POST':
        args = request.form
    try:
        code = args.get("code")
        config, config_ext = config_util.get_extend_config_json(code)
        templates = config.get("templates", {})
        parent_module_code = config.get("generate", {}).get("parent_module", [])
        parent_module_code.append(code)
        template_util.get_last_module_code_map(parent_module_code, [t for t in templates])
        template_list = []
        for t in templates:
            module_code = template_util.get_last_module_code(parent_module_code, t)
            module_code = module_code is None and code or module_code
            template_list.append({"name": t, "moduleCode": module_code, "alias": t.replace(".", "_")})
        ctx["configMap"] = config
        ctx["configMapExt"] = config_ext
        ctx["templateList"] = template_list
        ctx["inputTemplate"] = "mysqlJava"
        ctx["code"] = code

    except Exception as e:
        print(e)

    return render_template("html/generate/frame.html", ctx=ctx)


@bp.route("/template/edit", methods=['post'])
@json_view
def template_edit():
    args = request.form
    module_code = args.get("moduleCode")
    file_name = args.get("fileName")
    content = args.get("content")
    file_util.edit_file_content("%s%s" % (module_code, "/template"), file_name, content)
    return {"code": "ee"}


@bp.route("/config/edit", methods=['post'])
@json_view
def config_edit():
    args = request.form
    module_code = args.get("moduleCode")
    content = args.get("content")
    config_util.analysis_config_str(content)
    file_util.edit_file_content(module_code, config_util.config_module_ini, content)


@bp.route("/dataFormat/edit", methods=['post'])
@json_view
def data_format_edit():
    args = request.form
    module_code = args.get("moduleCode")
    content = args.get("content")
    file_util.edit_file_content(module_code, template_util.data_format_template_name, content)


@bp.route("/generate", methods=['post'])
@json_view
def generate():
    args = request.json

    generator.Generator().generate(args)

    module_code = args["code"].replace("/", "_")
    files , pathPrefix = get_file_path_list(module_code, args["account"])
    return {"zip": get_zip(module_code, args["account"]), "files": files,"pathPrefix":pathPrefix}


def get_zip(module_code, account):
    return ("%s/%s/%s/%s.zip" % (web.workspace_dir, account, module_code, account)).split(web.web_dir)[1]


def get_file_path_list(module_code, account):
    path = "%s/%s/%s/file" % (web.workspace_dir, account, module_code)
    files = []
    for main_dir, sub_dir, file_name_list in os.walk(path):
        for filename in file_name_list:
            _main_dir = main_dir.replace("\\", "/")
            file_path = os.path.join(_main_dir, filename)
            files.append(file_path.split(path)[1])
    return files , "/%s/%s/%s/file" % (web.static_workspace , account, module_code)
