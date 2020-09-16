# 远程管理神器shuttle

## 介绍

我之前一直使用的是 Mac 版的 Royal TSX 作为远程管理工具，用户体验也不错。但是在 Mac重装之后，又开始研究新的软件，发现一款叫 Shuttle 的软件十分牛逼。

shuttle 官网 `http://fitztrev.github.io/shuttle/`

官方给出的定义是 `A simple shortcut menu for macOS`，意味着除了处理远程连接之外，它还有快捷键的功能。


## 配置

所有的服务都在 `.shuttle.json` 配置中，默认的配置长这样
```json
{
    "_comments": [
    "Valid terminals include: 'Terminal.app' or 'iTerm'",
    "In the editor value change 'default' to 'nano', 'vi', or another terminal based editor.",
    "Hosts will also be read from your ~/.ssh/config or /etc/ssh_config file, if available",
    "For more information on how to configure, please see http://fitztrev.github.io/shuttle/"
  ],
    "editor": "default",
    "launch_at_login": true,
    "terminal": "iTerm",
    "iTerm_version": "nightly",
    "default_theme": "Homebrew",
    "open_in": "new",
    "show_ssh_config_hosts": false,
    "ssh_config_ignore_hosts": [],
    "ssh_config_ignore_keywords": [],
    "hosts": [
        {
            "cmd": "ps aux | grep defaults",
            "name": "Grep - Opens in Default-window-theme-title"
    },
        {
            "Spouses Servers": [
                {
                    "cmd": "echo '—->WARNING! Running commands<-- Are you sure? y/n'; read sure; if [ $sure == y ]; then echo running command && ps aux | grep [a]pple; else echo save to history and show... && history -s 'ps aux | grep [a]pple' && osascript -e 'tell application \"System Events\" to keystroke \"p\" using {control down}'; fi",
                    "inTerminal": "current",
                    "name": "Logs - Opens in the current active terminal window"
        },
                {
                    "Jane’s Servers": [
                        {
                            "cmd": "ssh username@blog2.example.com",
                            "inTerminal": "tab",
                            "name": "SSH blog - Opens in Tab of active window",
                            "theme": "basic",
                            "title": "title of tab"
            },
                        {
                            "cmd": "ssh username@shop1.example.com",
                            "inTerminal": "new",
                            "name": "SSH Shop - Opens in New Window",
                            "theme": "basic",
                            "title": "title of new window"
            }
          ]
        }
      ]
    },
  ]
}
```

`comments` 里提到了如果是 host 对象下的命令，会自动读取 `~/.ssh/config` 和 `/etc/ssh_config` 文件配置，另外 shuttle 目前支持的终端只有 `'Terminal.app' or 'iTerm'`

### 配置说明

1. editor：配置文件编辑器，我用的是 vscode
2. launch_at_login: 开机启动，true or false
3. iTerm_version: 该选择只针对于终端为 `iTerm` 的用户，选择 iTerm 的版本
4. default_theme: 默认主题
5. open_in: 打开方式，有 `tab` 和 `new` 两个可选，新建一个tab或者打开一个新窗口
6. show_ssh_config_hosts: 是否解析 config 文件，默认为 true
7. ssh_config_ignore_keywords: 忽略的关键字

命令格式说明
```json
{
    "菜单名称": [
        {
            "cmd": "需要执行的 ssh 命令",
            "inTerminal": "命令执行的窗口模式：new/tab/current",
            "name": "子菜单名",
            "theme": "终端主题：basic",
            "title": "新窗口/新标签页标题，缺失时使用 name 作为标题",
        }
    ]
```


示例
```json
"hosts": [
    {
      "cmd": "ssh root@192.168.0.100 -p 4000",
      "inTerminal": "tab",
      "name": "SSH - root用户",
      "theme": "basic",
      "title": "Blue"
    },
    {
      "cmd": "ssh root@192.168.0.200 -p 4000",
      "inTerminal": "tab",
      "name": "SSH - git用户",
      "theme": "basic",
      "title": "Blue"
    }
    ]
```

## 快捷键

shuttle 同时可以挂载常用一些常用的命令

```json
"hosts": [
    {
      "cmd": "ps aux | grep java",
      "name": "查看java进程",
    }
    ]
```



## 扩展用法

在使用 shuttle 进行远程连接时，由于只是在命令行运行 `ssh` 命令，`ssh` 命令没有提供输入密码的快捷方式，所有导致每次`ssh`连接都需要输入密码，非常麻烦。

可以提供运行 sh 脚本来实现远程连接，模拟人工输入

### 文件路径

要注意文件路径的问题，`.shuttle.json` 位于 MacOS 中的 `~` 目录，即用户目录，同时终端的默认目录也在此，所以提供的对应脚本也应该在 `~` 目录下。

脚本内容

```shell
#!/usr/bin/expect

set timeout 30
spawn ssh -p [lindex $argv 0] [lindex $argv 1]
expect {
"(yes/no)?"
{send "yes\n";exp_continue}
"Password:"
{send "[lindex $argv 2]\n"}
" password:"
{send "[lindex $argv 2]\n"}
}
interact
```

### 文件权限

要将文件提高到可执行和访问权限 `chmod 777 xxx.sh`


使用实例

```json
"NOISE":[
            {
            "cmd": "./xxx.sh 22 root@xx.xx.xx.xx 你的密码",
            "inTerminal": "tab",
            "name": "密码连接",
            "title": "SSH"
            }
```


这样就可以实现不用每次输入密码进行远程连接