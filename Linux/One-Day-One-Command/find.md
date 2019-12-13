## 作用

用来在指定目录下查找文件，任何在参数之前的字符串都被认为是查找对象，如果不设定任何参数，则在当前目录下查找，并将找到的子目录和文件全部显示。


## 语法
```
find path -option [-print] [-exec -ok command] {} \;
```

## 参数

find 是使用如下规则判断是 path 还是 expression，在命令行第一个 `-(),!` 之前的是path，之后的为 expression。如果 path 为空字符，则默认为当前目录，如果 expression 为空字符则使用 `-print`。

+ -mount,-xdev: 只查找同一文件系统下的文件。
+ -nmin: `n` 分钟之内读取过的文件。
+ -anewer file: 比目标 `file` 更晚更新的文件。
+ -ntime: `n` 天之内被读取的文件。
+ -cmin: `n` 分钟内被修改过的文件。
+ -cnewer file: 比目标 `file` 更新的文件。
+ -ctime: `n` 天之内被修改的文件。
+ -empty: 空文件夹。
+ -gid n or -group name: gid 是 n 或者 group 为 name 的文件。
+ -ipath p,path p: 路径符合 p 的文件，ipath 忽略大小写。
+ -iname n, name n: 名称符合 n 的文件，iname 忽略大小写。
+ -pid n: process id 是 n 的文件。

## 实例

1.将当前目录及其子目录下的所有后缀名为 c 的文件列出来
```
$ find . -name "*.c"
```

2.将当前目录下其子目录中所有一般文件列出
```
$ find . -type f
```

3.查找/var/log目录中更改时间在7日以前的普通文件，并在删除之前询问它们
```
# find /var/log -type f -mtime +7 -ok rm {} \;
```
