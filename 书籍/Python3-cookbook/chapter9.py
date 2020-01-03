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

# 2.定义一个带参数的装饰器