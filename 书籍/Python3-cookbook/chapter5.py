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

# 10.内存映射的二进制文件
""" 想内存映射一个二进制文件到一个可变数组，目的是为了随机访问它的内容或者是原地修改
使用 mmap 模块
ATTENTION 内存映射并没有将整个文件都存储在内存之中，而是操作系统仅仅为文件内容保留了一段虚拟内存
当你访问不同区域时，这些区域的内容才根据需要被读取到内存区域
mmap 有些平台差异性，需要注意
 """
# 如果使用内存映射方式打开文件
import os
import mmap
def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)
# 初始化一个文件到指定大小
size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')
m = memory_map('data')  
len(m)  # 1000000
# 切片查看
m[0:10] # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
# 修改
m[0:11] = b'Hello World'
m.close()
# 可以作为上下文管理器使用
with memory_map('data') as m:
    print(len(m))

# 11.文件路径名操作
""" 使用 os.path 模块操作文件名 """
import os
path = '/Users/beazley/Data/data.csv'
# 获得路径最后一部分
os.path.basename(path) # 'data.csv'
# 获得文件夹名
os.path.dirname(path) # '/Users/beazley/Data'
# 连接路径
os.path.join('tmp', 'data',os.path.basename(path)) # 'tmp/data/data.csv'
# 扩展用户目录
path = '~/Data/data.csv'
os.path.expanduser(path) # '/Users/beazley/Data/data.csv'
# 分离文件后缀名
os.path.splitext(path) # ('~/Data/data', '.csv')

# 12.测试文件是否存在
""" 使用 os.path 模块来测试文件或者目录是否存在
ATTENTION 要小心权限问题
"""
import os
# 判断文件or文件夹
os.path.exists('/etc/passwd') # True
# 判断是否为文件
os.path.isfile('/etc/passwd')
# 判断是否为文件夹
os.path.isdir('/etc/passwd')
# 判断是否为符号链接
os.path.islink('/usr/local/bin/python3')
# 判断是否为硬链接
os.path.realpath('/usr/local/bin/python3')
# 获得文件大小
os.path.getsize('/etc/passwd') # 3369
# 获得修改时间
os.path.getmtime('/etc/passwd')

# 13.获得文件夹中的文件列表
""" 使用 os.listdir 结合其他库进行筛选 """
import os
names = os.listdir('somedir')
# 使用列表推导式进行筛选普通文件
names = [name for name in os.listdir('somedir') if os.path.isfile(os.path.join('somedir', name))]
# 使用 startswith 和 endswith 也很有效
names = [name for name in os.listdir('somedir') if name.endwith('.py')]
# 文件名匹配也可以考虑 glob 和 fnmatch
import glob
pyfiles = glob.glob('somedir/*.py')

# 14.忽略文件名编码
""" 所有文件名都会根据 sys.getfilesystemencoding 返回的文本编码来编码或解码
如果想忽略该编码，使用一个原始字节字符串指定一个文件名即可
"""
with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy!')
import os
os.listdir('.') # ['jalapeño.txt']
os.listdir(b'') # [b'jalapen\xcc\x83o.txt']

# 16.增加或者改变已打开文件编码
""" 使用 io.TextIOWrapper 修改编码，二进制对象直接修改
文本文件，首先是要 detach 移除编码层，然后在使用新的编码代替
I/0 系统由一系列层次结构组成，io.TextIOWrapper 是解码编码的文本处理层
io.BufferedWriter 是一个处理二进制数据的带缓存的 I/O 层，io.FileIO 是一个表示操作系统底层文件描述符
的原始文件。
 """
# 二进制对象，直接包装
u = b'\x00'
f = io.TextIOWrapper(u, encoding='utf-8')
# 修改已打开的文本模式的文件编码方式，使用 detach 移除已存在编码层，使用新编码代替
import sys
sys.stdout.encoding # 'UTF-8'
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
sys.stdout.encoding # 'latin-1'
# 可以用这种技术处理文件，错误机制
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii',errors='xmlcharrefreplace')

# 17.在文本模式打开的文件中写入原始的字节数据
""" 使用 buffer 直接写入二进制数据，同时读取 buffer 可以规避文本编码层 """
import sys
# 直接写入 buffer 即可
sys.stdout.buffer.write(b'Hello\n')

# 19.创建临时文件和文件夹
""" 需要创建一个临时文件和文件夹，使用完成后自动销毁 """
from tempfile import TemporaryFile
# 支持 with 操作
with TemporaryFile('w+ts') as f:
    f.write('Hello World\n')
# 参数和 open 函数一样
with TemporaryFile('w+t', encoding='utf-8', error='ignore') as f:
    pass
# 一般是没有名字和目录的，可以使用 NamedTemporaryFile 确定名字
from tempfile import NamedTemporaryFile
with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)
# 如果不想关闭文件时被删除，传递 delete 关键字参数
with NamedTemporaryFile('w+t', delete=False) as f:
    print('filename is:', f.name)
# 创建临时目录,结束就被销毁
from tempfile import TemporaryDirectory
with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)

# 21.序列化Python对象
""" pickle 序列化对象为字节流
ATTENTION 不要对不信任的数据使用 pickle.load()
因为 pickle 在加载时有一个副作用就是它会自动加载相应模块并构造实例对象
pickle 是 Python 特有的附着在源码上的，如果需要长期存储数据的时候不应该选用
 """
import pickle
# 存入文件
data = '...' # some python object
f = open('somefile', 'wb')
pickle.dump(data, f)
# 将对象转为字符串
s = pickle.dumps(data)
# 从文件恢复对象
f = open('somefile', 'rb')
data = pickle.load(f)
# 从字符串中恢复
data = pickle.loads(s)
# 序列化多个后展开
f = open('somedata', 'wb')
pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()
f = open('soemdata', 'rb')
pickle.load(f) # [1, 2, 3, 4]
pickle.load(f) # 'hello'
pickle.load(f) # {'Apple', 'Pear', 'Banana'}
# 某些依赖外部状态的对象，无法序列化，可以通过定义 __getstate__ 和 __setstate__ 来绕过
# 序列化调用 __getstate__ 反序列化调用 __setstate__
import time
import threading
class Countdown():
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()
    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)
    def __getstate__(self):
        return self.n
    def __setstate__(self, n):
        self.__init__(n)
