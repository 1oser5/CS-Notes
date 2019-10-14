#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_rlock.py
@Time    :   2019/10/14 09:50:27
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用 RLock（）函数创建锁
'''

# here put the import lib
import threading
import time

class Box(object):
    shared_lock = threading.RLock()
    def __init__(self):
        self.items = 0
    def change_items(self,n):
        Box.shared_lock.acquire()
        self.items += n
        Box.shared_lock.release()
    def add(self):
        Box.shared_lock.acquire()
        self.change_items(1)
        Box.shared_lock.release()
    def remove(self):
        Box.shared_lock.acquire()
        self.change_items(-1)
        Box.shared_lock.release()

def adder(box, n):
    while n > 0:
        print("add 1 item")
        box.add()
        time.sleep(1)
        n -= 1
def remover(box, n):
    while n > 0:
        print("remove 1 item")
        box.remove()
        time.sleep(1)
        n -= 1
if __name__ == '__main__':
    box = Box()
    t1 = threading.Thread(target=adder,args=(box,5))
    t2 = threading.Thread(target=remover,args=(box,5))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("item is",box.items)