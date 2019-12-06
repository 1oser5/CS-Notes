#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   improve_long_str.py
@Time    :   2019/12/06 14:52:42
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   优化超长字符串
'''

# here put the import lib
def brackets_log():
    print(("There is something really bad happened during the process. "
    "Please contact your administrator."
    ))

# also can do it this way
def multi_string():
    # it will count indent.so you must set the rest line to topic.
    # is is ugly but useful way.
    print("""There is something really bad happened during the process.
Please contact your administrator.   
    """)

# maybe best
from textwrap import dedent

def dedent_string():
    # dedent will ignore the indent in left.
    message = dedent("""
    Welcome, today's movie list:
    - Jaw (1975)
    - The Shining (1980)
    - Saw (2004)
    """)
    print(message)
if __name__ == '__main__':
    brackets_log()
    multi_string()
    dedent_string()