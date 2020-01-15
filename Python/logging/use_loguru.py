#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   use_loguru.py
@Time    :   2020/01/15 15:39:59
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from loguru import logger
import sys
logger.add(sys.stdout, format="{time} {level} {message}", filter='my_module', level='WARNING')
logger.add("file.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", level='WARNING')
logger.debug('This is it. beautiful and simple logging')
logger.info('This is it. beautiful and simple logging')
if __name__ == '__main__':
    pass