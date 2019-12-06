## 作用

用于复制文件或者目录

## 语法

```
cp [options] source dist
```
or
```
cp [options] source.. directory
```

## 参数

+ **-a**: 通常在复制文件夹时使用，保留链接，文件属性的同时复制目录下所有内容，和使用参数 `dpR` 一样效果。
+ **-d**: 保留文件链接，这里指的链接是 windows 的快捷方式。
+ **-f**: 如果有同名文件或文件夹不询问直接删除。
+ **-i**: 和 `-f` 相反，有同名文件进行询问。
+ **-p**: 复制文件内容同时，复制修改时间和访问权限。
+ **-r**: 若目标是文件夹，递归复制，用户复制文件夹时必须要该参数。
+ **-l**: 不复制，只是建立链接。


## Usage

1.使用指令"cp"将当前目录"test/"下的所有文件复制到新目录"newtest"下，输入如下命令：
```
$ cp -r test/ newtest
```