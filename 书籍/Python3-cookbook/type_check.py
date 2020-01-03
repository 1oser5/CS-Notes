#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   type_check.py
@Time    :   2020/01/03 10:28:22
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   创建类描述器来进行类型检查
'''

# here put the import lib
class Typed(object):
    """ 类描述器 """
    def __init__(self, name, expected_type):
        """ 初始化
        
        param: str name 变量名 
        param: str expected_type 期望类型
        """
        self.name = name
        self.expected_type = expected_type
    def __get__(self, instance, cls):
        if instance is None: # 调用类属性时，instance 为空，只需要返回自身即可
            return self
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if isinstance(value, self.expected_type):
            raise TypeError('Expected' + str(self.expected_type))
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        del instance.__dict__[self.name]
def typeassert(**kwargs):
    """ 类装饰器 """
    def decorate(cls):
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate
@typeassert(name=str, shares=int, price=float)
class Stock(object):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
if __name__ == '__main__':
    pass