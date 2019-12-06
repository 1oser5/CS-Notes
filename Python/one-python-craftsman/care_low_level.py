#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   care_low_level.py
@Time    :   2019/12/06 15:05:48
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   关注细节来编写出更好的代码
'''

# here put the import lib

# avoid to init or expand list,it is expensive
# normal
list = [(i for i in range(100))]
# best
generator = (i for i in range(100))

# when you want insert a element at hand in list,it takes O(n).
# you should use collections.deque,because it takes O(1).
from collections import deque
d = deque()
d.appendleft('head')

# use dict or set to judge whether a element in.because they create by Hash Table.
# item in [] takes O(n),item in {} takes O(1).
user_list = ['Adam', 'Bob', 'Simon']

check_list = ['Adam', 'Jack', 'Ali']
# normal
for user in user_list:
    if user in check_list:
        pass
# good
check_dict = set(check_list)
for user in user_list:
    if user in check_dict:
        pass
    
if __name__ == '__main__':
    pass