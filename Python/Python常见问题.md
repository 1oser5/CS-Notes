# 目录
+ (1. if \__name__ == "main" 做了什么)[1.if \__name__ == "main" 做了什么]
+ (2.os.system('cd')问题)[2.os.system('cd')问题]


## 1.if \__name__ == "\__main__" 做了什么

问题来源：stackoverflow 高分 Python 问题

链接：https://stackoverflow.com/questions/419163/what-does-if-name-main-do



## 2.os.system('cd')问题

今天在公司写自动化打包脚本的时候发现使用`os.system('cd xxx')`命令进行目录切换，十分好奇，去 Google 了以下原由。

原来和 Python 中 os.system 的实现机制有关。
> Execute the command (a string) in a subshell. This is implemented by calling the Standard C function system(), and has the same limitations.

os.system 实际上运行了一个子进程，是通过调用 C 标准库中的 system 来实现的，并且具有相同的限制。

由于是子进程，那么自然而然无法影响父进程的环境变量。

解决的办法有两种：

1.是使用os提供的`os.chdir(‘hello’)`

2, 是使用复合语句或者多个语句

`os.system(‘cd hello && ls’)`
或者 `os.system(‘cd hello’;’ls’)`

同时也可以使用 `subprocess` 模块

存疑。