#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   helloPythonWithTreads.py
@Time    :   2019/10/10 10:46:46
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from threading import Thread
from time import sleep

class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message="Hello Paraller Python CookBook\n"
    
    def print_message(self):
        print(self.message)
    
    def run(self):
        print("Thread Starting\n")
        x = 0
        while(x < 10):
            self.print_message()
            sleep(2)
            x += 1
        print("Thread Ended\n")
if __name__ == '__main__':
    print("Process Started")

    hello = CookBook()

    hello.start()

    print("Process Ended")