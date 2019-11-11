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

然后重新安装，推荐使用源码安装。

下载源码
```
wget http://nodejs.org/dist/v0.10.30/node-v0.10.30.tar.gz
```

解压源码
```
tar xzvf node-v* && cd node-v*
```

安装必要的编译软件
```
sudo yum install gcc gcc-c++
```

编译
```
./configure
make
sudo make install
```

查看版本 
```
node --version
```

由于安装位置不一样（可能是权限问题？），需要创建软连接
```
ln -s /usr/bin/node /usr/bin/node
ln -s /usr/bin/npm /usr/bin/npm
```
-s 之后是你安装的node位置

