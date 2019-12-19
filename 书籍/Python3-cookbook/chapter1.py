#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   chapter1.py
@Time    :   2019/12/19 14:02:47
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib

if __name__ == '__main__':
    pass
# here put the import lib

# 1.解压序列赋值给多个变量
p = (4, 5)
x, y = p
#仅需要某几个值
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, x, _, y = data

# 2.获得 n 个对象
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
#解压出来的 *something 永远是 列表类型 
print(type(phone_numbers)) # list

# 3.使用 deque 保留 N 个元素
from collections import deque
q = deque(maxlen = 3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
#队列在两端插入或删除元素复杂度都是 O(1)，而列表在开头或者删除元素复杂度为 O(n)

# 4.查找最大或者最小的 N 个元素
"""当元素数量较小的时候，使用 nlargest, nsmallest 是个不错的选择，但是如果只有一个，使用 max 或 min
更快，如果 N 很大，接近集合大小，则使用 sorted(items)[:N] or sorted(items)[N:] 会更好些
"""
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
largest_3 = heapq.nlargest(3, nums)
smallest_3 = heapq.nsmallest(3, nums)
print(largest_3)
print(smallest_3)

# 更复杂的数据结构
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

# 使用堆排序
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(nums)
print(nums)

# 5. 实现一个优先级队列

class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        # 优先级为 priority index item 防止出现优先级一样的情况。-priority 是因为是优先级由大到小
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

q = PriorityQueue()
q.push('foo',1)
q.push('bar',2)
q.push('spam',3)
print(q.pop())
print(q.pop())

# 6. 字典中的键映射多个值
""" defaultdict 会自动为每个 key 创建默认值 """
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)

# without defaultdict
d = {}
pairs = {'foo': 1, 'bar': 2}
for key,value in pairs.items():
    if key not in d:
        d[key] = []
    d[key].append(value)

# with defaultdict
d = defaultdict(list)
for key, value in pairs.items():
    d[key].append(value)

# 7.字典排序
from collections import OrderedDict
""" OrderedDict 可以保留插入字典时的元素顺序
ATTTENTION 一个 OrderedDict 字典大小是一个普通字典的两倍，因为他内部维护着另一个链表
"""

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
for key in d:
    print(key ,d[key])

# 如果需要精确控制编码或者序列化的结果，也可以使用 OrderedDict
import json
json.dumps(d) 
# {"foo": 1, "bar": 2, "spam": 3}

# 8.字典运算
""" 需要进行字典值比较，你可以使用 zip 函数将 key 和 value 反转
ATTTENTION zip 返回的是只能 使用一次 的迭代器，
如果两个元素 value 相同，则会比较 key 来决定返回结果。
"""
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)

# 值相同情况，根据 key 值
d = {'AAA': 100, 'ZZZ': 100}
min_d = min(zip(d.values(), d.keys()))
max_d = max(zip(d.values(), d.keys()))
print(max_d) # ZZZ
print(min_d) # AAA

# 9.查找俩字典的相同点
""" 可以使用集合操作查找俩字典见的关系 """
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}