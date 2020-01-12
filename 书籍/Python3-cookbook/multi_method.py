#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   multi_method.py
@Time    :   2020/01/12 19:45:45
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用元类配合函数注解实现函数重载
'''

# here put the import lib
import inspect
import types

class MultiMethod(object):
    def __init__(self, name):
        self._methods = {}
        self.name = name
    def register(self, meth):
        sig = inspect.signature(meth)
        types = []
        for name, param in sig.parameters.items():
            if name == 'self':
                continue
            if param.annotation is inspect.Parameter.empty:
                raise TypeError('Argument {} must be annotated with a type'.format(name))
            if not isinstance(param.annotation, type):
                raise TypeError('Argumennt {} annotation must be a type'.format(name))
            if param.default is not inspect.Parameter.empty:
                self._methods[tuple(types)] = meth
            types.append(param.annotation)
        self._methods[tuple(types)] = meth
    def __call(self, *args):
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types, None)
        if meth:
            return meth(*args)
        else:
            raise TypeError('No match for types {}'.format(types))
    def __get__(self, instance, cls):
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self
class MultiDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            current_value = self[key]
            if isinstance(current_value, MultiMethod):
                current_value.register(value)
            else:
                mvalue = MultiMethod(key)
                mvalue.register(value)
                mvalue.register(current_value)
                super().__setitem__(key, mvalue)
        else:
            super().__setitem__(key,value)
class MultipleMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        return type.__new__(cls, clsname, bases, dict(clsdict))
    @classmethod
    def __prepare__(cls, clsname, bases):
        return MultiDict()
if __name__ == '__main__':
    pass