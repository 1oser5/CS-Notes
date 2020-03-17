## 原因

今天在写自动导表模块的时候，发现 linux 之前用 yum 装的版本实在是太低了，影响了自动化脚本操作，我重新安装了之后，发现 GitPython 无法找到 环境变量中的 Git 路径了。但是我不通过 jenkins 运行脚本，是可以正常运行的。应该是jenkins 环境变量的问题


## 过程

我输出 jenkins 终端的 PATH ，确实么有对应的 Git 路径，首先打开 `vim /etc/profile`，该文件一般是系统级别的配置文件，对所有用户都生效，然后手动把Git的路径加入，在文件末尾加入`export PATH=$PATH:/usr/local/git/bin`，然后保存，重新加载配置 `source /etc/profile`。然后我运行 jenkins 脚本还是不行，jenkins输出的 PATH 仍然没有 Git。之后我在运行脚本前，先运行 `vim /etc/profile` 则可以运行。但我嫌每次都要配置一下 环境变量太麻烦了，不然每次写脚本都得 `vim /etc/profile && python3 对应脚本`，因此我们把重载环境变量直接写在 jenkins 配置中，打开 jenkins 配置文件 `vim /etc/sysconfig/jenkins` ，在末尾加上 `source /etc/profile` 重启 jenkins 服务即可。

