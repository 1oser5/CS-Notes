#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   condition_test.py
@Time    :   2019/10/14 10:57:35
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   3个线程按顺序答应出abc各十次
'''

# here put the import lib
import threading

condition = threading.Condition()
current = "A"

class ThreadA(threading.Thread):
    def run(self):
        global current
        condition.acquire()
        for _ in range(10):
            if current != "A":
                condition.wait()
            print("A")
        current = "B"
        condition.notify_all()
        condition.release()

class ThreadB(threading.Thread):
    def run(self):
        global current
        condition.acquire()
        for _ in range(10):
            if current != "B":
                condition.wait()
            print("B")
        current = "C"
        condition.notify_all()
        condition.release()

class ThreadC(threading.Thread):
    def run(self):
        global current
        condition.acquire()
        for _ in range(10):
            if current != "C":
                condition.wait()
            print("C")
        current = "A"
        condition.notify_all()
        condition.release()
if __name__ == '__main__':
    a = ThreadA()
    b = ThreadB()
    c = ThreadC()
    a.start()
    b.start()
    c.start()
    a.join()
    b.join()
    c.join()