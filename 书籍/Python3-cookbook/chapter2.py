#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   chapter2.py
@Time    :   2019/12/20 16:07:07
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   Python3-cookbook 第二章 文本和字符串
'''


# 1.使用多个界定符分隔字符串
"""使用 re.split 可以更加灵活的切割字符串"""
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
l = re.split(r'[;,/s]\s*', line)
print(l) # ['a', 'df fjdk', 'afed', 'fjek', 'a', 'df', 'foo']
# 可以使用括号捕获分组
fields = re.split(r'(;|,|\s)\s*', line)
print(fields) # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']


# 2.检查开头或结尾匹配
""" 使用 str.endswith 和 str.startwith 进行开头或结尾匹配
可以匹配多个元素，但传入的必须为元组
"""

filename = 'spam.txt'
filename.endswith('.txt') # True
#匹配多种情况
filenames = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
print([name for name in filenames if name.endswith(('.c','.h'))]) # ['foo.c', 'spam.c', 'spam.h']

# 3.使用 shell 通配符匹配字符串
"""使用 Unix 进行字符串匹配，比较奇怪。。"""
from fnmatch import fnmatch, fnmatchcase

# On OS X (Mac)
fnmatch('foo.txt', '*.TXT') # False
# On Windows
fnmatch('foo.txt', '*.TXT') # True