#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   chapter9.py
@Time    :   2020/01/03 14:13:43
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# 1.函数上添加包装器,并使用 wrap 保留元数据
""" 通过装饰器进行函数功能的添加
使用 wrap 复制元信息，使得函数中有用的信息保留下来
使用访问 wrapped 属性进行接触包装器
"""
import time
from functools import wraps
def timethis(func):
    @wraps(func) # 保留了函数的元数据
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name, end - start)
        return result
    return wrapper
@timethis
def count_down(n):
    while n > 0:
        print(n)
        n -= 1
# 通过 wrapped 访问到被包装函数
count_down.__wrapped__(10) 
count_down.__name__ # count_down

# 6.带可选参数的装饰器
""" 设定一个装饰器，你可以给他传参，也可以不传
装饰器的第一个变量永远是被装饰函数，运用这一点和 partial 配合
"""


# 7.使用装饰器进行类型检查
""" 使用装饰器配合 signature 配合检查参数"""
from inspect import signature
from functools import wraps
def typeassret(*ty_arg, **ty_kwargs):
    def decorate(func):
        if __debug__:
            return func # 如果全局变量 __debug__ 被设置为 Fasle 则直接返回被装饰函数
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_arg, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
            return func(*args, **kwargs)
        return wrapper
    return decorate
@typeassret(int,z=int)
def spam(x, y, z):
    print(x, y ,z)

# 8.将装饰器定义为类的一部分
""" 虽然看上去是一件很奇怪的事情，但是标准库中有很多类似的实现 
比如 property
"""
class A(object):
    # 实例装饰器
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
# usage
a = A()
@a.decorator1
def foo():
    print(1)
@A.decorator2
def spa1m():
    print(2)

# 11.装饰器为包装函数增加额外的参数
""" 想给被包装函数添加固定参数 """
# 可以简单这样写，但是如果 kwargs 里本身就有 debug 关键字，就会报错，因此需要处理
def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
# 处理 debug 关键字
import inspect
def optional_debug1(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        # debug 关键字判断
        if 'debug' in inspect.getargspec(func).args:
            raise TypeError('debug argument already defined')
        # 后续和上述一样
# 上述方案的被包装函数签名其实是错误的
@optional_debug1
def add2(x, y):
    return x+y
print(inspect.signature(add2)) # (x,y)
# 修改函数签名
def optional_debug3(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug',
                inspect.Parameter.KEYWORD_ONLY,
                default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper
@optional_debug3
def add3(x, y):
    return x + y
print(inspect.signature(add3)) # (x, y, *, debug=False)

# 12.使用装饰器扩展类功能
# 添加打印属性功能
def log_getattribute(cls):
    orig_getattribute = cls.__getattribute__
    def new_getattribute(self, name):
        print('get', name)
        return orig_getattribute(self, name)
    cls.__getattribute__ = new_getattribute
    return cls
# Usage
@log_getattribute
class B(object):
    def __init__(self, x):
        self.x = x
a = B(42)
a.x # gettinng: x  42
# 另一种使用类的方案,速度没有上述的函数实现的快
class LogGetAttribute(object):
    def __getattribute__(self, name):
        print('get', name)
        super().__getattribute__(name)
class E(LogGetAttribute):
    def __init__(self, x):
        self.x = x

# 13.使用元类控制实例的创建
""" 元类中，在新建类的时候调用 __init__ 函数，在创建实例的时候调用 __call__ 函数 """
# 新建一个无法创建实例的类
class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('Cant instantiate directly')
class No(metaclass=NoInstance):
    @staticmethod
    def grok():
        print('No.grok')
n = No() # raise error
No.grok() # No.grok
# 创建单例元类
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance
class Spam(metaclass=Singleton):
    def __init__(self):
        print('create Spam')
a = Spam()
b = Spam()
a is b # True