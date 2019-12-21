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

# 4.字符串匹配和搜索
""" 简单的字符串匹配可以使用 str.find 等工具
稍微复杂些的可以使用 re.match进行匹配
如果 某个模块使用多次，可以用 re.complie 预编译为模版，增加性能
ATTENTION match 之从头开始匹配。想要匹配所有情况，使用 findall
其返回一个列表，如果想要捕获分组，使用括号包裹。想要返回迭代器，使用 finditer
"""
# 简单匹配
text = 'yeah, but no, but yeah, but no, but yeah'
text.find('no') # 10 返回下标位置
# 复杂匹配
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
print(re.match(r'\d+/\d+/\d',text1)) # <re.Match object; span=(0, 7), match='11/27/2'>
print(re.match(r'\d+/\d+/\d',text2)) # None
# 预编译为模式对象
datepat = re.compile(r'\d+/\d+/\d+')
# 任意位置匹配
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text) # ['11/27/2012', '3/13/2013']
# 使用括号捕获分组，降低后续处理难度
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012') # <_sre.SRE_Match object at 0x1005d2750>
m.group(0)  # '11/27/2012'
m.group(1) #'11'
m.group(2) #'27'
m.group(3) #'2012'
m.groups() # ('11', '27', '2012')
# 可以这样赋值
month, day, year = m.groups()
# 多个匹配对象会返回多个元组
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text) # [('11', '27', '2012'), ('3', '13', '2013')]
for month, day, year in datepat.findall(text):
    print(f'{year}-{month}-{day}')
# 返回迭代
for m in datepat.finditer(text):
    print(m.groups())
    #('11', '27', '2012')
    #('3', '13', '2013')

# 5.字符串的搜索和替换
""" 字符串替换，简单情况使用 str.replace 复杂情况使用 re.sub
同样的，要增加新性能，可以使用 re.compile 进行预编
"""
# 简单替换
text = 'yeah, but no, but yeah, but no, but yeah'
text.replace('yeah', 'yep') # 'yep, but no, but yep, but no, but yep'
# 复杂替换
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
s = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text) # 第二个参数中的数字表示捕获组号
print(s) #'Today is 2012-11-27. PyCon starts 2013-3-13.'
# 更复杂，使用一个函数接受 match 对象，进行操作后返回
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
datepat.sub(change_date, text) # 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'
# 想要知道替换了几处地方，使用 subn
new_text, n = datepat.subn(r'\3-\1-\2', text)
n # 2

# 6.字符串忽略大小写的搜素替换
""" 为了忽略大小写，可以在使用 re 模块时加上 re.IGNORECASE 标志 
ATTENTION 下文的 mathccase 返回一个回调函数（参数必须为 match 对象），因为上文说 sub 可以接受一个回调函数
"""
text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags=re.IGNORECASE) # ['PYTHON', 'python', 'Python']
re.sub('python', 'snake', text, flags=re.IGNORECASE) # 'UPPER snake, lower snake, Mixed snake'
# 替换字符不会符合原文的大小写规范，你可以使用辅助函数
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        else:
            return word.lower()
    return replace
# 使用方法
re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE) #'UPPER SNAKE, lower snake, Mixed Snake'

# 7.最短匹配模式
""" 使用正则的非贪婪匹配 ？得到最短匹配值 """
str_pat = re.compile(r'"(.*)"')
text1 = 'Computer says "no."'
str_pat.findall(text1) # ['no.']
text2 = 'Computer says "no." Phone says "yes."'
str_pat.findall(text2) # ['no." Phone says "yes.']
# r'"(*.)"' 本意匹配被双引号包含的文字，但 * 操作是贪婪地，可以使用 ？
str_pat = re.compile(r'"(.*?)"')
str_pat.findall(text2) # ['no.', 'yes.']

# 8.多行匹配模式
""" 当你想用 . 去匹配任意字符时，要记住其不能匹配换行符的事实 """
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
print(comment.findall(text1)) # [' this is a comment ']
text2 = '''/* this is a
... multiline comment */
... '''
comment.findall(text2) # n
# 可以这样修改模式字符串来支持换行，(?:.|\n) 指定了一个非捕获组（仅用来匹配，而不能通过单独捕获）
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2) # [' this is a\n multiline comment ']
# 使用标志参数 re.DOTALL，使 . 匹配包括换行符在内的任意字符
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
comment.findall(text2)  # [' this is a\n multiline comment ']

# 9.将 Unicode 文本标准化
s1 = 'Spicy Jalape\u00f1o' # 'Spicy Jalapeño'
s2 = 'Spicy Jalapen\u0303o' # 'Spicy Jalapeño'
s1 == s2 # False
len(s1) # 14
len(s2) # 15
# 上面的 s1 使用了整体字符，s2 使用了组合字符，使用 unicodedata 修正类似问题
import unicodedata
# NFC 表示尽可能使用单一
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
t1 == t2 # True
# NFD 表示尽可能使用组合字符
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
t1 == t2

# 10. 正则匹配 Unicode
# \d+ 支持匹配 Unicode
import re
num = re.compile('\d+')
num.match('123') # <_sre.SRE_Match object at 0x1007d9ed0>
num.match('\u0661\u0662\u0663') # <_sre.SRE_Match object at 0x101234030>

