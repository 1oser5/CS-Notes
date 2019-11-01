#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   server_1.py
@Time    :   2019/10/22 15:08:54
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from __future__ import print_function
import Pyro4
import chainTopology

this = "1"
next = "2"
servername = "example.chainToppology." + this
daemon = Pyro4.core.Daemon()
obj = chainTopology.Chain(this, next)
uri = daemon.register(obj)
ns = Pyro4.naming.locateNS()
ns.register(servername, uri)

print("server _%s started"%this)
daemon.requestLoop()
if __name__ == '__main__':
    pass