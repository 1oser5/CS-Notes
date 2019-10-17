#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   background_process.py
@Time    :   2019/10/17 13:16:56
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   后台运行线程
'''

# here put the import lib
import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print("Start",name)
    time.sleep(3)
    print("Exit",name)

if __name__ == '__main__':
    back_process = multiprocessing.Process(target=foo)
    no_back_process = multiprocessing.Process(target=foo)
    back_process.start()
    back_process.daemon = True
    no_back_process.daemon = False
    no_back_process.start()
    back_process.join()
    no_back_process.join()