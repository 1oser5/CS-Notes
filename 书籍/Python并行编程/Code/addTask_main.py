#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   addTask_main.py
@Time    :   2019/10/22 11:19:17
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
import addTask
if __name__ == '__main__':
    result = addTask.add.delay(5, 5)
    