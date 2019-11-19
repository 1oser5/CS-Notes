#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   pyro4_chain_cilent.py
@Time    :   2019/10/22 15:04:47
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from __future__ import print_function

import Pyro4

obj = Pyro4.core.Proxy("PYRONAME:example.chain.A")
print("Result = %s" % obj.process(["hello"]))
if __name__ == '__main__':
    pass