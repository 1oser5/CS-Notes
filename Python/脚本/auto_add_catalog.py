#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   自动添加md文件目录.py
@Time    :   2019/11/19 15:56:30
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   自动在md文件中添加目录
'''

# here put the import lib
import re
import os
import sys

def made_catalog(f_name: str) -> None:
    '''
    param 文件名
    
    生成md文件目录函数
    '''
    # todo 错误捕捉
    with open(f_name,'r+') as f:
        s = []
        n = f.read()
        l = n.split('\n')
        for i in l:
            if i and i[0] == '#':
                #获得缩进
                l = re.findall(r'#+',i)
                #将缩进值和目录内容放进 s 数组
                s.append((i[len(l[0])+1:].replace(' ',''),len(l[0]) - 1))
        #文件指针指向文件首
        f.seek(0,0)
        f.write('# 目录\n')
        for i in s:
            #缩进
            f.write('    ' * i[1])
            #索引添加
            f.write('+ [{0}](#{0})\n'.format(i[0]))
        f.write('\n'*5)
        f.write(n)
        print(' \033[1;35m {0} 自动生成目录成功 \033[0m!'.format(f_name))
if __name__ == '__main__':
    f_name = sys.argv[1]
    #判断是否为文件夹
    if os.path.isdir(f_name):
        print('\033[1;35m 输入为文件夹，遍历文件夹内所有 md 文件 \033[0m')
        #获得文件夹内所有文件
        files = os.listdir(f_name)
        #todo 递归调用文件夹
        for j in files:
            #跳过所有非 md 文件
            if os.path.splitext(j)[-1] != '.md':
                continue
            else:
                print('\033[1;35m 当前文件为 %s \033[0m' % j)
                p = input('是否需要生成[y/n]')
                if p == 'n':continue
                if p == 'y':
                    made_catalog(f_name+'/'+j)
                # todo 输入y/n之外的怎么处理
    elif os.path.isfile(f_name):
        made_catalog(f_name)
    else:
        print(' \033[1;35m 该文件不存在！ \033[0m!')

    