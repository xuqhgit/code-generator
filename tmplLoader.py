# -*- coding: UTF-8 -*-
from jinja2 import Template, FileSystemLoader
import os
import config
import json
from jinja2.environment import Environment

env = Environment()
env.loader = FileSystemLoader('.')

_dir = os.path.dirname(__file__)
loader = FileSystemLoader(_dir)

baseTemplateDir = 'base'
templateDir = config.get("info", 'template')
if templateDir is None:
    templateDir = baseTemplateDir
templateDirArr = templateDir.split(",")


def getTmpl(templateName):
    t = None
    for i in reversed(templateDirArr):
        path = "templates/%s/%s.tmpl" % (i, templateName)
        try:
            # t = Template(loader.get_source("", path)[0])
            t = env.get_template(path)
        except BaseException, e:
            print path, e.message
        if t:
            return t
    return t

def getPathTmpl(path,templateName):
    path = "templates/%s/%s.tmpl" % (path, templateName)
    t = env.get_template(path)
    return t


def renderStr(templateStr, value):
    """
    字符串模板解析
    :param templateStr:
    :param value:
    :return:
    """
    template = Template(templateStr)
    return template.render(value)


def getExtTemplate():
    """
    获取扩展的模板
    :return:
    """
    with open('templates/%s/extTemplate.json' % templateDirArr[len(templateDirArr)-1]) as json_file:
        if json_file is None:
            return
        extArr = json.load(json_file)
    extJson = {}
    for ext in extArr:
        e = {}
        name = ext[0]
        type = ext[1]
        tmpl = getTmpl(name)
        if tmpl is None:
            continue
        e['template'] = tmpl
        e['type'] = type
        e['path'] = ext[2] and ext[2] or 'other'
        e['fileName'] = ext[3] and ext[3] or type + '_'
        extJson[name] = e
    return extJson


