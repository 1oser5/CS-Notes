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

# 16.*args 和 kwargs 的强制签名
""" 使用 inspect 模块的 Signature 和 Parameter 来进行参数检查 """
# 首先使用 signature 创建签名对象
from inspect import Signature, Parameter
params = [ Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
         Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
         Parameter('z', Parameter.KEYWORD_ONLY, default=None) ]
sig = Signature(params)
print(sig)  # (x, y=42, *, z=None)
# 使用
def func(*args, **kwargs):
    bind_value = sig.bind(*args, **kwargs)
    for name, value in bind_value.arguments.items():
        print(name, value)
func(1,2,3) 
func(1,2,3,4) # ERROR
# 强制所有子类必须提供特定参数签名的例子
def make_sig(*names):
    params = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(params)

class Sign(object):
    __signature__ = make_sig()
    def __init__(self, *args, **kwargs):
        a = self.__signature__.bind(*args, **kwargs)
        for name, value in a.arguments.items():
            print(name, value)
# usage
class Stock1(Sign):
    __signature__ = make_sig('name', 'shares', 'price')


# 17.通过元类来进行参数或者方法的监听
class MyType(type):
    # 定义 new
    def __new__(cls, clsname, bases, clsdict):
        return super().__new__(cls, clsname, bases, clsdict)
    # 定义 iit
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)

# 简单例子，不允许驼峰名称
class NoMixType(type):
    def __new__(cls, clsname, bases, clsdict):
        for name, value in clsdict.items():
            if name.lower() != name:
                raise TypeError('Bad attribute name' + name)
        return super().__new__(cls, clsname, bases, clsdict)
class Root(metaclass=NoMixType):
    pass

class So(Root):
    pass

# 18.以编程方式创建类
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price
def cost(self):
    return self.shares * self.price
cls_dict = {
    '__init__' : __init__,
    'cost':cost
}
import types
# 动态定义类
Stock2 = types.new_class('Stock',(), {},lambda ns: ns.update(cls_dict))
# 需要追加设置一下 __module__ 属性
Stock2.__module__ = __name__
# 传输元类
import abc
Stock2 = types.new_class('Stock',(),{'metaclass':abc.ABCMete},lambda ns: ns.update(cls_dict))

# 19.在定义时初始化类成员
import operator
# 定义初始化元类，在类定义的时候，init函数会调用一次
class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._field):
            setattr(cls, name, property(operator.itemgetter(n)))
# 创建类,使用new是因为init在实例创建之后调用，而tuple不可变
class Struct2(tuple,metaclass=StructTupleMeta):
    _field = []
    def __new__(cls, **args):
        if len(args) != len(cls._field):
            raise AttributeError('Need arguments {cls._field}')
        return super().__new__(cls, args)
# 用例
class Stock(Struct2):
    _field = ['name','price','shares']

# 20.避免重复的属性方法
""" 可以使用 property 进行定义检查变量，但是这样会有很多代码冗余，使用一个函数效果更好 """
# 属性定义函数
def type_property(name, excepted_type):
    strong_name = '_' + name
    @property
    def prop(self):
        return getattr(self, strong_name)
    @prop.setter
    def prop(self, value):
        if not isinstance(value, excepted_type):
            raise TypeError('{} must be a {}'.format(name, excepted_type))
        setattr(self, strong_name, value)
    return prop
## 用例
class Person(object):
    name = type_property('name', str)
    def __init__(self, name):
        self.name = name
# 可以使用 partial 进行简化
import functools
String = functools.partial(type_property, excepted_type=str)

# 22.管理上下文简单方法
import time
from contextlib import contextmanager
# enter 方法执行 yield 之前的代码， exit 方法执行 yield 之后的代码
@contextmanager
def timethis1(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}:{}'.format(label, end-start))
# 使用上述特性实现一个事务的列表
@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working
items = [1, 2, 3]
with list_transaction(items) as working:
    working.append(4)
    working.append(5)
items # [1,2,3,4,5]
with list_transaction(items) as working:
    working.append(6)
    working.append(7)
    raise RuntimeError('oops')
items # [1,2,3,4,5]
# 可以不使用 contextmanager,手动写 enter 和 exit

# 23.局部变量中执行代码
""" exec 函数的范围是拷贝实际局部变量组成的一个字典,因此执行它不会修改局部变量的值，你需要一些操作 """
def test1():
    a = 12
    exec('b = a + 1')
    print(b) # ERROR
# 如果想获得 b 的值
def test2():
    a = 12 
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(b) # 14