# 11.删除字符串中不需要字符
""" 使用 strip() 删除开始或者结尾字符，lstrip() 和 rstrip() 分别从左右执行删除，默认为空白字符 """
# 替换空白或者换行符
s = ' hello world \n'
s.strip() # 'hello world'
s.lstrip() # 'hello world \n'
s.rsplit() # ' hello world'
# 替换指定字符
t = '-----hello====='
t.lstrip('-') # 'hello====='
t.strip('-=') # 'hello'
# 注意上述方法不会对字符串中的字符进行操作，如果咬着牙，可以使用 replace() 或者 正则
s = ' hello     world \n'
s.replace('   ','') # 'helloworld' 
re.sub(r'\s+', ' ', s) # 'hello world'

# 12.审查和清理字符串
""" 使用 str.translate() 清理字符串
ATTENTION 可能使用 str.replace() 更快些
"""
# 简单例子
s = 'pýtĥöñ\fis\tawesome\r\n'
remap = {
     ord('\t') : ' ',
     ord('\f') : ' ',
     ord('\r') : None # Deleted
}
a = s.translate(remap) # 'pýtĥöñ is awesome\n'

# 13. 字符串对齐
""" ljust()，rjust() 和 center() 进行字符串对齐"""
text = 'Hello World'
text.ljust(20) # 'Hello World         '
text.rjust(20) # '         Hello World'
text.center(20) # '    Hello World     '
# 接受可选填充字符
text.rjust(20, '=') # '=========Hello World'
# 使用 format 可以达到相同效果，< 在右边填充，> 在左边填充， ^ 居中
format(text, '>20') # '         Hello World'
# 指定填充字符，把它放到对齐字符前
print(format(text, '=>20')) # '=========Hello World'
# 多个值也可以使用
'{:>10} {:>10}'.format('Hello', 'World') # '     Hello      World'
# format 可以用来格式任何值
x = 1.2345
format(x, '>10') # '    1.2345'
format(x, '^10.2f') # '   1.23   '

# 14.合并字符串
""" 使用 join() 合并字符串，如果仅仅合并少数几个，使用 + 就行
ATTENTION + 的效率会比较低下，会引起内存复制以及垃圾回收操作
"""
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
','.join(parts) # 'Is,Chicago,Not,Chicago?'
# 注意无意义的拼接
a, b, c = '1', '2', '3'
print(a + ':' + b + ':' + c) # Ugly
print(':'.join([a, b, c])) # Stile ugly
print(a, b, c, sep=':') # Better

# 16.固定列宽格式化字符串
""" 使用 textwrap 格式化长输出 """

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
import textwrap
print(textwrap.fill(s, 70))  # 宽度为 70
# 使用 os.get_terminal_size() 获得终端尺寸大小
import os
# 要在终端使用下面代码
# os.get_terminal_size() # columns=80, lines=24

# 17.字符串处理 html 和 xml
# 使用 html.escape() 函数替换文本字符串中的 '<' 和 '>'
s = 'Elements are written as "<tag>text</tag>".'
import html
print(html.escape(s)) # Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;.

# 18.字符串令牌解析
"""使用 scanner 生成器实现不断的 match()
如果有多个匹配语句，并且一个模式恰好是另一个模式更长的子字符串，你要将长模式写在前面
 """
text = 'foo = 23 + 42 * 10'
# 你想把其指定为下述序列对
tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)' # 匹配以字母开头的可含有数字的名字
NUM = r'(?P<NUM>\d+)' # 匹配数字
PLUS = r'(?P<PLUS>\+)' # 匹配符号
TIMES = r'(?P<TIMES>\*)' # 匹配次数
EQ = r'(?P<EQ>=)' # 匹配等号
WS = r'(?P<WS>\s+)' # 匹配空白符
# ?P<TOKENNAME> 用于给一个模式起别名
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
# 使用 scanner() 方法，不断调用 match()
scanner = master_pat.scanner('foo = 42')
s = scanner.match() # <_sre.SRE_Match object at 0x100677738>
# lastgroup 是类型，value 是 值
s.lastgroup, s.group() # ('NAME', 'foo')
# 可以利用上述技术，将代码打包到一个生成器
from collections import namedtuple
def generate_tokens(pat, text):
    """ 返回生成器
    
    param: re pat 匹配模式
    param: str text 文本
    """
    Token = namedtuple('Token',['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match(), None):
        yield Token(m.lastgroup, m.group())
# 长短模式
LT = r'(?P<LT><)'
LE = r'(?P<LT><=)'
EQ = r'(?P<EQ>>=)'
# 应该这样写
master_pat = re.compile('|'.join([LE, LT, EQ])) # correct
# 如果这样写，识别 <= 时，会匹配为 LT + EQ ，而不是单独的 LE
master_pat = re.compile('|'.join([LT, LE, EQ]))

# 19.见 descent_parser.py

# 20.字节字符串操作

# 字节字符串支持大部分内置操作
data = b'Hello World'
data[0:5] # b'Hello'
data.startswith(b'Hello') # True
data.split() # [b'Hello', b'World']
data.replace(b'Hello', b'Hello Cruel') # b'Hello Cruel World'
# 同样适用于字节数组
data = bytearray(b'Hello World')
data[0:5] # bytearray(b'Hello')
data.startswith(b'Hello') # True
# 注意字节字符串索引返回的是整数而不是单独字符
b = b'Hello World'
b[0] # 72 ascii 码
