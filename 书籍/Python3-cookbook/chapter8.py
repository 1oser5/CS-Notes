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
