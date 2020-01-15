#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   hi_logging.py
@Time    :   2020/01/15 09:32:38
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
import  logging
# 创建 logger
logger = logging.getLogger('simple')
logger.setLevel(logging.INFO)
# 创建输出处理器
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# 创建格式程序
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 设置格式化
ch.setFormatter(formatter)
# 增加处理器
logger.addHandler(ch)
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
if __name__ == '__main__':
    pass