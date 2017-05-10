# -*- coding: utf-8 -*-
# author: Administrator
# createTime: 2017/5/9
import array


def propertyToField(property):
    field = ''
    length = len(property)
    flag = False
    for i in range(0, length):
        if property[i] == '_' and i < length:
            flag = True
        else:
            if flag:
                flag = False
                field = field + property[i].upper()
            else:
                field = field + property[i]
    return field


def fieldToProperty(field):
    property = ''
    length = len(field)
    for i in range(0, length):
        if field[i].isupper():
            property = property + "_"
        property = property + field[i]
    return property.upper()
