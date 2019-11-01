#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   server_2.py
@Time    :   2019/11/01 09:05:29
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

this = '2'
next = '3'

servername = "example.chainTopology." + this
daemon = Pyro4.core.Daemon()
obj = chainTopology.Chain(this, next)
uri = daemon.register(obj)
ns = Pyro4.naming.locateNS()
ns.register(servername, uri)
# enter the service loop.
print("server_%s started" % this)
daemon.requestLoop()
if __name__ == '__main__':
    pass