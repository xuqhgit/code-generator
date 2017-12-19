# -*- coding: UTF-8 -*-

import json
import time
import tmplLoader
import dataRW
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')
src_root_path = "src"
config_dir = 'config'
page_dir = 'jsp'


def load():
    return dataRW.dataReadJson()


def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)


def writeFile(dirPath, str, fileName, fileType):
    path = ''
    if fileType == 'java':
        path = './%s/%s' % (src_root_path, dirPath.replace(".", "/"))
    elif fileType == 'jsp':
        path = './%s/%s' % (src_root_path, page_dir + "/" + dirPath.replace(".", "/"))
    else:
        path = './%s/%s' % (src_root_path, config_dir)
    mkdir(path)
    file_object = open('%s/%s.%s' % (path, fileName, fileType), 'w')
    file_object.write(str)
    file_object.close()


def firstLetterUpper(value):
    return value.replace(value[0], value[0].upper(), 1)


def firstLetterLower(value):
    return value.replace(value[0], value[0].lower(), 1)


def setDbFields(data):
    dbFields = []
    for f in data['fields']:
        if f['isDbField']:
            dbFields.append(f)
    data['dbFields'] = dbFields


def handleData(data):
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    data['date'] = date
    data['className'] = firstLetterUpper(data['className'])
    data['sClassName'] = firstLetterLower(data['className'])
    for fj in data['fields']:
        fj['upperName'] = firstLetterUpper(fj['name'])

    if 'basePackage' not in data or data['basePackage'] == '':
        data['basePackage'] = data['package'][0:data['package'].rindex('.')]
    data['mapperPackage'] = data['basePackage'] + '.mapper'
    data['servicePackage'] = data['basePackage'] + '.service'
    data['serviceImplPackage'] = data['basePackage'] + '.service.impl'
    data['controllerPackage'] = data['basePackage'] + '.controller'
    data['dtoPackage'] = data['basePackage'] + '.dto'

    data['mapperClass'] = data['className'] + 'Mapper'
    data['sMapperClass'] = data['sClassName'] + 'Mapper'

    data['serviceClass'] = "I" + data['className'] + 'Service'
    data['sServiceClass'] = data['sClassName'] + 'Service'

    data['serviceImplClass'] = data['className'] + 'ServiceImpl'
    data['sServiceImplClass'] = data['sClassName'] + 'ServiceImpl'

    data['controllerClass'] = data['className'] + 'Controller'
    data['sControllerClass'] = data['sClassName'] + 'Controller'

    data['dtoClass'] = data['className'] + 'DTO'
    data['sDtoClass'] = data['sClassName'] + 'DTO'

    setDbFields(data)


data = load()

entityTemplate = tmplLoader.getTmpl("entity")
mapperXmlTemplate = tmplLoader.getTmpl("mapperXml")
mapperTemplate = tmplLoader.getTmpl("mapper")
serviceTemplate = tmplLoader.getTmpl("service")
serviceImplTemplate = tmplLoader.getTmpl("serviceImpl")
controllerTemplate = tmplLoader.getTmpl("controller")
addTemplate = tmplLoader.getTmpl("add")
editTemplate = tmplLoader.getTmpl("edit")
indexTemplate = tmplLoader.getTmpl("index")
validConstantTemplate = tmplLoader.getTmpl("validConstant")
dtoTemplate = tmplLoader.getTmpl("dto")
extTemplate = tmplLoader.getExtTemplate()

for j in data:
    if j['className']:
        handleData(j)

        if entityTemplate:
            javaStr = entityTemplate.render(j)
            writeFile(j['package'], javaStr, j['className'], 'java')
        if dtoTemplate:
            dtoStr = dtoTemplate.render(j)
            writeFile(j['dtoPackage'], dtoStr, j['dtoClass'], 'java')

        if mapperXmlTemplate:
            mapperXmlStr = mapperXmlTemplate.render(j)
            writeFile(j['package'], mapperXmlStr, j['mapperClass'], 'xml')

        if mapperTemplate:
            mapperStr = mapperTemplate.render(j)
            writeFile(j['mapperPackage'], mapperStr, j['mapperClass'], 'java')

        if serviceTemplate:
            serviceStr = serviceTemplate.render(j)
            writeFile(j['servicePackage'], serviceStr, j['serviceClass'], 'java')

        if serviceImplTemplate:
            serviceImplStr = serviceImplTemplate.render(j)
            writeFile(j['serviceImplPackage'], serviceImplStr, j['serviceImplClass'], 'java')

        if controllerTemplate:
            controllerStr = controllerTemplate.render(j)
            writeFile(j['controllerPackage'], controllerStr, j['controllerClass'], 'java')

        if addTemplate:
            addStr = addTemplate.render(j)
            writeFile(j['sClassName'], addStr, 'add', 'jsp')
        if editTemplate:
            editStr = editTemplate.render(j)
            writeFile(j['sClassName'], editStr, 'edit', 'jsp')

        if indexTemplate:
            indexStr = indexTemplate.render(j)
            writeFile(j['sClassName'], indexStr, 'index', 'jsp')

        if extTemplate:
            for e in extTemplate:
                extJson = extTemplate[e]
                tmplStr = extJson['template'].render(j)
                writeFile(tmplLoader.renderStr(extJson['path'], j), tmplStr, tmplLoader.renderStr(extJson["fileName"], j),
                          extJson['type'])
    pass
