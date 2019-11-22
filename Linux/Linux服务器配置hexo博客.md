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
$ vim /root/.ssh/id_rsa.pub
```

将本地公钥复制到 GitHub 的 SSH key，就可以实现本地下载了。

测试是否添加成功，可以在命令行输入一下命令：

```
$ ssh -T git@github.com
```


## hexo

安装 Hexo，命令行运行

```
$ npm install -g hexo-cli
```
初始化Hexo，在命令行依次运行
```
$ hexo init <folder>
$ cd <folder>
$ npm install
```

新建完成后，在路径下，会产生这些文件和文件夹：

```
.
├── _config.yml
├── package.json
├── scaffolds
├── source
|   ├── _drafts
|   └── _posts
└── themes
```

安装 `hexo-deployer-git`，命令行运行

```
$ npm install hexo-deployer-git --save
```
### 站点配置文件 
 
路径为 `<folder>\_config.yml`

### 站点配置文件 

​ 路径为 `<folder>\themes\<主题文件夹>\_config.yml`

### 启动服务器

```
$ hexo server
```
