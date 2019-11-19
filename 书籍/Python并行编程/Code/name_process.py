#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   name_process.py
@Time    :   2019/10/17 13:08:14
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   获得目前运行线程名
'''

# here put the import lib
import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print("Start %s" % name)
    time.sleep(3)
    print("Exit %s" % name)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=foo,name = 'foo_process')
    p2= multiprocessing.Process(target=foo)
    p1.daemon = True # 表示其为守护进程，意味着这个线程是不重要的，在线程退出时，可以不等待这个线程退出。
    p1.start()
    p2.start()
    p1.join()
    p2.join()
