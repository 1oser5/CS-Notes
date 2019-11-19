#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_queue.py
@Time    :   2019/10/14 12:13:26
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用 queue 进行线程通信
'''

# here put the import lib
import threading
import random
from queue import  Queue
import time
class Producer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        for _ in range(10):
            item = random.randint(0,100)
            self.queue.put(item)
            print("item %s put in queue"%item)
            time.sleep(1)
class Consumer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            item = self.queue.get()
            self.queue.task_done()
            print("pop %s form queue"%item)    
if __name__ == '__main__':
    queue = Queue()
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()