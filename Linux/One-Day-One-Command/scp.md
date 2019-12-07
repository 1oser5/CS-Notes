## 作用
scp 是用来传输文件和目录的命令。
scp 的全称是 scoure copy ，它是 linux 基于 ssh 登录的远程文件传输命令。
rcp 是非加密的，scp是 rcp 的加强版。


## 语法
```
scp [-1246BCpqrv] [-c cipher] [-F ssh_config] [-i identity_file]
[-l limit] [-o ssh_option] [-P port] [-S program]
[[user@]host1:]file1 [...] [[user@]host2:]file2
```
简易语法
```
scp [可选参数] file_source file_target
```
## 参数
+ -1: 强制使用 ssh1 加密
+ -2: 强制使用 ssh2 加密
+ -4: 强制使用 IPv4 寻址。
+ -6: 强制使用 IPv6 寻址。
+ -B: 使用批处理模式。
+ -C: 允许压缩。
+ -q: 不显示传输过程。
+ -p: 保留文件的访问时间，修改时间和访问权限。
+ -r: 递归调用。
+ -v: 详细输出。
+ -C cipher: 使用 cipher 方式加密。
+ -F ssh_config: 指定 ssh 配置文件。
+ -i identity-file: 指定的加密文件。
+ -l limit: 限制带宽，以 Kbit/s 为单位。
+ -P prot: 指定数据传输的端口号。
+ -S program: 指定加密传输的程序，必须支持 ssh（1）

## Usage

1.本地文件复制到远程
```python
# 指定用户传输指定文件到指定文件夹，文件名为 local_file
scp local_file remote_user@remote_ip:remote_dir
# 指定用户传输指定文件到指定文件
scp local_file remote_user@remote_ip:remote_file
# 不指定用户，需要后续输入
scp local_file remote_ip:remote_file
```

2.本地文件夹复制到远程
```python
scp -r local_folder remote_username@remote_ip:remote_folder 
或者 
scp -r local_folder remote_ip:remote_folder 
```
3.从远程复制到本地
```python
# 参数位置调换即可
# 文件
scp remote_user@remote_ip:remote_file local_file
#文件夹
scp -r remote_user@remote_ip:remote_folder local_folder
```