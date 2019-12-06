#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_raise.py
@Time    :   2019/12/06 15:32:57
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   使用异常来进行错误流程处理才是更地道的做法
'''

# here put the import lib
from enum import IntEnum

class ItemSource(IntEnum):
    MAX_NAME_LENGTH = 5
    MAX_ITEM_LENGTH = 5
class CreateItemError(Exception):
    """创建 Item 失败抛出的异常"""
    pass
class Item(object):
    def __init__(self,items):
        self.items = items
    def create_item(self, name):
        """创建一个新的 Item

        raises: 无法创建时抛出 CreateItemError
        """
        if len(name) > ItemSource.MAX_NAME_LENGTH:
            raise CreateItemError('name of item is too long')
        if len(self.items) > ItemSource.MAX_ITEM_LENGTH:
            raise CreateItemError('items is full')
        self.items.append(name)
        return name
if __name__ == '__main__':
    item = Item(['1','2','3','4'])
    # item.create_item('12345667777')
    item.create_item('12')
    item.create_item('123')
    item.create_item('123')
