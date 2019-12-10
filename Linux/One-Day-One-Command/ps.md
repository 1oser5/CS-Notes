## 作用
显示当前进程（process）的状态。

## 语法

```
ps [options] [--help]
```

## 参数

+ -A: 显示所有进程。
+ -w: 加宽以显示进程详细。
+ -au: 显示进程详细信息。
+ -aux: 显示包含其他用户的所有进程，输出格式为 `USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND`。

## Usage

1.显示所有进程
```
$ ps -A 显示进程信息
PID TTY     TIME CMD
  1 ?    00:00:02 init
  2 ?    00:00:00 kthreadd
  3 ?    00:00:00 migration/0
  4 ?    00:00:00 ksoftirqd/0
```

2.显示指定用户信息

```
$ ps -u root //显示root进程用户信息
 PID TTY     TIME CMD
  1 ?    00:00:02 init
  2 ?    00:00:00 kthreadd
  3 ?    00:00:00 migration/0
  4 ?    00:00:00 ksoftirqd/0
  5 ?    00:00:00 watchdog/0
  6 ?    00:00:00 events/0
  7 ?    00:00:00 cpuset
```

3.显示所有进程信息，连同命令行
```
$ ps -ef //显示所有命令，连带命令行
UID    PID PPID C STIME TTY     TIME CMD
root     1   0 0 10:22 ?    00:00:02 /sbin/init
root     2   0 0 10:22 ?    00:00:00 [kthreadd]
root     3   2 0 10:22 ?    00:00:00 [migration/0]
root     4   2 0 10:22 ?    00:00:00 [ksoftirqd/0]
root     5   2 0 10:22 ?    00:00:00 [watchdog/0]
root     6   2 0 10:22 ?    /usr/lib/NetworkManager
```