#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   set_bool.py
@Time    :   2019/12/06 14:34:35
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   如何设定自定义类的布尔值
'''

# here put the import lib
class User(object):
    def __init__(self, users):
        self.users = users
    # 方法一：设置 __bool__ 函数
    def __bool__(self):
        return False
    # 方法二：设置 __len__ 函数
    def __len__(self):
        return len(self.users)
if __name__ == '__main__':
    # 方法一 > 方法二
    user_list = ['Adam','Bob','Ali','Jack']
    u = User(user_list)
    if u:
        print('It is a True class')
    else :
        print('It is a False class')
    #输出 'It is a False class'
    
    