#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   calling_Process.py
@Time    :   2019/10/10 10:31:42
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   调用进程
'''

# here put the import lib
import os
import sys


if __name__ == '__main__':
    program = "python"
    print("Process calling")
    arguments = ["called_Process.py"]
    #调用 called_Process.py 脚本
    os.execvp(program,(program,) + tuple(arguments))
    print("Good Bye")