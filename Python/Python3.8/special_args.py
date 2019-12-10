#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   special_args.py
@Time    :   2019/12/10 09:35:14
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   Python3.8 特殊参数
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
'''
# positional or keyword
def standard_args(a):
    pass

# positional only
def positional_only(a, /):
    

if __name__ == '__main__':
    pass