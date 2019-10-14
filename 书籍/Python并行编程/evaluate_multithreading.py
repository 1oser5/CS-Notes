#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   evaluate_multithreading.py
@Time    :   2019/10/14 12:30:18
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   多线程性能评估
'''

# here put the import lib
import threading

class threads_obj(threading.Thread):
    def run(self):
        fun()
class nothreads_obj(object):
    def run(self):
        fun()
def fun():
    a, b = 0, 1
    for i in range(10000):
        a, b = b, a + b
def non_threads(num):
    funcs = []
    for _ in range(num):
        funcs.append(nothreads_obj())
    for i in funcs:
        i.run()
def threads(num):
    funcs = []
    for _ in range(num):
        funcs.append(threads_obj())
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()

def show_results(fun_name, results):
    print("%-23s %4.6f seconds"%(fun_name, results))   
if __name__ == '__main__':
    import sys
    from timeit import Timer
    repeat = 100
    number = 1
    num_threads = [1, 2, 4, 8]
    print('Starting tests')
    for i in num_threads:
        t = Timer("non_threads(%s)" % i, "from __main__ import non_threads")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("non_threads (%s iters)" % i, best_result)
        t = Timer("threads(%s)" % i, "from __main__ import threads")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("threads (%s threads)" % i, best_result)
        print('Iterations complete')