# 作用
用来更变为其他使用者的身份，除了 root 外，都需要输入密码

# 语法
```
$ su [-fmp] [-c command] [-s shell] [--help] [--version] [-] [USER [ARG]]
```

## 参数

+ -f 或 -fast: 不启动读档
+ -m -p 或: 不改变环境变量
+ -c command: 使用 USER 账户运行 command 再切换回来
+ -s shell: 使用指定 shell 启动 USER 账户，预设值为 `/etc/passwd/` 内该用户的 shell
+ --help: 在线帮助
+ --version: 显示版本
+ --l: 以 USER 重新登录，工作环境切换为 USER 为主，使用不同的工作目录，如果不给出 USER，默认为 root
+ USER: 变更者账号
+ ARG: 传入 shell 参数

## Usage

1.变更账号为 root 并执行 ls 后退出
```
su -c ls root
```