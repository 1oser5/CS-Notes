## 作用
`cat` 命令用于连接文件并打印到标准输出设备上。


## 语法
```sh
cat [-AbennstTuv][--help][--version] fileName
```

## 参数

+ **-n 或 --number**: 由 1开始对所有输出的行数编号。
+ **-b 或 -number-nonblank**: 和 -n 相似，只不过对空白行不编号。
+ **-s 或 --squeeze-blank**: 当遇到有连续两行以上的空白行，就用一行代替。
+ **-v 或 --show-nonprinting**: 使用 `^` 和 `M-` 符号，除了 LFD 和 TAB 之外。
+ **-E 或 --show-ends**: 在每行结束处显示 $。
+ **-T 或 --show-tabs**: 将 TAB 字符显示未 `^|`。
+ **-A，--show-all**: 等价于 `-vET`。
+ **-e**: 等价于 `-vE` 选项。
+ **-t**: 等价于 `-vT` 选项。


## Usage

1.把 text1 的内容加到 text2 中。
```
cat -n text1 > text2
```
2.text1 和 text2 加上行号之后附加到 text3 中。
```
cat -b text1 text2 >> text3
```
3.清空 /etc/test.txt 文档内容。
```
cat /dev/null > /etc/test.txt
```
