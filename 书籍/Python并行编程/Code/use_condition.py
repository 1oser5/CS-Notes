#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_condition.py
@Time    :   2019/10/14 10:39:56
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用条件进行线程同步
'''

# here put the import lib
import threading
import time
condition = threading.Condition()
items = []

class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def consume(self):
        global condition
        global items
        condition.acquire()
        #等待通知
        if len(items) == 0:
            condition.wait()
            print("conmuser is wait")
        items.pop()
        print("consume one item")
        condition.notify()
        condition.release()
    def run(self):
        for _ in range(20):
            self.consume()
            time.sleep(2)

class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def produce(self):
        global condition
        global items
        condition.acquire()
        #等待通知
        if len(items) == 10:
            condition.wait()
            print("producer is wait")
        items.append(1)
        print("producer one item")
        condition.notify()
        condition.release()
    def run(self):
        for _ in range(20):
            self.produce()
            time.sleep(1)
if __name__ == '__main__':
    p = Producer()
    c = Consumer()
    p.start()
    c.start()
    p.join()
    c.join()