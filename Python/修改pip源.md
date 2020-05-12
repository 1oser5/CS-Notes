## 原因

国外的 pip 下载慢，又经常出现超时断开情况，使用切换到国内 pip 源

## 过程
切换为清华大学开源软件镜像站 `https://mirrors.tuna.tsinghua.edu.cn/help/pypi/`

pypi 镜像使用帮助
pypi 镜像每 5 分钟同步一次。

临时使用
`
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
`
注意，simple 不能少, 是 https 而不是 http

设为默认
升级 pip 到最新的版本 (>=10.0.0) 后进行配置：
```
pip3 install pip -U
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
如果您到 pip 默认源的网络连接较差，临时使用本镜像站来升级 pip：
`
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
`