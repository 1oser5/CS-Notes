#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   pyro4_client.py
@Time    :   2019/10/22 14:43:40
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   pyro4客户端
'''

# here put the import lib
import Pyro4

uri = input("What is the Pyro uri of the greeting object").strip()
name = input("What is your name").strip()
server = Pyro4.Proxy("PYRONAME:server")
print(server.welcome(name))


if __name__ == '__main__':
    pass