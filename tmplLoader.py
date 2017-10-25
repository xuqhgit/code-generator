# -*- coding: UTF-8 -*-
from jinja2 import Template, FileSystemLoader
import os
import config

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
            t = Template(loader.get_source("", path)[0])
        except BaseException, e:
            print path, e.message
        if t:
            break
    return t
