#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   chapter5.py
@Time    :   2019/12/27 15:21:46
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   Python3-cookbook 第五章 文件与 IO
'''

# 1.读写文本数据
""" 使用 open 函数打开文本 """
# 读取整个文件
with open('somefile.txt', 'rt') as f:
    data = f.read()
# 按行读取
with open('somefile.txt', 'rt') as f:
    for line in f:
        pass
# 文件读写操作默认使用系统编码，可以调用 sys.getdefaultcoding() 得到，大多为 utf-8
# 你也可以指定其他编码方式
with open('somefile.txt', 'rt', encoding='latin-1') as f:
    pass
# 不使用 with 需要手动关闭
f = open('somefile.txt', 'rt')
data = f.read()
f.close()
# Unix 和 Windows 换行符问题，Python 可以识别所有的普通换行符将其转换为单个 \n 字符
# 可以通过 newline 进行修改
# 默认
f = open('hello.txt', 'rt')
f.read() # 'hello world!\n'
# 修正为 \r\n
g = open('hello.txt', 'rt', newline='')
g.read() # 'hello world!\r\n'
# 可以使用 errors 来处理错误
# 将坏字符识别为 U+fffd 
f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
# 忽略怀字符
f = open('sample.txt', 'rt', encoding='ascii', errors='ignore')

# 2.输出至文件中,文件是二进制会报错
with open ('somefile.txt', 'wt') as f:
    print('Hello World!', file=f)

# 3.使用其他分隔符和终止符打印
print('ACME', 50, 91.5, sep=',') # ACME,50,91.5
print('ACME', 50, 91.5, sep=',', end='!!\n') # ACME,50,91.5!!

# 4.读写字节数据
""" 使用 rb 或 wb 的 open 函数来读写字节数据 """
# 读操作
with open('somefile.bin', 'rb') as f:
    data = f.read()
# 写操作
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')
# 从二进制文件读取或者写入文本数据，必须进行解码和编码
with open('somefile.bin','rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')
with open('somefile.txt', 'rt') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))
# 二进制 I/O 可以将数组和 C 结构体直接写入
import array
nums = array.array('i',[1, 2, 3, 4])
with open('data.bin', 'wb') as f:
    f.write(nums)
# 这适用于任何实现了 “缓存接口” 的对象，这种对象会直接暴露其底层内存缓存区给能处理它的操作，二进制写入
# 就是其中之一
# 通过 readinto 读取二进制底层内存
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)
# 要注意平台相关性和字节顺序（大小端）

# 5.不允许文件覆盖
""" 使用 x 来替换 w 防止文件覆盖 """
# 文本文件
with open('somefile.txt', 'xt') as f:
    pass
# 二进制文件
with open('data.bin', 'xb') as f:
    pass

# 6.字符串 I/O 操作
""" 使用 io.StringIO() 和 io.BytesIO() 来创建类文件对象，这在单元测试时很有效 """
import io
s = io.StringIO()
# 直接写入
s.write('Hello World\n')
# 重定向写入
print('This is a test', file=s)
# 全部删除
s.getvalue()  # 'Hello World\nThis is a test\n'
# 生成一个有内容文件 
s = io.StringIO('Hello\nWorld\n')
s.read(4) # Hell
s.read() # 'o\nWorld\n'

# 7.读写压缩文件
""" 使用 gzip 和 bz2 读写压缩文件 """
# 读操作
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()
# 写操作
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

# 8.在固定长度的数据块上迭代
""" 使用 iter 配合 functools.partial() """
from functools import partial
RECORD_SIZE = 32
with open('somefile.data', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        pass

# 9.读取二进制数据到可变缓存区
""" readinto 能用来为预先分配内存的数组填充数据，和普通方法不同，readinto 填充已存在的缓存区而不是为新对象
重新分配内存
ATTENTION 需要检查 readinto 的返回值，如果字节数小于缓存区，表明数据被截断或者破坏了
 """
import os.path
# 直接读取入 bytearray
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf
# 使用用例
with open('data.bin', 'wb') as f:
    f.write(b'Hello World')
buf = read_into_buffer('data.bin') # bytearray(b'Hello World')
# 使用 memoryview 通过零复制方式对已存在的缓存区执行切片操作,甚至还能修改内容
m1 = memoryview(buf)
m1[-5:] # <memory at 0x100681390>
m1[:] = b'WORLD'
buf # bytearray(b'Hello WORLD')