#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   chapter8.py
@Time    :   2019/12/31 18:04:10
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   Python3-cookbook 第八章 类与对象
'''

# 1.改变对象的字符串显示
""" 修改实例的字符串显示，定义 __str__ 和 __repr__ """
class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        return '{0.x!s}, {0.y!s}'.format(self)
# Usage
p = Pair(3, 4)
p # Pair(3, 4) # __repr__() output
print(p) # (3, 4) # __str__() output
# !r 指明格式化输出 __repr__() 来代替 __str__
p = Pair(3, 4)
print('p is {0!r}'.format(p)) # p is Pair(3, 4)
print('p is {0}'.format(p)) # p is (3, 4)
# __repr__ 的标准是让 eval(repr(x)) == x 为真，如果不行，就创建一个有用的文本，并使用 <> 括起来
f = open('some.txt') # <_io.TextIOWrapper name='file.dat' mode='r' encoding='UTF-8'>
# 0 实际上表示 self 本身
print('p is {0!r}'.format(p))

# 2.自定义字符串的格式化
""" 定义 __format__ 实现自动格式化 """
_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)
d = Date(2012, 12, 21)
format(d) # '2012-12-21'

# 3.让对象支持上下文管理协议
""" 定义 __enter__ 和 __exit__ 实现 with 语句 """
# 实现一个简单的网络连接
from socket import socket, AF_INET, SOCK_STREAM
class LazyConnection(object):
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None
    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected!')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock
    def __exit__(self, exc_tu, exc_val, tb):
        self.sock.close()
        self.sock = None
# Usage，属于懒连接，在定义时什么都不做
conn = LazyConnection(('www.python.org', 80))
with conn as s:
    pass

# 4.创建大量对象的内存优化
""" 你可以使用 __slots__ 属性来极大地减少实例所占的内存
ATTENTION 当你这样做时，Python 会为实例使用一种更紧凑的内部表示
实例通过一个固定大小的数组来构建，而不是每个实例定义一个字典，和元组和列表类似
但我们使用了 __slots__ 之后无法定义新的属性，只能使用那些属性
将 __slots__ 作为封装工具来防止用户增加新的属性，并不是其初衷，请将它作为一个内存管理工具来使用
"""
class Date_(object):
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

# 5.在类中封装属性名
""" Python 没有私有变量的限制，但是程序员遵循一定的属性和方法命名来达到这个效果
第一个约定: 任何以单下划线 _ 开头的名字都应该是内部实现
第二个约定: 使用双下划线会导致访问名称会变成其他形式，使得其在继承中无法被覆盖
第三个约定: 如果你的变量命名和保留字冲突，在后面加上 _
"""
# 单个下划线是内部实现
class A(object):
    def __init__(self):
        self._internal = 0
# 双下划线其无法被覆盖
class B(object):
    def __init__(self):
        self.__private = 0
    def __private_method(self):
        pass
class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1 # Does not override B.__private
    # Does not override B.__private_method()
    def __private_method(self):
        pass

# 6.创建可管理的属性
""" 使用 property 进行类管理
可以将已有的方法定义为 property
定义为 property 的属性是懒加载的
可以用其让代码变得优雅，而不是臃肿
"""
# 使用 property 进行类检查
class Person(object):
    def __init__(self, first_name):
        self.first_name = first_name
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Excepted a string')
        self._first_name = value
# 将已有方法定义为 property
class P(object):
    def __init__(self, first_name):
        self.set_first_name(first_name)
    # Getter function
    def get_first_name(self):
        return self._first_name
    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value
    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")
    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)
# 懒加载，优雅的访问属性
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
c = Circle(4.0)
c.radius # 4.0
c.area # 50.26548245743669

# 7.调用父类方法
""" 使用 super 调用父类超类方法
Python使用解析顺序表（MRO）进行继承，这里列表就是简单地基类线性表
其使用 C3 线性算法实现，遵守如下三条准则：
1.子类先于父类被检查
2.多个父类会根据表中顺序被检查
3.下个类存在合法选择，选择第一个父类
"""
class A1(object):
    def spam(self):
        self.x = 1
class B1(A1):
    def spam(self):
        super().spam() # 调用 A1 spam 方法
# 常见用法是保证 父级 __init__ 正常工作
class I(object):
    def __init__(self):
        self.x = 1
class IChildren(I):
    def __init__(self):
        self.y = 1
        super().__init__()
i = IChildren()
IChildren.__mro__ # 查看继承链

# 8.子类中扩展property
""" 需要复写全部 property 时，写法和定义一样，
只需要覆盖某个 property 时，有些区别
"""
class P2(object):
    def __init__(self, name):
        self.name = name
    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")
# 全部重写
class SubPerson(P2):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)
# 部分重写
class SubPerson1(P2):
    @P2.name.getter # 可以正常运行，标红可能是因为 property 是动态计算的
    def name(self):
        print('Getting name')
        return super().name

# 10.使用延迟计算
""" 将一个只读属性定义为 property 使其只有在访问时才计算结果，并把计算值保存下来 """
# 描述器
class LazyProperty(object):
    def __init__(self, func):
        self.func = func
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value  = self.func(instance) # 本来 func 就接受一个入参 self
            setattr(instance, self.func.__name__, value)
            return value
class Circle1(object):
    def __init__(self, radius):
        self.radius = radius
    @LazyProperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2
    @LazyProperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius
# 这样使得调用只会计算一次

# 11.简化数据结构的初始化
""" 使用一个基类的 init 来简化后续初始化工作 """
# 基类
class Structure1(object):
    _field = [] # 接收参数
    def __init__(self, *args):
        if len(args) != len(self._field):
            raise TypeError('Excepted {} arguments'.format(len(self._field)))
        for name, value in zip(self._field, args):
            setattr(self, name, value)
# 实例
class Some(Structure1):
    _field = ['a', 'b']

