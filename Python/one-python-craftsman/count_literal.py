#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   count_literal.py
@Time    :   2019/12/06 14:46:45
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   不必预设字面量表达式
'''

# here put the import lib
import dis

def count_literal(use_time):
    if use_time > 950400:
        pass

def discount_literal(user_time):
    if user_time > 11 * 24 * 3600:
        pass

if __name__ == '__main__':
    dis.dis(count_literal)
    dis.dis(discount_literal)
    """Python 代码在执行时会被解释器编译成字节码，无论是否考虑字面量，字节码都是一致的

17          0 LOAD_FAST                0 (use_time)
            2 LOAD_CONST               1 (950400)
            4 COMPARE_OP               4 (>)
            6 POP_JUMP_IF_FALSE        8

18     >>    8 LOAD_CONST               0 (None)
            10 RETURN_VALUE
21           0 LOAD_FAST                0 (user_time)
            2 LOAD_CONST               1 (950400)
            4 COMPARE_OP               4 (>)
            6 POP_JUMP_IF_FALSE        8

22     >>    8 LOAD_CONST               0 (None)
            10 RETURN_VALUE

"""