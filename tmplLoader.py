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

def getEntityTmpl():
    path = 'templates/%s/entity.tmpl' % templateDir
    return Template(loader.get_source("", path)[0])

def getMapperXmlTmpl():
    path = "templates/%s/mapperXml.tmpl" % templateDir
    return Template(loader.get_source("", path)[0])

def getMapperTmpl():
    path =  "templates/%s/mapper.tmpl" % templateDir
    return Template(loader.get_source("", path)[0])


def getContorllerTmpl():
    path = "templates/%s/controller.tmpl" % templateDir
    return Template(loader.get_source("", path)[0])

def getServiceTmpl():
    path = "templates/%s/service.tmpl" % templateDir
    return Template(loader.get_source("", path)[0])

def getServiceImplTmpl():
    path = "templates/%s/serviceImpl.tmpl" % templateDir
    return Template(loader.get_source("", path)[0])

def getDataTmpl():
    path = "templates/%s/data.tmpl" % templateDir
    return Template(loader.get_source("", path)[0])
