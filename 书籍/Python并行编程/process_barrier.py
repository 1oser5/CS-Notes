#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   process_barrier.py
@Time    :   2019/10/17 15:26:29
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用 barrier 进行进程同步
'''

# here put the import lib
import multiprocessing
import time
import datetime

def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time.time()
    while serializer:
        print("process %s ----> %s" %(name, datetime.datetime.fromtimestamp(now)))

def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time.time()
    print("process %s ----> %s"%(name,datetime.datetime.fromtimestamp(now)))
if __name__ == '__main__':
    synchronizer = multiprocessing.Barrier(2)
    serializer = multiprocessing.Lock()
    multiprocessing.Process(target=test_with_barrier,args=(synchronizer, serializer,)).start()
    multiprocessing.Process(target=test_with_barrier,args=(synchronizer, serializer,)).start()
    multiprocessing.Process(target=test_without_barrier).start()
    multiprocessing.Process(target=test_without_barrier).start()