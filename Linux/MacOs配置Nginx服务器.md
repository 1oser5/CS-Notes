## 原因
由于公司的打包业务需求，需要打包完成之后提供一个下载地址链接，使得测试可以方便的通过链接进行相应版本的软件下载。

选择使用 Nginx 服务器
## 配置环境

### nginx

选用 nginx 作为 web 服务器

使用 homebrew 下载 nginx
```
brew install nginx
```
在下载完之后会告诉你相关的设置位置
```python
# 文件根目录
Docroot is: /usr/local/var/www
# 默认端口号，以及相关配置文件
The default port has been set in /usr/local/etc/nginx/nginx.conf to 8080 so that
nginx can run without sudo.
## 服务器文件目录
nginx will load all files in /usr/local/etc/nginx/servers/.
## 运行并且开机运行
To have launchd start nginx now and restart at login:
  brew services start nginx
# 不需要后台运行，直接使用 nginx
Or, if you dont want/need a background service you can just run:
  nginx
```

## 设置

1.设置根目录
```
$ cd /usr/local/etc/nginx/
```
2.打开
```
$ vim nginx.conf
```
3.可以看到以下内容
```python
  server {
        listen       8080;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            #此处改为你放文件的路径
            root   /Users/zhyl/Desktop/package;
            index  index.html index.htm;
        }
```
4.重启
```
nginx -s reload
```

在 url 后输入对应文件名即可
```
10.0.30.6/some.json
```


打开目录索引
```
autoindex on;
```