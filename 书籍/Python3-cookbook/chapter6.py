#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   chapter6.py
@Time    :   2019/12/30 09:22:04
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   Python3 cookbook 第六章 数据编码和处理
'''


# 1. 读写 csv 数据
""" 使用 csv 模块读写 csv 文
csv 库可以是别 Micorsoft Excel 所使用的 CSV 编码规则
csv 产生的数据都是字符串类型
"""
# 读取 csv
import csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = csv.reader(f) # 获得标头
    for row in f_csv:
        pass
# 使用命名元组防止混淆
from collections import namedtuple
with open('stock.cvs') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r) # 列表解构
# 或者将其读到字典中
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        pass
# 列表写入
headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
         ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
         ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]
with open('stock.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerow(rows)
# 字典写入
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]
with open('stock.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
# 注意读取时列名的合法性，列名不合法会抛出 ValueError
# 保护列名
import re
with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headers = [re.sub('[^a-zA-Z]','_', h) for h in next(f_csv)] # 将不为字母的字符转化为 _

# 2.读取JSON数据
import json
data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}
# 转为json编码字符串
json_str = json.dumps(data)
# 转回 Python 数据结构
data = json.loads(json_str)
# 如果是处理文件而不是字符串，可以使用 json.dump() 和 json.load()
# 写入 JSON 文件
with open('data.json', 'w') as f:
    json.dump(data, f)
# 读回数据
with open('data.json', 'r') as f:
    data = json.loads(f)
# JSON 编码和 Python 编码几乎一致,除了 True -> true, False -> false, None -> null
json.dumps(False) # 'false'
# 使用 pprint 打印优美的 JSON 格式
from pprint import pprint
pprint(data)
# 想要创建其他数据结构，使用 object_pairs_hook 参数
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict()) # OrderedDict([('name', 'ACME'), ('shares', 50), ('price', 490.1)])
# 将 JSON 字典转换为 Python 对象
class JSONObject(object):
    def __init__(self, d):
        self.__dict__ = d
data = json.loads(s, object_hook=JSONObject)
data.name # 'ACME'
# json.dumps 的 indent 参数也可以用来美化输出
print(json.dumps(data, indent=4))
# 输出
# {
#     "price": 542.23,
#     "name": "ACME",
#     "shares": 100
# }
# 通常来讲 JSON 实例不可序列化，可以提供一个函数，输入为实例，返回一个可序列化字典
def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d
# 反序列化
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
# 维护一个已知类表
classes = {
    'Point':Point
}
def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # 不调用 __init__ 新建实例
        for k, v in d.items():
            setattr(obj, k, v)
        return object
    else:
        return d
# Usage
p = Point(2, 3)
s = json.dumps(p, default=serialize_instance) # '{"__classname__": "Point", "y": 3, "x": 2}'
a = json.loads(s, object_hook=unserialize_object) 
a.x # 2
a.y # 3

# 9.编码和解码十六进制数
""" 十六进制字符串和字节字符串的相互转换 """
import binascii
s = b'hello'
h = binascii.b2a_hex(s) # b'68656c6c6f'
binascii.a2b_hex(h) # b'hello'
# base64 也有相同模块
import base64
h = base64.b16encode(s) # b'68656C6C6F'
base64.b16decode(h) # b'hello'

# 10. 使用 Base64 解码或编码二进制数据
import base64
a = base64.b64encode(s) # b'aGVsbG8='
base64.b85decode(a) # b'hello'
