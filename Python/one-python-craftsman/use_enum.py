#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_enum.py
@Time    :   2019/12/06 14:40:19
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用 enum 枚举类改善代码
'''

# here put the import lib
from enum import IntEnum

class SchoolSource(IntEnum):
    """定义枚举类"""
    STUDENT_LOGIN = 1
    TEACHER_LOGIN = 2

def check_login(arg):
    if arg == SchoolSource.STUDENT_LOGIN:
        print('user is a student')
    elif arg == SchoolSource.TEACHER_LOGIN:
        print('user is a teacher')
if __name__ == '__main__':
    check_login(1)
    check_login(2)