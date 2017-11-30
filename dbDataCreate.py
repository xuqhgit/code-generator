# -*- coding: utf-8 -*-
# author: Administrator
# createTime: 2017/5/9
import config
import db
import stringUtil
import tmplLoader
import sys

reload(sys)
sys.setdefaultencoding('utf8')

tables = config.get('info', 'tables')
basePackage = config.get('info', 'basePackage')
baseEntity = config.get('info', 'baseEntity')
author = config.get('info', 'author')
baseFields = config.get('info', 'baseFields')
db_type = str(config.get('db', 'type')).upper()
baseFieldsArr = []
if baseFields:
    baseFieldsArr = baseFields.split(",")
arr = tables.split(";")
result = []
for a in arr:
    d = a.split(",", 2)
    length = len(d)
    table_name = None
    table_alias = None

    if length == 2:
        table_name = d[0]
        table_alias = d[1]
    else:
        table_name = d[0]
        table_alias = stringUtil.propertyToField(table_name)
    data = db.getColInfo(table_name)
    for f in data:
        f['dbField'] = f['DBFIELD']
        f['comments'] = f['COMMENTS']

        f['field'] = stringUtil.propertyToField(f['dbField'].find('_') == -1 and f['dbField'] or f['dbField'].lower())
        f['isBaseField'] = f['field'] in baseFieldsArr and 'true' or 'false'
        f['title'] = ''
        f['required'] = 'false'
        f['requiredMessage'] = '必填项'
        f['pattern'] = ''
        f['patternMessage'] = ''
        # equal like gt lt
        f['searchFieldType'] = ''
        f['addField'] = 'true'
        f['editField'] = 'false'
    j = {'table': table_name, 'className': table_alias, 'fields': data, "db": db_type,
         'author': author, 'basePackage': basePackage, 'package': '%s.%s' % (basePackage, baseEntity)}
    result.append(j)
template = tmplLoader.getTmpl("data")
dataStr = template.render(list=result)
file_object = open('data.json', 'w')
file_object.write(dataStr)
file_object.close()
