#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   subclass_process.py
@Time    :   2019/10/17 14:29:52
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
import multiprocessing

class MyProcess(multiprocessing.Process):
    def run(self):
        print("called run method in process %s"%self.name)

if __name__ == '__main__':
    for i in range(5):
        p = MyProcess()
        p.start()
        p.join()