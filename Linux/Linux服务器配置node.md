## Node
到node官网下载选择下载链接
```
wget https://nodejs.org/dist/v12.13.1/node-v12.13.1-linux-x64.tar.xz
```

Linux 解压 `tar.xz` 文件
```
tar -xvJf node-v8.11.1-linux-x64.tar.xz
```

解压到用户默认目录之后，开始配置环境

nvm方式安装

curl:
```
$ curl https://raw.github.com/creationix/nvm/master/install.sh | sh
```
wget：
```
$ wget -qO- https://raw.github.com/creationix/nvm/master/install.sh | sh
```

## git

下载 Git
```
yum install git-core
```
配置自己的用户名和密码
```
$ git config --global user.name "humingx"
$ git config --global user.email "humingx@yeah.net"

```
生成密钥
```
$ ssh-keygen -t rsa -C "humingx@yeah.net"
```

查看本地公钥

```
vim /root/.ssh/id_rsa.pub
```

将本地公钥复制到 GitHub 的 SSH key，就可以实现本地下载了。