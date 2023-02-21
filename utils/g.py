# -*- coding: utf-8 -*-
# @author: chenhaibing
# @contact: chenhaibing@tal.com
# @Time : 2023/1/11 15:40

def _init():
    global _global_dict
    _global_dict = {}

def set_value(key,value):
    #定义全局变量
    _global_dict[key] = value

def get_value(key):
    #获取全局变量
    try:
        return _global_dict[key]
    except KeyError:
        return '不存在的key'
