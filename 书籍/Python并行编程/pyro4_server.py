#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   pyro4.py
@Time    :   2019/10/22 14:35:52
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   pyro4服务端
'''

# here put the import lib
import Pyro4
@Pyro4.expose
class Server(object):
    def welcome(self, name):
        return ("Hi welcome" + str(name))

def startServer():
    server = Server()
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(server)
    ns.register("server", uri)
    print("Ready, Object uri = ", uri)
    daemon.requestLoop()
if __name__ == '__main__':
    startServer()