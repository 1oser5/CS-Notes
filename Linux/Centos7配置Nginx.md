## 原因 
之前配置的内网 Nginx 由于一些原因，需要迁移到外网服务器上，公司有一台阿里云服务器，支持外网访问，因此就在该服务器上搭建一个新的 Nginx 文件用来下载打包文件。

### 秘钥配置

首先研究阿里云的连接方式，直接使用 `pem` 文件实现无秘连接

使用
```
ssh -i 秘钥路径 用户名@ip地址
```
进行连接


### Nginx下载

服务器上是有 `yum` 的，直接使用 `yum install nginx`


## 启动

使用 `systemctl start nginx` 运行，居然就报错了
```
 * Starting nginx nginx
nginx: [emerg] bind() to [::]:80 failed (98: Address already in use)
nginx: [emerg] bind() to [::]:80 failed (98: Address already in use)
nginx: [emerg] bind() to [::]:80 failed (98: Address already in use)
nginx: [emerg] bind() to [::]:80 failed (98: Address already in use)
nginx: [emerg] bind() to [::]:80 failed (98: Address already in use)
nginx: [emerg] still could not bind()
```

可以使用 `whereis nginx` 查看 nginx 下载位置

查找了一下原因，是因为 `nginx conf` 的设置有错误，好呆！

`nginx conf` 文件中有如下俩句
```
listen 80;
listen [::]:80 default_server;
```
随便注释掉一句即可（因为你同时监听了相同的2个端口），`Stack Overflow`上有这样回答的，加上一个 `ipv6only` 参数
```
listen 80;
listen [::]:80 ipv6only=on default_server;
```
但是我还是报错了，所以直接注释了下面一句，服务器可以正常运行。


## 端口号
但是使用 ip 地址加上端口号连接还是无法访问，检查了相关端口是否开启
```
netstat -nupl (UDP类型的端口)
netstat -ntpl (TCP类型的端口)
```
明明是开启的，查了一下发现阿里云可以需要手动添加规则，把我设置的 `8998` 端口加上去就可以访问了，当然需要查看目录s功能的话，需要把配置里的 `autoindex` 参数加上
```
location / {
            root   （当前静态文件的路径）;
            index  index.html index.htm;
            autoindex on;
        }
```

## Centos 常用命令
+ centOS 7 启动一个服务：systemctl start 服务名.service
+ 关闭一个服务：systemctl stop 服务名.service
+ 重启一个服务：systemctl restart 服务名.service

+ 显示一个服务的状态：systemctl status 服务名.service
+ 在开机时启用一个服务：systemctl enable 服务名.service
+ 在开机时禁用一个服务：systemctl disable 服务名.service

