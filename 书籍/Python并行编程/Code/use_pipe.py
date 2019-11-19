#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_pipe.py
@Time    :   2019/10/17 14:59:51
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用管道进行进程通讯
'''

# here put the import lib
import multiprocessing

def create_item(pipe1):
    _output,_ = pipe1
    for i in range(10):
        _output.send(i)
    _output.close()

def multi_item(pipe1,pipe2):
    close, _input = pipe1
    print("pipe1",pipe1)
    close.close()
    _output,_ = pipe2
    try:
        while True:
            item = _input.recv()
            _output.send(item*item)
    except EOFError:
        _output.close()
if __name__ == '__main__':
    # 第一个进程管道发出数字
    pipe1 = multiprocessing.Pipe(True)
    p1 = multiprocessing.Process(target=create_item,args=(pipe1,))
    p1.start()
    #第二个进程管道接受数字
    pipe2 = multiprocessing.Pipe(True)    
    p2 = multiprocessing.Process(target=multi_item,args=(pipe1,pipe2,))
    p2.start()
    pipe1[0].close()
    pipe2[0].close()
    try:
        while True:
            print(pipe2[1].recv())
    except EOFError:
        print("End")