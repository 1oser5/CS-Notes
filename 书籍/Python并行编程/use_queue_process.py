#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_queue_process.py
@Time    :   2019/10/17 14:37:55
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用队列进行进程通信
'''

# here put the import lib
import multiprocessing
import time
import random

class Producer(multiprocessing.Process):
    def __init__(self,queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
    def run(self):
        for i in range(10):
            i = random.randint(0,100)
            self.queue.put(i)
            print("%s append in queue"%i)
            print("lens of queue is",self.queue.qsize())

class Consumer(multiprocessing.Process):
    def __init__(self,queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            if self.queue.empty():
                print("queue is empty")
                break
            item = self.queue.get()
            print("%s is pop from queue"%item)
            time.sleep(2)

if __name__ == '__main__':
    q = multiprocessing.Queue()
    p = Producer(q)
    c = Consumer(q)
    p.start()
    c.start()
    p.join()
    c.join()