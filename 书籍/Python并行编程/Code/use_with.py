#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_with.py
@Time    :   2019/10/14 11:36:31
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用 with 语法
'''

# here put the import lib
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s)%(message)s',)

def thread_with(statement):
    with statement:
        logging.debug('%s acquired via with' % statement)

def thread_no_with(statement):
    statement.acquire()
    try:
        logging.debug('%s acquired directly' % statement)
    finally:
        statement.release()
if __name__ == '__main__':
    lock = threading.Lock()
    rlock = threading.RLock()
    condition = threading.Condition()
    semaphore = threading.Semaphore(1)
    l = [lock, rlock, condition, semaphore]
    for i in l:
        t1 = threading.Thread(target=thread_with,args=(i,))
        t2 = threading.Thread(target=thread_no_with,args=(i,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
