#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   event.py
@Time    :   2019/10/17 17:20:06
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用 asyncio 提供的时间循环创建异步模型应用
'''

# here put the import lib
import asyncio
import datetime
import time

def fun_1(end_time, loop):
    print("fun_1 called")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1,fun_2, end_time, loop)
    else:
        loop.stop()

def fun_2(end_time, loop):
    print("fun_2 called")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1,fun_3, end_time, loop)
    else:
        loop.stop()

def fun_3(end_time, loop):
    print("fun_3 called")
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1,fun_1, end_time, loop)
    else:
        loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    end_loop = loop.time() + 10.0
    loop.call_soon(fun_1, end_loop, loop)
    loop.run_forever()
    loop.close()