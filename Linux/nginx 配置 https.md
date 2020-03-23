## 原因

之前在 mac 机器上配置过 nginx 的 https 服务，但是发现有些细节处理的有问题，导致后续有关证书问题出错。

## 过程

首先要进行证书自签，一键生成自签证书` sudo openssl req -x509 -nodes -days 36500 -newkey rsa:2048 -keyout /root/project/ssl/nginx.key -out /root/project/ssl/nginx.crt
`

会让你输入一些问题

```
Country Name (2 letter code) [AU]:CN

State or Province Name (full name) [Some-State]:Fu jian

Locality Name (eg, city) []:Xia men

Organization Name (eg, company) [Internet Widgits Pty Ltd]:lin

Organizational Unit Name (eg, section) []:qiezi

Common Name (e.g. server FQDN or YOUR name) []:www.qeizi666.cn

Email Address []:
```

上述中的 `Common Name` 很重要，输入你的想要配置证书的域名或者ip地址

然后将证书对应位置配置到 nginx 里即可。