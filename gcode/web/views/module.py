# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, redirect, request, session

from web.ui import *
import web
from web.util import config_util, template_util, file_util
from web.service.generator import generator_map,Generator

from web import result
import os

bp = Blueprint('module', __name__, template_folder='template', static_folder='../' + web.template_module,
               static_url_path='/static', url_prefix='/module')


@bp.route("/page/get", methods=['post', 'get'])
def create():
    args = request.args
    ctx = {}
    if request.method == 'POST':
        args = request.form
    code = args.get("code")
    config, config_ext = config_util.get_extend_config_json(code)
    try:
        templates = config.get("templates", {})
        parent_module_code = config_util.get_parent_module_code_arr(config,code)
        # template_util.get_last_module_code_map(parent_module_code, [t for t in templates])
        template_list = []
        latest_data_format_module_code = template_util.get_last_data_module_code(parent_module_code)
        for t in templates:
            module_code = template_util.get_last_module_code(parent_module_code, t)
            module_code = module_code is None and code or module_code
            template_list.append({"name": t, "moduleCode": module_code, "alias": t.replace(".", "_")})
        ctx["configMap"] = config
        ctx["configMapExt"] = config_ext
        ctx["templateList"] = template_list
        ctx["dataFormatModuleCode"] = latest_data_format_module_code
        ctx["user"] = {"account":"00001"}
        ctx["inputTemplate"] = config.get("generate", {}).get("input_template", "")
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
    return result.success()


@bp.route("/config/edit", methods=['post'])
@json_view
def config_edit():
    args = request.form
    module_code = args.get("moduleCode")
    content = args.get("content")
    config_util.analysis_config_str(content)
    file_util.edit_file_content(module_code, config_util.config_module_ini, content)
    return result.success()

@bp.route("/dataFormat/edit", methods=['post'])
@json_view
def data_format_edit():
    args = request.form
    # 修改后需要刷一下config json数据
    module_code = args.get("moduleCode")
    content = args.get("content")
    file_util.edit_file_content(module_code, template_util.data_format_template_name, content)
    return result.success()

@bp.route("/generate", methods=['post'])
@json_view
def generate():
    args = request.json
    code = args['code']
    config, config_ext = config_util.get_extend_config_json(code)
    generator = generator_map.get(config.get("generate").get("generator",Generator.__name__)).get("object")
    generator.generate(args)
    zip_path = file_util.create_zip(code, args.get("account"))
    module_code = args["code"].replace("/", "_")
    files, path_prefix = get_file_path_list(module_code, args["account"])
    return result.success(data={"zip": zip_path.split(web.web_dir)[1], "files": files, "pathPrefix": path_prefix})


def get_zip(module_code, account):
    return ("%s/%s/%s/%s.zip" % (web.workspace_dir, account, module_code, account)).split(web.web_dir)[1]


def get_file_path_list(module_code, account):
    path = "%s/%s/file/%s" % (web.workspace_dir, account, module_code)
    files = []
    for main_dir, sub_dir, file_name_list in os.walk(path):
        for filename in file_name_list:
            _main_dir = main_dir.replace("\\", "/")
            file_path = os.path.join(_main_dir, filename)
            files.append(file_path.replace("\\", "/").split(path+"/")[1])
    return files, "/%s/%s/file/%s/" % (web.static_workspace, account, module_code)
