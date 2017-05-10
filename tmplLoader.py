# -*- coding: UTF-8 -*-
from jinja2 import Template, FileSystemLoader
import os

_dir = os.path.dirname(__file__)
loader = FileSystemLoader(_dir)


def getEntityTmpl():
    return Template(loader.get_source("", "templates/entityTmpl/entity.tmpl")[0])

def getMapperXmlTmpl():
    return Template(loader.get_source("", "templates/entityTmpl/mapperXml.tmpl")[0])

def getMapperTmpl():
    return Template(loader.get_source("", "templates/entityTmpl/mapper.tmpl")[0])


def getContorllerTmpl():
    return Template(loader.get_source("", "templates/entityTmpl/controller.tmpl")[0])

def getServiceTmpl():
    return Template(loader.get_source("", "templates/entityTmpl/service.tmpl")[0])

def getServiceImplTmpl():
    return Template(loader.get_source("", "templates/entityTmpl/serviceImpl.tmpl")[0])

def getDataTmpl():
    return Template(loader.get_source("", "templates/entityTmpl/data.tmpl")[0])
