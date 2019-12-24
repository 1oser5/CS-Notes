#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   chapter4.py
@Time    :   2019/12/24 18:57:34
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# 1.手动遍历迭代器
""" 使用 next() 配合 stopIteration 进行手动迭代 """
def manual_iter():
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            print('迭代完成')
# 也可以使用 None 来结束迭代
def iter_man():
    with open('/etc/passwd') as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line,end='')

# 2.代理迭代
""" 定义一个新容器，容器中有可迭代对象时，你可以使用 __iter__ 将迭代代理给该对象 """
class Node1(object):
    def __init__(self):
        self._children = []
    def add_children(self,n):
        self._children.append(n)
    def __iter__(self):
        return iter(self._children)
# test
root = Node1()
root.add_children(1)
root.add_children(2)
root.add_children(3)
for i in root:
    print(i) # 1, 2, 3

# 3.使用生成器创建新的迭代
# 自定义的 range 函数
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment
# 通过可接受可迭代对象的函数调用
for n in frange(0, 4, 5):
    print(n)
list(frange(0, 1, 0.125))

# 4.实现迭代协议
# 广度优先遍历树节点
class Node(object):
    def __init__(self, value):
        self._value = value
        self._children = []
    def add_child(self, n):
        self._children.append(n)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        yield self
        # for 调用 self 返回的是 self._children
        for c in self:
            yield from c.depth_first()
root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))
for c in root.depth_first():
    print(c)