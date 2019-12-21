# 作用

从标准输入读取单行数据，当你重定向时，可以读取文件中的一行。

## 语法
```
read [-ers] [-a name] [-d delim] [-i text] [-n nchars] [-N nchars] [-p prompt] [-t timeout] [-u fd] [name...]
```

## 参数
+ -p: 指定一个提示。
+ -t: 等待 read 命输入计秒数，当超时会返回一个非零的退出状态。
+ -s: 将输入的命令不显示在终端上
+ -e: 自动补全
+ -n: 限制输入字符


## Usage

1.简单读取
```shell
$ echo "输入网站名"
$ read website
$ echo "你输入的网站是 $website"
# 输出
# 输入网站名: 
# www.runoob.com
# 你输入的网站名是 www.runoob.com
```

2.-p,允许给出提示
```shell
$ read -p "输入网站名" website
$ echo "你输入的网站名是 $website"
```

3.-t,指定输入时间，超时返回非零状态码
```
read -t 5
```

4.-s，让输入数据不出现在目录终端
```
read -s -p "输入你的密码"
```