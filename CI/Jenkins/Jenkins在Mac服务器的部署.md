公司的 Mac 打包机到了，想以后所有的打包任务都放在这台 Mac 上。

之前是否部署过 Jenkins 已经忘了，现在重新进行部署。

本来想通过 `homebrew` 下载，奈何国内网速实在是。。。。


只能去官网下载相应版本进行手动安装，安装完之后出现了会自动弹出一个网页，但是这里报错了

### 无法连接到服务器 localhost

意思是端口号被占用了，使用下面命令切换端口号
```
java -jar jenkins.war --ajp13Port=-1 --httpPort=8081
```
报错
```
Unable to access jarfile jenkins.war
```
添加了 `sudo` 命令还是一样报错

因为没有进入 Jenkins 的对应目录，原来我上次把 Jenkins 放在应用程序目录了。

切换端口之后可以正常使用了。


### 连接内网的每台电脑都需要进行登录么？

