## 作用
用来为文件或目录改名、或将文件或目录移入其他位置。

## 语法
```
mv [options] source dest
mv [options] source... directory
```

## 参数

+ -i: 若指定目录已有同名文件，则先询问是否覆盖旧文件
+ -f: 在 mv 操作要覆盖某已有的目标文件时不给任何提示

|命令格式|运行结果|
|-|-|
|mv 文件名 文件名|将源文件改为目标文件名|
|mv 文件名 目录名|将文件移动到目标目录|
|mv 目录名 目录名|目标目录已存在则将源目录移到目标目录；目标目录不存在则改名|
|mv 目录名 文件名| 出错|

## Usage

1.将文件 aaa 改为文件 bbb
```
$ mv aaa bbb
```

2.将 info 目录放入 logs 目录中。如果 logs 目录不存在，则该命令将 info 改为 logs。
```
$ mv info/ logs
```

3.将 /usr/student 下的所有文件和目录移到当前目录
```
$ mv /usr/student/* .
```