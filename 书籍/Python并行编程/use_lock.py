#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_lock.py
@Time    :   2019/10/14 09:29:31
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用 Lock（）函数创建锁
'''

# here put the import lib
import threading

count_with_lock = 0
count_without_lock = 0
COUNT = 10000000
shared_lock = threading.Lock()

#有锁条件下
def increment_with_lock():
    global count_with_lock
    for _ in range(COUNT):
        shared_lock.acquire()
        count_with_lock += 1
        shared_lock.release()
def decrement_with_lock():
    global count_with_lock
    for _ in range(COUNT):
        shared_lock.acquire()
        count_with_lock -= 1
        shared_lock.release()


#无锁条件下
def increment_without_lock():
    global count_without_lock
    for _ in range(COUNT):
        count_without_lock += 1

def decrement_without_lock():
    global count_without_lock
    for _ in range(COUNT):
        count_without_lock -= 1
if __name__ == '__main__':
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("count_with_lock is",count_with_lock)
    print("count_without_lock is",count_without_lock)