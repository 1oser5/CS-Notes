#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2020/01/21 10:35:11
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib

import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    # base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    # return os.path.join(base_path, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)
if __name__ == '__main__':
    s = resource_path('流水线语法.md')