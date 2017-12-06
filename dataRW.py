# -*- coding: utf-8 -*-
# author: Administrator
# createTime: 2017/5/9

import config
import json
def dataWrite(data):
    config.branches_config
    file_object = open('templates/%s/data.json' % config.branches_config, 'w')
    file_object.write(data)
    file_object.close()

def dataRead():
    with open('templates/%s/data.json' % config.branches_config) as json_file:
        return json_file
    return None

def dataReadJson():
    with open('templates/%s/data.json' % config.branches_config) as json_file:
        return json.load(json_file)
    return None

