#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   executor_pool.py
@Time    :   2019/10/17 16:40:57
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   比较顺序执行，线程池执行和进程池执行速度
'''

# here put the import lib
import concurrent.futures
import time

num_list = list(range(10))

def evaluate_item(x):
    for i in range(100000):
        i += 1
    return i*x
if __name__ == '__main__':
    #顺序执行
    start_time = time.time()
    for i in num_list:
       evaluate_item(i)
    print("sequential execution use time",time.time() - start_time)
    #进程池
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate_item,i) for i in num_list]
        for f in concurrent.futures.as_completed(futures):
            f.result()
    print("processPool use time",time.time() - start_time)
    #线程池
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(evaluate_item,i) for i in num_list]
        for f in concurrent.futures.as_completed(futures):
            f.result()
    print("threadPool use time",time.time() - start_time) 
