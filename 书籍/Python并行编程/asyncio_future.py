#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   asyncio_future.py
@Time    :   2019/10/22 10:36:06
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用 asyncio 的 future 类
'''

# here put the import lib
import asyncio

@asyncio.coroutine
def f1(future, n):
    count = 0
    for i in range(2, n + 1):
        count += i
        yield from asyncio.sleep(3)
    future.set_result("first coroutine (sum of N intergers) result = " + str(count))
@asyncio.coroutine
def f2(future, n):
    count = 1
    for i in range(2, n + 1):
        count *= i
        yield from asyncio.sleep(3)
    future.set_result("second coroutine (factorial) result = " + str(count))

def get_result(future):
    print(future.result())
if __name__ == '__main__':
    future1 = asyncio.Future()
    future2 = asyncio.Future()
    loop = asyncio.get_event_loop()
    tasks = [f1(future1,4),f2(future2,4)]
    future1.add_done_callback(get_result)
    future2.add_done_callback(get_result)
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()