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

# 4.5反向迭代
""" 定义了 __reversed__ 函数的对象可以使用 reversed 进行反向迭代
如果没有定义 __reversed__ 方法，则需要先转化为列表
ATTENTION 如果列表元素很大，转化列表会很占用空间
__reversed__ 返回生成器是很高效的做法
 """
# 反向迭代列表
a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)
# 转化为列表再反转
lines = '123'
for line in reversed(list(lines)):
    print(line)
# 定义生成器反转
class Countdown(object):
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        """ 正向迭代 """
        n = self.start
        while n > 0:
            yield n
            n -= 1
    def __reversed__(self):
        """ 反向迭代 """
        n = 0
        while n <= self.start:
            yield n
            n += 1
for r in reversed(Countdown(30)):
    print(r)
for r in (Countdown(30)):
    print(r)

# 4.6带有外部状态的生成器
""" 想暴露一些生成器的属性，将它设计为类，再实现 __iter__ 方法即可 """
from collections import deque
class linehistory(object):
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)
    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line
    def clear(self):
        self.history.clear()

# 7.生成器切片
""" 使用 itertools 解决生成器切片问题 """
import itertools
def count(n):
    while True:
        yield n
        n += 1
for x in itertools.islice(c, 10, 20):
    print(x)

# 8.跳过可迭代对象的开始部分
""" 使用 itertools 的 dropwhile 和 islice
dropwhile 接受一个函数对象和可迭代对象，他会返回一个迭代器对象，丢弃原有序列中直到函数返回 False 之前的元素
 """
from itertools import dropwhile
with open('/etc/passwd') as f:
    for line in dropwhile(lambda x: line.startswith('#'), f):
        print(line, end='')
# 知道具体跳过哪几个对象，使用 islice
from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

# 9.迭代的排列组合
""" itertools.permutations() 生成全排列
itertools.combinations() 也生成全排列但不在乎顺序
itertools.itertools.combinations_with_replacement() 则不剔除元素计算
 """
from itertools import permutations
items = ['a', 'b', 'c']
# 全排列
for p in permutations(items):
    print(p)
# 输出
# ('a', 'b', 'c')
# ('a', 'c', 'b')
# ('b', 'a', 'c')
# ('b', 'c', 'a')
# ('c', 'a', 'b')
# ('c', 'b', 'a')

# 指定长度
for p in permutations(items, 2):
    print(p)
# 对 combination 来说，不在乎顺序
from itertools import combinations
for c in combinations(items,3):
    print(c) # ('a', 'b', 'c')
for c in combinations(items, 2):
    print(c)
# 输出
# ('a', 'b')
# ('a', 'c')
# ('b', 'c')

# itertools.combinations_with_replacement() 不会剔除元素
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)
 # 输出
 # ('a', 'a', 'a')
# ('a', 'a', 'b')
# ('a', 'a', 'c')
# ('a', 'b', 'b')
# ('a', 'b', 'c')
# ('a', 'c', 'c')
# ('b', 'b', 'b')
# ('b', 'b', 'c')
# ('b', 'c', 'c')
# ('c', 'c', 'c')   

# 10.序列索引值迭代
""" enumerate() 函数很好的解决了这个问题 """
my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print(index, value)
# 输出
# 0 a
# 1 b
# 2 c

# 可以使索引从指定位置开始
for index, value in enumerate(my_list, 1):
    print(index, value)
# 输出
# 1 a
# 2 b
# 3 c

# 11.同时迭代多个序列
""" 使用 zip 来进行同时迭代
zip 会返回一个生成器，生成器中的元素为 个数为输入序列数量的元组
生成器长度默认为 最短序列长度
可以使用 itertools.zip_longest() 来继续迭代到最长序列
"""
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print (x, y)
# 输出
# 1 101
# 5 78
# 4 37
# 2 15
# 10 62
# 7 99

# 返回生成器长度和最短序列一致
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    print(i)
# 输出
# (1, 'w')
# (2, 'x')
# (3, 'y')

# 使用 itertools.zip_longest() 来输出最长生成器
from itertools import zip_longest
for i in zip_longest(a, b):
    print(i)
# 输出
# (1, 'w')
# (2, 'x')
# (3, 'y')
# (None, 'z')

# 可以设置默认填充值
for i in zip_longest(a, b, fillvalue=0):
    print(i)
# 输出
# (1, 'w')
# (2, 'x')
# (3, 'y')
# (0, 'z')

# 12.不同集合上元素的迭代
""" 想要多个集合执行相同操作，使用 itertools.chain()
其可以接受1个或者多个集合，并返回一个迭代器
这会比将几个集合先合并在执行循环效率要高，因为合并集合需要新建一个集合，而 chain 没有这一步
在集合元素较多时很有用
 """
from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)
# 输出
# 1
# 2
# 3
# 4
# x
# y
# z

# 其效率比先将序列合并在迭代要高得多
# Inefficent
for x in a + b:
    pass
# Better
for x in chain(a, b):
    pass

# 14.展开嵌套的序列
""" 使用 yield from 将多层嵌套展开为单层列表 """
from collections.abc import Iterable

def flatten(items, ignore_types = (str, bytes)):
    for i in items:
        if isinstance(i, Iterable) and not isinstance(i, ignore_types):
            yield from i
        else:
            yield i
items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x) # Produces 1 2 3 4 5 6 7 8

# 15.顺序迭代合并后的排序迭代对象
""" 使用 heapq.merge() 将有序的多个列表合并为一个
ATTENTION 注意 heapq 要求所有输入都是有序的，因为他不会预先读取所有数据到堆栈中，
也不会对输入做任何排序检测，他只检查所有序列开始部分的最小那个
"""
import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)

# 15.使用 iter() 代替无限循环
""" iter 函数鲜为人知的一点是它接受一个 callable 对象和一个结束标志，他会不断迭代
知道 callabe 返回和结束标志一样的内容
"""
CHUNKSIZE = 8192
# 传统 I/O 做法
def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        # process_data(data)
# 使用 iter()
def reader2(s):
    for chunk in iter(lambda s: s.recv(CHUNKSIZE), b''):
        pass