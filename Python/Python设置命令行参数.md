想给自己写的打包脚本添加参数，实现动态打包的需求，所以研究了一下怎么调用脚本时添加参数。

有两种解决方案

+ getopt 库:更偏向于 C 模式编程，Python 很早就支持
+ argparse:更 Pythonic 的库，3.2版本之后才支持

## getopt

引入库
```
import getopt
```

可以通过 `sys.argv` 获得命令行参数，通过 `getopt` 库进行参数的判断。


```python
getopt.getopt(args, shortopts, longopts=[])
```
参数含义：

+ args : 指的是当前脚本接收的参数，它是一个列表，可以通过sys.argv获得
+ shortopts : 短参数 类似于 `python test.py -h`  输出帮助信息
+ longopts : 长参数 类似于 `python test.py -help`  输出帮助信息

短参数例如 `-h:` 后面有冒号表示接收参数值，长参数如 `-help=` 后面有等号表示接受参数值

通过 `getopt.GetoptError` 捕获非法参数

```python
inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"-g:-d:-p:-f:",[])
   except getopt.GetoptError:
      print('输出正确格式')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-g", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print('输入的文件为：', inputfile)
   print('输出的文件为：', outputfile)
```
`getopt.getopt` 返回值是有俩个列表组成的元组


## argparse
引入库
```
import argparse
```
### 定义 `ArgumentParser()` 类
```
parser = argparse.ArgumentParser()
```
之后的操作基本上都是对这个类进行修改。

### 添加参数
使用 `add_argument` 方法
```
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
```

参数定义：

+ name or flags : 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
+ actions : 当参数在命令行中出现时使用的动作基本类型，例如 'store_true' 或者 'store_false'。
+ nargs : 命令行应该被消耗的数目。
+ const : 参数默认值。
+ type : 参数应该被转换成的类型（这个很有意思，碾压了 getopt）
+ choices : 可选参数的容器。
+ required : 此命令行选项是否可以省略（仅选项可用）
+ help : 对此选项的简单描述
+ metavar : 在使用方法消息中使用的参数值示例。
+ dest : 被添加到 parse_args() 所返回对象上的属性名。

```python
parser = argparse.ArgumentParser()
#必选 git地址和 dir 位置
parser.add_argument("git_url",type =str,help="type git_url here")
parser.add_argument("dir_url",type =str,help="type dir_url here")
#可选互斥参数 项目类型
group = parser.add_mutually_exclusive_group()
group.add_argument("-vue", action="store_true", default='True', help="vue project, default")
group.add_argument("-rn", action="store_true", help="react-native")
#可选
parser.add_argument("-ipa", action="store_true", default='True', help="package to ipa, default")
parser.add_argument("-apk", action="store_true",  help="package to apk")
```

### 解析参数

通过 `parser.parse_args()` 解析参数
```
ArgumentParser.parse_args(args=None, namespace=None)
```
参数定义：

+ args : 解析的字符串列表，默认为 `sys.argv`
+ namespace : 存储属性的对象，默认为 `Namespace` 

可以通过 `vars(parser.parse_args())` 获得字典形式的参数列表。
