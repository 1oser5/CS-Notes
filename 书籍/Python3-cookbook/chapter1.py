#!/usr/bin/env python3.7
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
""" 可以使用集合操作查找俩字典间的关系 """
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

# find key in common
a.keys() & b.keys() # {'x', 'y'}
# find keys in a but not in b
a.keys() - b.keys() # {'z'}
# find (k,v) pairs in common
a.items() & b.items() #{('y', 2)}

# 修改和过滤某些元素
c = {key:a[key] for key in a.keys()- {'x', 'w'}}


# 10.在一个序列上删除相同元素并保持顺序

# 如果该序列是 hashable 的，则可以直接使利用集合和生成器
def dequpe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dequpe(a)))

# 不可哈希元素，使用如下代码，通过 key 将其转为 hashable
def deque_un(items, key = None):
    seen = set()
    for item in items:
        val = item if key == None else key(item)
        if val not in seen:
            yield val
            seen.add(val)
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(deque_un(a, key=lambda d: (d['x'],d['y']))))

# 11.命名切片
""" 通过 slice 将代码变得更加有可读性 """
record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[20:23]) * float(record[31:37])

# 可以通过 start, stop, step 参数获得详细信息
a = slice(5, 50, 2)
a.start # 5
a.stop # 50
a.step # 2

# 使用 indices(size) 将其映射到已知序列上，返回一个 三元组 (start, stop, step)，所有值都会缩小
s = 'HelloWorld'
a.indices(len(s)) # (5, 10, 2)
for i in range(*a.indices(len(s))):
    print(s[i])

# 12. 序列中出现的最多次数的元素
from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
words_count = Counter(words)
top_three = words_count.most_common(3) 
print(top_three) # [('eyes', 8), ('the', 5), ('look', 4)]

# 实际上 counter 就是一个字典，key 为元素的值，value 为出现次数
words_count['eye'] # 8
words_count['not'] # 1

# 可以手动增加记数
morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    words_count[word] += 1
print(words_count['eye']) # 9

# 也可以使用 update 函数
words_count.update(morewords)

# counter 可以用来计算数值
a = Counter(words)
b = Counter(morewords)
print(a+b)  
#Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2, 'around': 2, "don't": 1, "you're": 1, 'under': 1, 'why': 1, 'are': 1, 'you': 1, 'looking': 1, 'in': 1})
print(a-b)  
#Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2,#"you're": 1, "don't": 1, 'under': 1})

# 13 通过某个关键字进行排序
from operator import itemgetter
""" 通过 itemgetter 进行字典排序，可以选择多个值
itemsgetter 创造了一个 callable 对象，其对每一个传入对象返回一个值，sorted 会根据这些值进行排序。
如果你传入多个对象，就会返回一个元组。
ATTENTION itemgetter 比 lambda 更快
 """
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
# 单个值
row_by_fname = sorted(rows, key=itemgetter('fname'))
# 多个值
row_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(row_by_fname)
print(row_by_lfname)

# itemgetter 可以用 lambda 代替
row_by_fname = sorted(rows, key=lambda a: a['fname'])

# 14. 排序不支持原生比较的对象
""" 和 13 不同的是这里使用了属性比较
ATTENTION attrgetter 比 lambda 更快
"""
from operator import attrgetter

class User(object):
    def __init__(self, user_id):
        self._user_id = user_id
def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))
    #可以使用 attrgetter 代替 lambda 参数
    print(sorted(users, key=attrgetter('user_id')))

# 15.通过某个字段分组
""" 可以通过 sort 配合 groupby 进行对某个字段的数据分组
ATTENTION 必须先进行排序，因为 groupby 仅仅检查连续的元素！
"""
from itertools import groupby
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
# 首先进行排序
rows.sort(key=itemgetter('date'))
# 分组
for date,items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(i)
# 只是想把其分组放到一个更大的数据结构，并允许随机访问，使用 defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

# 16. 过滤元素

# easy way，使用列表推导式
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
pos = [i for i in mylist if i > 0]   
# mid way，生成器
pos_ge = (i for i in mylist if i > 0)
#情况比较复杂使用 filter 函数
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals) #['1', '2', '-3', '4', '5']

# 17. 从字典中提取子集
"""ATTENTION 字典推导式会比 dict 快 """
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# 获得 value > 200 的子集
over_200 = {key: value for key, value in prices.items() if value > 200}
# 使用 dict 函数实现
over_200 = dict((key, value) for key, value in prices.items() if value > 200)

# 18. 映射名称到序列元素
""" 通过命名元组来实现名称访问，collections.namedtuple 函数返回一个标准呢元组类型子类的一个方法
虽然 nametuple 实例看起来像类但是他和元组是可以交换数据的。
命名元组比较字典更节约内存，但需要注意其是不可变的。
如果十分在乎高效的数据结构，并且其要更新很多数据，__slots__可能是更好的选择。
"""
from collections import namedtuple
# 定义类，第一个参数为类名，第二个参数为类属性
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
# 可以拥有元组的所有操作
addr, joined = sub
len(sub)
# 需要改变属性值，可以使用 _replace 方法，他会创建一个全新的命名元组
sub_2 = sub._replace(addr = 'onesy@qq.com')
print(sub_2) # Subscriber(addr='onesy@qq.com', joined='2012-10-19')
# 使用 _replace 方法进行填充数据，先创建一个包含缺省值的原型元组，然后使用 _replace 替换
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# 创建原型实例
stock_prototype = Stock('', 0, 0.0, None, None)
# 定义填充数据函数
def dict_to_stock(s):
    return stock_prototype._replace(**s)
# Usage
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
dict_to_stock(a)

# 19. 转化并计算数据
"""使用列表生成器可以非常优雅的完成格式转换以及计算数据
当然生成器是更好的选择
"""
nums = [1, 2, 3, 4, 5]
s = sum(x*x for x in nums)
# 你可以不省略括号,但省略括号更棒！
s = sum((x*x for x in nums))
# 你可以生成列表来计算，但是这样增加了一个创建列表的开销
s = sum([x*x for x in nums])

# 20.合并多个字典或映射
""" 使用 chainMap 进行多字典合并后操作
这些字典并没有合并在一起，ChainMap 只是在内部创建了一个容纳这些字典的列表
 """
from collections import ChainMap
# 创建
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c = ChainMap(a, b)
print(c['x']) # 1
print(c['y']) # 2
print(c['z']) # 3
# 大部分操作可以执行
len(c)
list(c.keys())
list(c.values())
# ChainMap 更新和删除都先影响第一个字典，出现重复键，第一次出现的映射值会被返回
c['z'] = 10
c['w'] = 40
print(c)
del c['x']
print(a) # {'w': 40, 'z': 10}
# ChainMap 对于作用范围变量，有更好的定义
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values) # ChainMap({'x': 3}, {'x': 2}, {'x': 1})
# 可以使用 values.parents 进行切换
values = values.parents
print(values) # ChainMap({'x': 3}, {'x': 2}, {'x': 1})
# 使用 update 合并两个字典，会返回一个新字典，对新字典的改动不会映射到新字典中
merged = dict(b)
merged.update(a)