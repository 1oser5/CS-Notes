#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   simple_logging.py
@Time    :   2020/01/15 10:28:28
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
import logging
import logging.config
logging.config.fileConfig('/Users/xtl/Desktop/Me/CS-Notes/Python/logging/simple_logging.conf')
logger = logging.getLogger('root')
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
if __name__ == '__main__':
    pass