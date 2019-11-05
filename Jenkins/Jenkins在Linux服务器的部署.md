今天下午问导师要了公司 Liunx服务器的地址，想尝试使用 Jenkins 配合 GitHub 实现一个源代码库更新时，Jenkins 自动进行更新并发送邮件提示功能。

公司系统版本：
CentOS 7.6.1810

官网配置链接
https://pkg.jenkins.io/redhat-stable/

## 服务器环境配置
首先在服务器进行环境配置

需要使用以上版本库需要以下命令
```
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo

sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
```
1.java环境

```shell
# 查看JDK版本：
java -version
```

直接使用 yum 安装

```
yum install jenkins
```

发现 leader 给的部署 root 账号，只是普通账号。

只能 

``` 
sudo yum install jenkins
```


## 切换 yum 下载源

由于 yum 下载某些源并非国内的，比如上面的 jenkins，50MB的东西居然要安装20多分钟，这也太难顶了。

果断切换成国内的镜像源，目前国内的镜像源有俩家比较不错的，网易和阿里云。



1.首先备份系统自带yum源配置文件/etc/yum.repos.d/CentOS-Base.repo

如果不是 root 用户，下面所有命令加上 sudo 即可

```shell
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup

```


查看 Centos 版本

```shell
cat /etc/redhat-release
```

2.下载 对应的 aliyun 镜像版本


```shell
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

```

3、运行yum makecache生成缓存

```
yum makecache
```

4、这时候再更新系统就会看到以下mirrors.aliyun.com信息

```
yum -y update
```

## 启动 jenkins

启动 jenkins
```
service jenkins start
```
![avator](../pic/start-jenkins.png)

其默认端口为 8080，默认用户为 jenkins

可以在 /etc/sysconfig/jenkins 中修改 jenkins 配置

```
vi /etc/sysconfig/jenkins
```

返回 ok 之后，发现外网仍然无法访问改地址，但是使用 

```
curl localhost:8080
```

进行内部检查时是可以看到启动成功的。

也可以使用
```
netstat -tunlp
```
检查端口启动情况

可能是 8080 端口没有对外开放

添加对外的8080端口
```
firewall-cmd –zone=public –add-port=8080/tcp –permanent
```

修改后输入地址可以看到 jenkins 正常启动

![avator](../pic/join-jenkins.png)

基本部署完成。