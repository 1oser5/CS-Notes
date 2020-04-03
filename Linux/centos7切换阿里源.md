## 切换 yum 源

因为我国国情，使用原生的源下载速度慢，切换为国内阿里源


## 1.下载对应源
```
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
```

## 2.清空 yum 缓存
```
yum clean all
```

## 3.执行 yum makecache

```
yum makecache
```
