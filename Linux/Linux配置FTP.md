感觉每次使用 `scp` 命令传文件太麻烦了。索性配置一下 FTP 服务器。这样就方便多了。

## 安装
安装前先查看 ftp 是否已经安装，使用 yum 安装
```
$ vsftpd -v
$ yum -y install vsftpd
```
根据自己需求，修改 ftp 配置文件 `/etc/vsftpd/vsftpd.conf`

```shell
anonymous_enable=NO    # 是否允许匿名访问
local_enable=YES      # 是否允许使用本地帐户进行 FTP 用户登录验证
local_umask=022      # 设置本地用户默认文件掩码022
chroot_local_user=YES   # 是否限定用户在其主目录下（NO 表示允许切换到上级目录）
#chroot_list_enable=YES # 是否启用限制用户的名单（注释掉为禁用）
chroot_list_file=/etc/vsftpd/chroot_list # 用户列表文件（一行一个用户）
allow_writeable_chroot=YES # 如果启用了限定用户在其主目录下需要添加这个配置，解决报错 500 OOPS: vsftpd: refusing to run with writable root inside chroot()
xferlog_enable=YES     # 启用上传和下载的日志功能，默认开启。
use_localtime=YES     # 是否使用本地时(自行添加)
userlist_enable=YES 
```
## 启动
启动 ftp 服务
```
systemctl start vsftpd
```

## 用户管理

使用 `useradd` 命令添加一个用户
```
# 添加用户 ftpuser 
# -d：指定用户主目录 
# -s：指定用户所用的shell，此处为/sbin/nologin，表示不登录
$ useradd ftpuser -d /home/ftp1 -s /sbin/nologin
$ passwd ftpuser
```

删除用户
```
# -r：主目录及文件一并删除
$ userdel -r ftpuser 
```