#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   inlined_async.py
@Time    :   2019/12/30 15:10:13
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   内联回调函数
'''

# here put the import lib
from queue import Queue
from functools import wraps

def async_apply(func, args, *, callback):
    result = func(*args)
    callback(result)

class Async(object):
    def __init__(self, func, args):
        self.func = func
        self.args = args
def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        q = Queue()
        q.put(None)
        while True:
            result = q.get()
            try:
                a = f.send(result)
                async_apply(a.func, a.args, callback=q.put)
            except StopIteration:
                break
    return wrapper

            
def add(x, y):
    return x + y

@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')

if __name__ == '__main__':
    test()
