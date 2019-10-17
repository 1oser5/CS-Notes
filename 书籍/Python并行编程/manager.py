#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   manager.py
@Time    :   2019/10/17 15:43:36
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用 manager 管理共享对象
'''

# here put the import lib
import multiprocessing

def worker(dictionary,key,item):
    dictionary[key] = item
    print("key = %s, value = %s"%(key,item))
if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    dictionary = mgr.dict()
    p = [multiprocessing.Process(target=worker,args=(dictionary,i,i**2)) for i in range(10)]
    for j in p:
        j.start()
    for j in p:
        j.join()
    print("result",dictionary)