#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   chapter3.py
@Time    :   2019/12/22 12:38:12
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   Python3-cookbook 第三章 数字日期和时间
'''

# 1.数字的四舍五入
""" 使用 round 进行舍入运算 """
x = 1.2345
round(x, 1) # 1.2
print(round(x, 3)) # 1.234
print(round(1.27,1)) # 1.3
# 传给 round 的 ndigits 参数可以为负数，这样会在正数为上运算
a = 1627731
round(a, -1) # 1627730
round(a, -2) # 1627700
# 如果你只想输出固定长度的树，不需要 round，使用 format 即可，也会四舍五入
x = 1.23456
format(x, '0.2f') # 1.23

# 2.浮点数的精确运算
""" 浮点数无法精确表示 十进制数，即使是最简单的数学运算也会出错，需要精确运算，使用 decimal 模块"""
a = 4.2
b = 2.1
c = a + b
b == (6.3) #False
# 由于底层 CPU 和 IEEE 754 标准通过自己的浮点单位进行算术的特征
#使用 decimal 模块
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
c = a + b # Decimal('6.3')
print(c) # 6.3
c == Decimal('6.3') #True
# 允许控制计算的每一方面，需要创建上下文来改变它的设置
from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
a / b # 0.7647058823529411764705882353
with localcontext() as ctx:
    ctx.prec = 3
    a / b # 0.765
with localcontext() as ctx:
    ctx.prec = 50
    a / b # 0.7647058823529411764705882353

# 4.二八十六进制整数
""" 使用 bin(), oct(), hex() 转化二八十六进制 """
x = 1234
bin(x) # '0b10011010010'
oct(x) # '0o2322'
hex(x) # '0x4d2'
# 不想输出前缀可以使用 format() 函数
format(x, 'b') # '10011010010'
format(x, 'x') # '4d2'
# 如果是负数，输出结果会带一个符号
x = -1234
format(x, 'b') # '-10011010010'
#如果想使用无符号，需要添加一个最大位长度值
format(2**32 + x, 'b')  # '11111111111111111111101100101110'
# 不同进制整数字符串转化为数字，使用 int(), 不需要携带前缀
int('4d2', 16) # 1234

# 5.字节到大整数的打包与解包
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
# 将 bytes 解析为整数
int.from_bytes(data, 'little') # 小端
int.from_bytes(data, 'big') # 大端
# 大整数转化为字节字符串
x = 94522842520747284487117727783387188
x.to_bytes(16, 'little') # 小端 b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'
x.to_bytes(16, 'big') # 大端 b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

# 6.复数运算
""" 使用 complex(real, imag) 或者带 j 后缀的浮点数来指定一个复数
复数支持所有常见的数学运算，复杂些的可以使用 cmath 模块
"""
a = complex(2, 4) # 2+4j  
b = 3 - 5j # 3-5j
a.real # 实部 2.0
a.imag # 虚部 4.0
a.conjugate() # 共轭复数 2-4j
# 所有常见数学运算都支持
a + b  # 5-1j
a * b # 26+2j
# 复杂运算使用 cmath
import cmath
cmath.sin(a) # (24.83130584894638-11.356612711218174j)

# 7.无穷大和NAN
""" 你可以使用 float 来创建 无穷大和 NaN
ATTENTION NaN 之间的比较总是返回 False
 """
a = float('inf')
b = float('-inf')
c = float('nan')
# 通过 math.isinf() 和 math.isnan 进行测试
import math
math.isinf(a) # True
math.isnan(c) # True
# 无穷大在某些计算时会传播
a = float('inf')
a + 45 # inf
a * 10 # inf
10 / a # 0.0
# 但是某些未定义操作则返回 NaN
a = float('inf')
a / a # nan
b = float('-inf')
a + b # nan
# NaN 会在所有值中传播，并不产生异常
c = float('nan')
c + 23 # nan
c /2 # nan
# NaN 间的比较总是返回 False
c = float('nan')
d = float('nan')
c == d # False
c is d # False

# 8.分数运算
""" 使用 fractions 模块进行分数运算 """
from fractions import Fraction
a = Fraction(5, 4) # 5/4
b = Fraction(7, 16) # 7/16
a + b # 27/16
c = a * b # 35/64
c.numerator # 35 
c.denominator # 64
# 转化为浮点数
float(c) # 0.546875
# 限制分母的值
print(c.limit_denominator(8)) # 4/7
# 将浮点数转化为分数
x = 3.75
y = Fraction(*x.as_integer_ratio()) # Fraction(15, 4)

# 9.大型数组运算
""" Numpy 中的数组对象更适合进行数组运算
Numpy 底层实现使用了 C 或者 Fortran 语言的机制分配内存，
也就是说他们是一个非常大的连续的并由同类型数据组成的内存区域
 """
import numpy as np
ax = np.array([1, 2, 3, 4, 5])
ay = np.array([5, 6, 7, 8])
ax * 2 # array([2, 4, 6, 8])
ax + 10 # array([11, 12, 13, 14])
ax + ay # array([ 6, 8, 10, 12])
# 想要使用多项式
def f(x):
    return 3*x**2 - 2**x +7
f(ax) # array([ 8, 15, 28, 47])

# 11.随机选择
""" 从一个序列中随机抽取若干元素，或者生成几个随机数
使用 random 模块，其使用 Mersenne Twister 算法，这是一个确定性算法
因此有关加密部分，不要使用 random
 """
import random
values = [1, 2, 3, 4, 5, 6]
random.choice(values) # 3 随机抽取一个
# 随机抽取 N 个
random.sample(values, 2) # [6, 2]
random.sample(values, 3) # [6, 2, 1]
# 打乱顺序
random.shuffle(values) # [2, 4, 6, 5, 3, 1]
# 生成随机整数
random.randint(0, 10) # 2 参数为范围，左右都为闭区间，0，10都能取到
# 生成 0-1 浮点数
random.random() # 0.9406677561675867

# 12.基本的日期和时间转化
""" 使用 datetime 处理时间 """
# 计算时间段
from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
c.days # 2
c.seconds # 37800
c.seconds / 3600 # 10.5

# 15.字符串转换为日期
""" 使用 datetime 的 strptime 函数转化
ATTENTION strptime 的性能比你想象的差很多，因为他是纯 Python 实现的，并且要处理所有系统本地时间
 """
from datetime import datetime
text = '2012-09-20'
# str -> time
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y # datetime.timedelta(3, 77824, 177393)
# time -> str
nice_z = datetime.strftime(z, '%A %B %d, %Y') # 'Sunday September 23, 2012'