#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   addTask.py
@Time    :   2019/10/22 11:16:59
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
import celery

app = celery.Celery('addTask', broker='amqp://guest@localhost//')
@app.task
def add(x, y):
    return x + y
if __name__ == '__main__':
    pass