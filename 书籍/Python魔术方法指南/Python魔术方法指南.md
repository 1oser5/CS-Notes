## 介绍

主要介绍了一些 Python 中的魔术方法，以及相关的应用。

## 构造和初始化

`__init__` 用来新建对象，但事实上在新建对象时，第一个被调用的方法为 `__new__`(其在类继承自一个不可变对象时会用到)，而在删除时，有一个 `__del__`方法，作为结束。

`__init__` 和 `__new__` 为解析器，而 `__del__` 更像一个析构器。如果对象存在，则不能保证 `__del__` 被执行。

> 析构函数(destructor) 与构造函数相反，当对象结束其生命周期，如对象所在的函数已调用完毕时，系统自动执行析构函数。 析构函数往往用来做“清理善后” 的工作（例如在建立对象时用new开辟了一片内存空间，delete会自动调用析构函数后释放内存）。

下面代码实现了一个保证关闭文件流的 FileObject 类。
```python
import os

class FileObject(object):
    def __init__(self, filename, filepath):
        self.file = open(os.path.join(filepath, filename), 'r+')
    def __del__(self):
        self.file.close()
        del self.file
```

## 使用定制类

如果你想要判断两者是不是相等，你可以这样写
```python
if instance.equals(other_instance):
    #do something
```

或者直接使用 `__eq__` 方法进行比较。

### 用于比较的魔术方法

`__cmp__` 是最基本的比较方法，他实际上实现了所有符号的比较，但是规则不够统一（比较不同实例是会使用不同规则），当其返回正数时表示 `>`，返回负数时表示 `<`，`0` 时表示等于。

+ `__eq__`: 定义了**等号**行为 `==`
+ `__ne__`: 定义了**不等号**行为 `!=`
+ `__lt__`: 定义了**小于**行为 `<`
+ `__gt__`: 定义了**大于等于**行为 `>=`

```python
class Word(str):
    def __new__(self,word):
        #由于继承于不可变对象，初始化在 new 中
        if ' ' in word:
            word = word[:word.index(' ')] #第一个空格前的单词
        return str.__new__(cls, word)
    def __eq__(self, other):
        return len(self.word) == len(other)
    def __ne__(self, other):
        return len(self.word) != len(other)
    def __lt__(self, other):
        return len(self.word) < len(other)
    def __gt__(self, other):
        return len(self.word) >= len(other)
```

你也可以使用标准库中的 `functools.total_ordering` 来定义比较，你只需要定义一个 `__eq__` 和另一个（比如 `__gt__` 和 `__lt__`），他会使用装饰器实现剩余方法。

> 代价是会让执行速度更加缓慢和派生比较方法堆栈回溯会更为复杂。

### 数值处理的魔术方法

#### 一元操作符

+ `__pos__`: 实现了 `+` 的特性
+ `__neg__`: 实现了 `-` 的特性
+ `__abs__`: 实现了内置 abs() 函数特性
+ `__invert__`: 实现了 `~` 符号特性（取反）

### 算数操作符
+ `__add__(self, other)` 实现加法。
+ ` __sub__(self, other)` 实现减法。
+ `__mul__(self, other)` 实现乘法。
+ `__floordiv__(self, other)` 实现 // 符号实现的整数除法
+ `__div__(self, other)` 实现 / 符号实现的除法。
+ `__truediv__(self, other)` 实现真除法。注意只有只用了 `from __future__ import division` 的时候才会起作用。
+ `__mod__(self, other)` 实现取模算法 % `__divmod___(self, other)` 实现内置 divmod() 算法。
+ `__pow__ `实现使用 ** 的指数运算。
+ `__lshift__(self, other)` 实现使用 << 的按位左移动。
+ `__rshift__(self, other)` 实现使用 >> 的按位左移动。
+ `__and__(self, other)` 实现使用 & 的按位与。
+ `__or__(self, other)` 实现使用 | 的按位或。
+ `__xor__(self, other)` 实现使用 ^ 的按位异或。


### 反运算

反运算将操作数的位置进行了调换
```python
# normal add
a + b

# radd

b + a
```

所有算数运算符都支持反运算。大部分命令为原有命令加上一个 `r`，比如加法反运算(`__radd__`)。


### 增量赋值

```
x = 5
x += 1
```

可以使用使用 `__iadd__(self, other)` 实现复制加法，其他都是在原有命令加上一个 `i` 即可。

### 定义类型转换

很多方法来支持强制转换，`__int__` 实现整形的强制转换，还有很多类似的方法


### 表现类

使用 `__str__` 和 `__repr__` `__repr__` 返回的是机器读取的输出，而 `__str__` `__str__` 面向用户，而 `__repr__` 面向程序员。

### 控制属性访问

`__getattr__` 用于获取类中的属性，你可以在用户试图获取一个不存在的属性时，可以进行警告和报错，`__setattr__` 用来定义属性，而 `__delattr__` 用来删除属性，在使用 `__setattr__` 和 `__delattr__` 时要十分注意递归调用，看下面的例子。

