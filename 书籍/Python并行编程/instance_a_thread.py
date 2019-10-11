#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   define_a_thread.py
@Time    :   2019/10/11 08:33:40
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用 Threading.thread 定义一个线程
'''

# here put the import lib
import threading
def fun(i):
    return print("function called by thread",i)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=fun,args=(i,))
        t.start()
        t.join()