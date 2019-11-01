#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   rpyc.py
@Time    :   2019/11/01 10:53:02
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
import rpyc
import sys
if __name__ == '__main__':
    c = rpyc.classic.connect("localhost")
    c.excute("print(hi python cookbook)")
    c.modules.sys.stdout = sys.stdout
    c.excute("print(hi here)")