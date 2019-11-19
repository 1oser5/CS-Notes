#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   instance_process.py
@Time    :   2019/10/17 13:03:57
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
import multiprocessing

def fun(i):
    print("This is process",i)

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=fun,args=(i,))
        p.start()
        p.join()