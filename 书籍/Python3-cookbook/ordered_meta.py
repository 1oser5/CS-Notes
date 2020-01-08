#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   ordered_meta.py
@Time    :   2020/01/08 10:15:32
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用元类实现记录类属性定义顺序
'''

# here put the import lib
from collections import OrderedDict

class Type(object):
    _excepted_type = type(None)
    def __init__(self, name=None):
        self._name = name
    def __set__(self, instance, value):
        if not isinstance(value, self._excepted_type):
            raise TypeError(f'Excepted {self._excepted_type}')
        instance.__dict__[self._name] = value
class Ingter(Type):
    _excepted_type = int
class Float(Type):
    _excepted_type = float
class String(Type):
    _excepted_type = str
class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        print(clsdict)
        for name, value in clsdict.items():
            if isinstance(value, Type):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)
    @classmethod
    def __prepare__(cls, clsname, bases):
        return OrderedDict()
class Structure(metaclass=OrderedMeta):
    def p(self):
        print(self._order)
class Stock(Structure):
    name = String()
    shares = Ingter()
    price = Float()
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
if __name__ == '__main__':
    s = Stock('GOOG',100,490.1)
    s.p()