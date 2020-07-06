mac 可以直接使用 Microsoft Remote Desktop for Mac 来远程控制 Windows 界面。

![avator](https://raw.githubusercontent.com/1oser5/CS-Notes/master/pic/win-server-conn.png)

打开命令行输入
```
java -version
```
查看是否拥有 java 环境

windows 服务器方便就方便在有 GUI，直接打开浏览器去下载 java。

需要注意的是 Jenkins 对于 Java 的版本有一定要求。

百度是可以正常使用，但是发现 oracle 官网打不开，问题如下：

![avator](https://raw.githubusercontent.com/1oser5/CS-Notes/master/pic/win-server-unable-open-page.png)


1.搜索输入 运行，然后输入 inetcpl.cpl

2.打开 internet 设置

3.点击 高级

4.勾选“使用 TLS 1.1”和“使用 TLS 1.2”

5.刷新网页即可


确定 windows 服务器是几位的

在 cmd 中输入
```
systeminfo
```
![avator](https://raw.githubusercontent.com/1oser5/CS-Notes/master/pic/win-server-check-type.png)

去官网下载相应的下载包

然后直接打开，安装完成之后 Jenkins 将自动打开一个网页，复制相应密钥路径，在搜索中输入并打开，复制相应的字符串，登录成功后选择新手入门插件。

安装相应插件之后，在补充安装一个 Blue Ocean 即可。

在使用 jenkins 运行 windows 脚本时，选择 windows batch command，而不是 shell。

记得在 Windows 的服务中，把jenkins 的用户修改为 管理员，这样才能正常的进行 Git 操作。