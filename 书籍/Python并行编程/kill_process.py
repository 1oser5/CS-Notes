#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   kill_process.py
@Time    :   2019/10/17 13:23:13
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用 terminate 杀死进程
'''

# here put the import lib
import multiprocessing
import time

def foo():
    print("function start")
    time.sleep(1)
    print("function exit")
if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print(p.is_alive())
    p.start()
    print(p.is_alive())
    p.terminate()
    print(p.is_alive())
    p.join()
    print(p.is_alive())
    print('process exit code',p.exitcode)