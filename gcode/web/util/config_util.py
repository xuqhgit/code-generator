import configparser
import web
import json

config_info_ini = "info.ini"
config_module_ini = "module.ini"
_cache = {}


def get_config(path):
    config = configparser.ConfigParser()
    config.read(path, encoding="utf-8-sig")
    return config


def get_extend_config_json(module_code):
    cur_config = get_config_json_by_code(module_code)
    parent_module_code = cur_config.get("generate", {}).get("parent_module", [])
    ext_info = {}
    if bool(parent_module_code) is None:
        return cur_config, ext_info
    for code in reversed(parent_module_code):
        j = get_config_json_by_code(code)
        for k in j:
            if k not in cur_config:
                cur_config[k] = j[k]
                ext_info[k] = code
    return cur_config, ext_info


def get_sys_config_json(code):
    config = get_config(web.web_dir + "/config.ini")
    return get_section_json(config, code)


def get_section_json(config, section):
    options = config.options(section)
    result = {}
    for k in options:
        if k.find("/json") > -1 and bool(config.get(section, k)):
            try:
                result[k.replace("/json", "")] = json.loads(config.get(section, k))
            except Exception as e:
                raise Exception("exception : key:%s value:%s " % (k, config.get(section, k)))
            continue
        result[k] = config.get(section, k)
    return result


def get_config_json_by_code(code):
    config = get_config_by_code(code)
    return get_config_json_by_config(config)


def get_config_json_by_config(config):
    sections = config.sections()
    result = {}
    for s in sections:
        result[s] = get_section_json(config, s)
    return result


def analysis_config_str(content):
    config_parser = configparser.ConfigParser()
    config_parser.read_string(content)
    return get_config_json_by_config(config_parser)


def get_config_by_code(code):
    return get_config("%s/%s/%s" % (web.template_module_dir, code, config_module_ini))
