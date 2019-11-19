#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   define_a_thread.py
@Time    :   2019/10/11 08:47:41
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   定义一个线程类
'''

# here put the import lib
import threading
import time

class myThread(threading.Thread):
    def __init__(self,name,counter):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
    def run(self):
        print('start' + self.name)
        print_time(self.name, self.counter, 5)
        print('Exiting' + self.name)

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s:%s"%(threadName, time.ctime(time.time())))
        counter -= 1
if __name__ == '__main__':
    thread1 = myThread("Thread-1",1)
    thread2 = myThread("Thread-2",2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()