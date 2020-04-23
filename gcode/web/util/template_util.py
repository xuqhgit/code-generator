
from jinja2 import Template, FileSystemLoader
import web
from web.util import config_util
import json
from jinja2.environment import Environment
import os


env = Environment()
env.loader = FileSystemLoader(web.template_module_dir)
key_data_template = "dataTemplate"
key_modules = "modules"
key_child_module = "child"
key_module_template = "templates"
data_format_template_name = "dataFormat.json"
_cache={}

# def str_contains(source_str,contains_str):
#     if source_str is not None:
#         return source_str.find(contains_str) > -1
#     return False
#
# env.filters['contains']=str_contains
"""
    模板加载

"""



def render_template(code,template_name,context):
    path = "%s/%s/%s" % (code, web.template_fold, template_name)
    t = env.get_template(path)
    return t.render(context)


def render_data_template(code,template_name,context):
    path = "%s/%s" % (code, template_name)
    t = env.get_template(path)
    return t.render(context)

def render_str(template_str, value):
    """
    字符串模板解析
    :param template_str:
    :param value:
    :return:
    """
    template = Template(template_str)
    return template.render(value)




def render_data_template_by_modules(module_code_arr,context):
    temp_map = get_module_map()
    for code in reversed(module_code_arr):
        if code in temp_map and key_data_template  in temp_map[code] and bool(temp_map[code][key_data_template]):
            return render_data_template(code,temp_map[code][key_data_template],context)
    return None


def get_module_map():
    modules = None
    if key_modules in _cache:
        modules = _cache[key_modules]
    if modules is None:
        modules = read_module()
    module_map = {}
    def arr_handle(arr,m):
        for i in arr:
            m[i["code"]] = i
            if key_child_module in i and bool(i[key_child_module]):
                arr_handle(i[key_child_module],m)
    arr_handle(modules,module_map)
    return module_map

def get_last_module_code(module_code_arr,template_name):
    module_map = get_module_map()
    for code in reversed(module_code_arr):
        if code in module_map and key_module_template in module_map[code] and bool(module_map[code][key_module_template]):
            for t in module_map[code][key_module_template]:
                if t == template_name:
                    return code
    return None

def get_last_module_code_map(module_code_arr,template_name_arr):
    result = {}
    for name in template_name_arr:
        result[name]=get_last_module_code(module_code_arr,name)
    return result

def get_last_data_module_code(module_code_arr):
    temp_map = get_module_map()
    for code in reversed(module_code_arr):
        if code in temp_map and key_data_template in temp_map[code] and bool(temp_map[code][key_data_template]):
            return code
    return None

def read_module():
    """
    读取模板列表
    :return:
    """
    file_dir = web.template_module_dir
    temp_map = {}
    module_list=[]
    template_temp_map = {}
    for i in os.walk(file_dir):
        new_path = i[0].replace("\\","/")
        code = new_path[len(file_dir) + 1:len(new_path)]
        if file_dir == new_path:
            for item in reversed(i[1]):
                temp_map[item]={"code":item}
                module_list.append(temp_map[item])
        if config_util.config_info_ini in i[2]:
            config = config_util.get_config(new_path+"/"+config_util.config_info_ini)
            name = config.get("info","name")
            if code not in temp_map:
                temp_map[code] = { key_child_module: []}
            temp_map[code]["name"] = name
            temp_map[code][key_child_module] = []
            for item in reversed(i[1]):
                temp_map[code+"/"+item]={"code":code+"/"+item}
                temp_map[code][key_child_module].append(temp_map[code+"/"+item])
        elif config_util.config_module_ini in i[2]:
            config = config_util.get_config(new_path + "/" + config_util.config_module_ini)
            name = config.get("info","name")
            if code in temp_map:
                temp_map[code]["name"] = name
                temp_map[code][key_module_template] = []
            template_temp_map["%s/%s" % (code,web.template_fold)]= temp_map[code][key_module_template]
            if data_format_template_name in i[2]:
                temp_map[code][key_data_template]=data_format_template_name
        elif len(i[1])==0 and len(i[2])>0:
            if template_temp_map[code] is not None:
                template_temp_map[code].extend(reversed(i[2]))
    _cache[key_modules]=module_list
    return module_list



if __name__=="__main__":
    read_module()


