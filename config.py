# -*- coding: utf-8 -*-
# author: Administrator
# createTime: 2017/5/9
import ConfigParser


base_config_name = "config.conf"
bcp = ConfigParser.SafeConfigParser()
bcp.read(base_config_name)
branches_config=bcp.get("info", "config")
branches_config_name = "templates/%s/config.conf" % branches_config
cp = ConfigParser.SafeConfigParser()
cp.read(branches_config_name)


def get(s, k):
    return cp.get(s, k)


