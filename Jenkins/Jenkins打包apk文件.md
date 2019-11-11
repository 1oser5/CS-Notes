## 环境需求

+ java 环境
+ Gradle 环境
+ Android SDK

Gradle 是一个构建工具，其可以帮助更快的构建软件。简单来说，就是帮你打包的。


## Gradle配置

Gradle 在任何操作平台上都是基于 Java JDK or JRE 8以上。

首先先确认 java 版本
```
java -version
```

到 Gradle 官网，找到下载列表

![avator](../pic/download-gradle.png)

点击上图的 complete，进入下载页面，复制下载链接。

![avator](../pic/download-gradle-link.png)

在 linux 命令行中输入
```
wget https://services.gradle.org/distributions/gradle-6.0-all.zip
```

wget 后为之前复制的下载链接。

下载完之后新建一个文件夹用来解压 gradle.zip
```
mkdir /opt/gradle
```

在制定文件夹解压 gradle-6.0
```
unzip -d /opt/gradle gradle-6.0.bin.zip
```

bin 结尾的文件是二进制的版本的，我下载的是 complete 版本，所以压缩文件名称不一样，需要注意。

查看 gradle 是否正常解压
```
ls /opt/gradle/gradle-6.0
```

最后需要设置系统路径

```
export PATH=$PATH:/opt/gradle/gradle-6.0/bin
```


输入 
```
gradle -v
```

查看是否安装成功。


在 gradle 配置完成后，首先不引入 Jenkins 部分，先使用 gradle 进行打包。

看到公司给我的安卓项目，脑壳有点乱，这不太像是用 as 开发的文件目录啊。

晕了，原来是用 vue 开发的。

原来公司是用 vue 加 HBuilder 打包的，哇！！


之前的 HBuilder 命令行方案应该是不行的，好像没推出这个东西，只能使用 cordova。

首先 `npm install` 所有的包，然后在 `npm run build`，发现 `node.js` 版本不够。

目前公司 linux 服务器上的 node 版本为 6+。

### 更新node

首先清除 npm cache
```
sudo npm cache clean -f
```
安装 n 模块
```
sudo npm install -g n
```
安装最新稳定版本
```
sudo n stable
```
查看 node 版本
```
node -v
```

我虽然更新成功了，但是 `node -v` 显示的还是之前那个版本。

可能是下载了两个 node，直接删除吧
```
yum remove nodejs npm -y
```


1、下载源码，你需要在https://nodejs.org/en/download/下载最新的Nodejs版本，本文以v0.10.24为例:

cd /usr/local/src/
wget http://nodejs.org/dist/v0.10.24/node-v0.10.24.tar.gz
2、解压源码

tar zxvf node-v0.10.24.tar.gz
3、 编译安装

cd node-v0.10.24
./configure --prefix=/usr/local/node/0.10.24
make
make install
4、 配置NODE_HOME，进入profile编辑环境变量

vim /etc/profile
设置 nodejs 环境变量，在 export PATH USER LOGNAME MAIL HOSTNAME HISTSIZE HISTCONTROL 一行的上面添加如下内容:

#set for nodejs
export NODE_HOME=/usr/local/node/0.10.24
export PATH=$NODE_HOME/bin:$PATH
:wq保存并退出，编译/etc/profile 使配置生效

source /etc/profile
验证是否安装配置成功

node -v
输出 v0.10.24 表示配置成功

npm模块安装路径

/usr/local/node/0.10.24/lib/node_modules/

确实是下载好了 npm 和 node，但是发现没法 `sudo npm `
安装。

查了一下 npm 文件 应该放在 `/usr/local/bin/npm` 下，不然就会报错

只能建立软连接解决，不然就要重下了。
```
sudo ln -s /usr/local/node/0.10.24/bin/npm /usr/local/bin/npm
```

我真的服了，这东西是真的不好用。最终我使用 nvm 下的真的快，nvm天下第一。

1.安装并下载 nvm 脚本
```
curl https://raw.githubusercontent.com/creationix/nvm/v0.13.1/install.sh | bash

source ~/.bash_profile
```
列出所有的版本
```
nvm list-remote
```
安装对应版本
```
nvm install v0.10.30
```
查看已安装版本
```
nvm list
```
切换版本
```
nvm use v0.10.30
```
设为默认版本
```
nvm alias default v0.10.30
```