```python
class Student(object):
    def __init__(self, name):
        self.name = name
    def __setattr__(self, new_name):
        #下面的操作会导致递归调用，以为你在使用 = 赋值时，会调用 __setattr__本身。
        self.name = new_name
    def __del__(self, name):
        #相同的递归错误
       del self['name']

    ## 正确的用法
    def __setattr__(self, name):
        # 定制特有属性
        self.__dict__[name] = value
```

定制属性访问非常强大，事实上 Python 不会试图将那些不好的部分变得不可能，而是让他那以实现，下面是一个属性控制的例子。

```python
class AccessCounter(object):
    def __init__(self, val):
        super(AccessCounter, self).__setattr__('counter', 0)
        super(AccessCounter, self).__setattr__('val', val)
    def __setattr__(self, name):
        if name = 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter+1)
        else:
            raise SetError('No such attributes!')
    def __delattr__(self, name):
        if name = 'value':
            super(AccessCounter, self).__setattr__('counter', 0)
        else:
            raise SetError('No such attributes!')
```

使用 super 进行了变量管理，使得所有的变量都为同一个父类属性。


### 定制序列

你必须实现一些特定的类方法来实现某些功能，比如你想要能够使用 `self[key]` 来获得 `value`值，需要定义 `__getitem__` 属性。想使用 `self[key] = value` 时，需要定义 `__setitem__`。当你需要类可以被迭代时，定义 `__iter__`。

一个简单的例子

```
class FunctionalList:
'''一个封装了一些附加魔术方法比如 head, tail, init, last, drop, 和take的列表类。
'''

def __init__(self, values=None):
if values is None:
    self.values = []
else:
    self.values = values

def __len__(self):
    return len(self.values)

def __getitem__(self, key):
    #如果键的类型或者值无效，列表值将会抛出错误
    return self.values[key]

def __setitem__(self, key, value):
    self.values[key] = value

def __delitem__(self, key):
    del self.values[key]

def __iter__(self):
    return iter(self.values)

def __reversed__(self):
    return reversed(self.values)

def append(self, value):
    self.values.append(value)
def head(self):
    return self.values[0]
def tail(self):
    return self.values[1:]
def init(self):
    #返回一直到末尾的所有元素
    return self.values[:-1]
def last(self):
    #返回末尾元素
    return self.values[-1]
def drop(self, n):
    #返回除前n个外的所有元素
    return self.values[n:]
def take(self, n):
    #返回前n个元素
    return self.values[:n]
```

比较特别的是 `__contains__`，你可以不定义它然后使用 `in` 或者 `not in`，因为 Python 会迭代这个序列并且找到找到合适值时返回 `True`。

### 反射

可以使用魔术方法控制 `isinstance()` 和 `issubclass()` 方法

+ `__instancecheck__(self ,instance)`: 检查一个实例是不是你定义的类的实例。
+ `__subclasscheck__(self, subclass)`: 检查一个类是不是你定义的类的子类。

这些方法用的很少，但当你想要用时，会感激他的存在。

### 可调用的对象

Python 有一个模式方法可以让类的实现表现的像函数一样可以被调用，`__call__` 这让 Python 编程变得甜美无比。

一个简单的例子
```python
class Position(self):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __call__(x, y):
        self.x, self.y = x, y
```

这美的让你不敢相信。使用函数调用的方式来修改实例属性。

### 会话管理

使用 `__enter__` 和 `__exit__` 来定义 `with` 会话管理，这对定义好的日常行为和清洁工作很有帮助。

```python
class Closer(object):
    def __init__(self, obj):
        self.obj = obj
    def __enter__(self):
        return self.obj
    def __exit__(self, exception_type, exception_val, trace):
        try:
            self.obj.colse()
        except AttributeError:
            print('Not closable.')
            return True
```

下面是一些使用 Closer 的例子
```python
from ftplib import FTP
with Closer(FTP('ftp.somesite.com')) as conn:
    conn.dir()

with Closer(int(5)) as i:
    i += 1
```

### 储存你的对象

Pickle 用来序列化 Python 数据结构，在你要暂存一个对象的时候非常有用。

这种时候你可以把他写进一个文件中，但这样不安全，并且容易被崩溃。

让我们用 Pickle 代替

```python
import pickle
# 写入
data = {'foo': [1, 2, 3],
        'bar': ('Hello', 'world!'),
        'baz': True}
jar = open('data.pkl', 'wb')
pickle.dump(data, jar)
jar.close()

# 读取
pkl_file = open('data.pkl', 'rb')
data = pickle.load(pkl_file)
pkl_file.closer()
```

pickle 并不是很完美，其比较容易损坏，但是他比文件稍微安全一点。

Magic Methods

![avator](https://raw.githubusercontent.com/1oser5/CS-Notes/master/pic/python-magic-method.jpg)