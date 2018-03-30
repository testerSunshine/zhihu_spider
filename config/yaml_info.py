# -*- coding: utf8 -*-
__author__ = 'MR.wen'
import yaml
import os


def _get_yaml():
    """
    解析yaml
    :return: s  字典
    """
    path = os.path.join(os.path.dirname(__file__) + '/config.yaml')
    f = open(path)
    s = yaml.load(f)
    f.close()
    return s


def _get_yaml_local(yaml_name):
    """
    解析本地yaml
    :return:
    """
    path = os.path.join('/usr/local/{0}'.format(yaml_name))
    f = open(path)
    s = yaml.load(f)
    f.close()
    return s


if __name__ == "__main__":
    print _get_yaml_local("zhihu_login.yaml")