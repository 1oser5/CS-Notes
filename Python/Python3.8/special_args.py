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
    pass
# kwd_only    
def kwd_only_args(*, a):
    pass
def combined_example(pos_only, /, standard, *, kwd_only):
    pass
if __name__ == '__main__':
    standard_args(a=2)
    standard_args(2)
    positional_only(2)
    kwd_only_args(a=2)
    combined_example(1, 2, kwd_only=2)
    combined_example(standard = 1, kwd_only=2)