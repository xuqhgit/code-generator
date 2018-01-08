# -*- coding: utf-8 -*-
# author: Administrator
# createTime: 2017/5/9
import ConfigParser

base_config_name = "config.conf"
bcp = ConfigParser.SafeConfigParser()
bcp.read(base_config_name)
branches_config = bcp.get("info", "config")
branches_config_name = "templates/%s/config.conf" % branches_config
cp = ConfigParser.SafeConfigParser()
cp.read(branches_config_name)


def get(s, k):
    """
    获取子某块信息
    :param s:
    :param k:
    :return:
    """
    try:
        return cp.get(s, k)
    except Exception, e:
        print("获取配置信息异常:%s" % e)
        print("未获取到 %s-->%s" % (s,k))
    return None


def getMainConfig(s, k):
    """
    获取主配置信息
    :param s:
    :param k:
    :return:
    """
    try:
        return bcp.get(s, k)
    except Exception, e:
        print("获取配置信息异常:%s" % e)
        print("未获取到 %s-->%s" % (s,k))
    return None
