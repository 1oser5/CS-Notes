#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   chapter7.py
@Time    :   2019/12/30 13:29:58
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   Python3-cookbook 第七章 函数
'''

# 2. 只接受关键字参数的函数
""" 将关键字参数放到某个 * 参数或者单个 * 之前，使其只接受关键字参数 """
def recv(maxsize, * , block):
    pass
#recv(1024,False) # error
recv(1024,block=False) # Ok

# 3.给函数添加元信息
""" 使用参数注解是个不错的办法
ATTENTION 函数注解只存储在 __annotations__ 属性中
"""
def add(x:int, y:int) -> int:
    return x + y
print(help(add))
# 输出
# Help on function add in module __main__:

# add(x: int, y: int) -> int

# 其存储在 annotations 中
add.__annotations__ # {'y': <class 'int'>, 'return': <class 'int'>, 'x': <class 'int'>}

# 5.定义有默认参数的函数
""" 
ATTENTION 默认参数仅在函数定义的时候赋值一次
默认值应该是不可变对象，如果是可变对象，那么会为同一个（因为其在定义时创建，后续修改都基于同一个地址）
"""
# 简单的例子
def spam(a, b=42):
    print(a, b)
spam(1)
spam(1, 2)
# 需要默认参数是一个可修改的容器，使用 None 作为默认值
def foo(a, b=None):
    if b is None:
        b = []
# 仅仅只想测试一个是否有值传入，可以这样做
no_value = object()
def dam(a, b=no_value):
    if b is no_value:
        print('no b value supplied')
# 函数仅在定义时赋值一次
x = 42
def simple(a, b=x):
    print(a, b)
simple(2) # 2 42
x = 43
simple(2) # 2 42
# 定义默认参数为 可变对象，他会和你想象的不一样，但你可以利用他的特性
def spp(a, b=[]):
    print(b)
    return b
x = spp(1) # []
x.append(2) # [2]
x.append('now') # [2, 'now']
c = spp(2) # [2, 'now']

# 7.匿名函数捕获变量名
""" 事实上这章的内容会让人有些迷惑，因为很少会有人这样使用 lambda ，但有些真理还是至关重要的
ATTENTION lambda 中的变量在运行时绑定，而不是定义时！（和一般的函数有很大区别），如果你需要其在
定义时捕获值，将其设置为默认参数即可
"""
# 运行时绑定变量
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10)) # 30
print(b(10)) # 30
# 设置默认参数，使其在定义时绑定
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10)) # 20
print(b(10)) # 30

# 8.减少可调用对象的参数个数
""" 使用 functools.partial() 减少参数个数，在某些方面有妙用 """
from functools import partial
def test(a, b, c, d):
    print(a, b, c, d)
# 定义第一个参数为 a
s1 = partial(test, 1)
s1(2,3,4) # 1, 2, 3 ,4
# 定义指定参数
s2 = partial(test, d=42)
s2(1,2,3) # 1, 2, 3, 42

# 9.将单方法的类转化为函数
""" 利用闭包将单个方法的类转化为函数 """
# 该类仅仅只是为了记住 url
class Url(object):
    def __init__(self, url):
        self.url = url
    def open(self, *args, **kwargs):
        self.url # do something with url
# 使用 闭包达到上述类效果
def url(url):
    def open(*args, **kwargs):
        url # do something with url
    return open

# 10.在回调时需要携带额外状态
""" 使用类或者闭包甚至协程，使得回调函数能获取更多的环境变量 """
# 定义一个拥有回调函数的函数
def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)
def print_result(result):
    print('Got', result)
def add_some(x, y):
    return x + y
apply_async(add_some,(2, 3),callback=print_result) # Got 5
apply_async(add_some,('hello', 'world'),callback=print_result) # Got helloworld
# 使用类获得更多外部信息
class ResultHandler(object):
    def __init__(self):
        self.sequence = 0
    def handle(self, result):
        self.sequence += 1
        print_result(f'[{self.sequence}] Got {result}')
# 使用
r = ResultHandler()
apply_async(add_some, (2, 3), callback=r.handle) # [1] Got 5
# 或者使用闭包
def make_handle():
    sequence = 0
    def handle(result):
        nonlocal sequence # 没有这行代码会出错
        sequence += 1
        print_result(f'{sequence} Got {result}')
    return handle
handler = make_handle()
apply_async(add_some, (2, 3), callback=handler) # [1] Got 5
apply_async(add_some, (3, 3), callback=handler) # [1] Got 6

# 12.访问闭包中定义的变量
""" 扩展函数中的闭包，让他能访问和修改函数内部变量
ATTENNTION 为什么不用一个正儿八经的类来完成类似的事情？？？
这比使用类会稍微快些，但是限制会更多
"""
# 😂 像类一样的函数，使用闭包保存属性
def function_class():
    n = 0
    def func():
        print('n=',n)
    
    def get_n():
        return n
    
    def set_n(value):
        nonlocal n
        n = value
    func.get_n = get_n
    func.set_n = set_n
    return func
# Usage
f = function_class()
f() # n = 0
f.set_n(10)
f() # n = 10
