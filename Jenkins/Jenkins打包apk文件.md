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