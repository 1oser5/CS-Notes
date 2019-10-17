#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_pool.py
@Time    :   2019/10/17 15:53:21
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用进程池管理进程
'''

# here put the import lib
import multiprocessing
import time
def fun(a):
    return a*a
if __name__ == '__main__':
    l = list(range(100))
    start_time = time.time()
    pool = multiprocessing.Pool(processes=4)
    o = pool.map(fun,l)
    pool.close()
    pool.join()
    print("pool use time",time.time() - start_time)
    start_time = time.time()
    s = map(fun,l)
    print("normal use time",time.time() - start_time)
    print("pool:",o)
