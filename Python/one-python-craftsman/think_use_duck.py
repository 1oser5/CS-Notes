#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   think_use_duck.py
@Time    :   2019/12/06 15:20:08
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   面向接口而非具体实现
'''

# here put the import lib

# this function just can be used by list
def remove_upper(comments: [str]):
    index = 0
    for comment in comments:
        comments[index] = comment.lower()
        index += 1
    return comments

# best
def remove_upper_iter(comments: iter):
    for comment in comments:
        comment = comment.strip()
        yield comment.lower()
if __name__ == '__main__':
    comments =[
    "Implementation note",
    "Changed",
    "ABC for generator",
]
print(remove_upper(comments))
for comment in remove_upper_iter(comments):
    print(comment)