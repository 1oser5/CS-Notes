#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_event.py
@Time    :   2019/10/14 11:08:37
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用事件进行线程同步
'''

# here put the import lib
import time
import threading
import random

items = []
event = threading.Event()
class Consumer(threading.Thread):
    def __init__(self,event,items):
        threading.Thread.__init__(self)
        self.event = event
        self.items = items
    def run(self):
        while True:
            time.sleep(2)
            self.event.wait()
            item = self.items.pop()
            print("item pop item",item)

class Producer(threading.Thread):
    def __init__(self,event,items):
        threading.Thread.__init__(self)
        self.event = event
        self.items = items
    def run(self):
        for _ in range(20):
            time.sleep(2)
            item = random.randint(0,100)
            self.items.append(item)
            print("add item %s to items"%item)
            self.event.set()
            self.event.clear()
            print("cleared")
if __name__ == '__main__':
    t1 = Producer(event,items)
    t2 = Consumer(event,items)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(items)