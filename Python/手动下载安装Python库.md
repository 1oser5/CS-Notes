## 原因

由于本国国情，很多梯子都失效了，最近需要研究PyQt5，整个包有40M多，用pip下载需要一个多小时，而且还经常中途失败，在失败了几次之后真的崩溃了。我现在没有ss的梯子，但是我浏览器有插件可以科学上网，也就是说通过浏览器下载，速度是OK的。

## 方法

首先进入 PyPi 搜索 PyQt5，点击下面红框内的按钮

![avator](https://raw.githubusercontent.com/1oser5/CS-Notes/master/pic/pypi-download-file.jpg)
![avator](014fbc4d-d873-4a12-b160-867ddaed9807.jpg)


然后会看到几个不同平台的文件，注意这里有俩种文件模式， Wheel 模式是我们需要的下载的，文件名后面会有平台，记得看清楚自己是什么平台。最下面的 Source 则是源码。

![avator](https://raw.githubusercontent.com/1oser5/CS-Notes/master/pic/pypi-choose-plantom.jpg)

在下载完成之后，使用 pip 工具安装即可，pip本地安装的命令为
```
pip install <path>
```

接上本地路径即可。

