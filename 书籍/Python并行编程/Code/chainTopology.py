#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   chainToplogy.py
@Time    :   2019/11/01 09:11:07
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from __future__ import print_function
import Pyro4

class Chain(object):
    def __init__(self, name, next):
        self.name = name
        self.nextName = next
        self.next = None
    def process(self, message):
        if self.next is None:
            self.next = Pyro4.core.Proxy("PYRONAME:example.chain." + self.nextName)
        if self.name in message:
            print("Back at %s; the chain is closed! %s self.name")
            return ["complete at" + self.name]
        else:
            print("%s forwarding the message to the object %s"\
                % (self.name, self.nextName))
            message.append(self.name)
            result = self.next.process(message)
            result.insert(0, "passed on from" + self.name)
            return result
if __name__ == '__main__':
    pass