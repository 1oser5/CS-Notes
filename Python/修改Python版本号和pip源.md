## 起因
公司的 Linux 服务器上有好几个版本的 Python 和好几个版本的 pip。导致我使用 pip 安装都不知道装到哪一个 pip 依赖里了。需要进行一下系统的整理。

## 过程

首先我先排查的是 Python 模块搜索路径，保证模块搜索路径的正常

在命令行使用 `python3` 打开 `python shell`

```
import sys
sys.path
```

`sys path `就是 Python 模块搜索路径。该路径一般是一个数组。第一个空字符串表示的是当前文件目录。

上述的搜索模块可以通过 设置 PYTHONPATH 环境变量进行修改。

可以通过 `where python` 来确定 Python 的安装位置。


我发现对应的位置都是正确的，没什么问题。然后在我查看 pip 包安装的位置时，发现了猫腻，我发现我在命令行使用`python3`时，运行的是`python3.7`但是在`pip3 install`时，实际安装到的是`python3.6`的库中。

首先通过
```
pip show pip
```

可以查到默认使用的 pip 包。

果然这台服务器上的 pip3 默认的是 python3.6 版本。但是我无论是环境变量和执行都是 python3.7。

那么要查看一下 pip 的问题，首先要找到 pip 的配置文件。

pip 实际上也是 python 的一个库，所以理所当然的有自己的设置文件。

使用
```
python3 -m site -help
```

查看 `site.py` 的位置。

打开 `site.py` 文件，更改里面 `USER_BASE` 和`USER_SITE` 即可。其中 `USER_BASE` 和 `USER_SITE` 其实就是用户自定义的启用Python脚本和依赖安装包的基础路径。

我修改了 `USER_BASE` 为 python3.7 之后还是不行。

是不是修改的问题呢？

找到 pip 管理目录
```
/usr/local/bin
```

发现里面有好几个 pip。有一个 pip3.7 的难道才是 这台服务器 python3 的默认 pip 么。
```
pip3.7 install xxx
```
之后果然可以正常使用下载模块了。