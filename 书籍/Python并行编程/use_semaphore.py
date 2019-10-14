#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_semaphore.py
@Time    :   2019/10/14 10:20:17
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用信号量创建锁
'''

# here put the import lib
import threading
import time
import random

semaphore = threading.Semaphore(0)
def consumer():
    semaphore.acquire()
    print("consume item",item)
def producer():
    global item
    item = random.randint(0,100)
    print("produce item",item)
    semaphore.release()
if __name__ == '__main__':
    for _ in range(5):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t2.join()
        t2.join()