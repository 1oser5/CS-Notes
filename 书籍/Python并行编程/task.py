#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   task.py
@Time    :   2019/10/22 09:57:10
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用 asyncio 控制任务
'''

# here put the import lib
import asyncio

@asyncio.coroutine
def factorial(num):
    f = 1
    for i in range(2, num + 1):
        print("Asyncio.Task:Compute factorial(%s)" % (i))
        yield from asyncio.sleep(1)
        f *= 1
    print("Asyncio.Task - factorial(%s) = %s" % (num, f))

@asyncio.coroutine
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        print("Asyncio.Task:Compute fibonacci (%s)"%(i))
        yield from asyncio.sleep(1)
        a, b = b, a + b
    print("Asyncio.Task - fibonacci(%s) = %s"%(num, a))

@asyncio.coroutine
def binomialCoeff(n,k):
    result = 1
    for i in range(1, k + 1):
        result = result * (n-i+1) / i
        print("Asyncio.Task:Compute binomialCoeff (%s)"%(i))
        yield from asyncio.sleep(1)
    print("Asyncio.Task - binomialCoeff(%s,%s) = %s"%(n,k,result))


if __name__ == '__main__':
    tasks = [asyncio.Task(fibonacci(10)),
    asyncio.Task(factorial(10)),
    asyncio.Task(binomialCoeff(20,10))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


