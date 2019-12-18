
## 需求
需要让打包出来的 ipa 直接能通过网页下载，需要这两个对象

1.ipa.plist

下载地址以及应用相关的配置

2.index.html

这是一个提供给用户的简单网页，点击之后就会跳转至 ipa.plist

## 配置

### ipa.plist

ipa.plist 结构应该像这样：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>items</key>
    <array>
        <dict>
            <key>assets</key>
            <array>
                <dict>
                    <key>kind</key>
                    <string>software-package</string>
                    <key>url</key>
                    <string>请填上你的ipa下载地址(比如:http://www.example.com/app.ipa)</string>
                </dict>
            </array>
            <key>metadata</key>
            <dict>
                <key>bundle-identifier</key>
                <string>请填上开发者相关信息</string>
                <key>bundle-version</key>
                <string>请填上软件版本号</string>
                <key>kind</key>
                <string>software</string>
                <key>title</key>
                <string>请填上软件名称</string>
            </dict>
        </dict>
    </array>
</dict>
</plist>
```

除了 url 信息之外，其余的信息都可以通过打包出来的 ipa 包解压之后，找到 info.plist 进行配置。

## index.html

提供一个下载链接

```html
<!doctype html>
<html>
<head>
	<meta content="utf-8">
	<title>标题</title>
</head>
<body>
      <div align="center" ><h1 style="font-size:20pt">xxx软件下载<h1/></div>	
      <div align="center" ><h1 style="font-size:20pt">如果点击无法下载安装，请复制超链接到Safari浏览器中打开<h1/></div>
      <div align="center" ><h1 style="font-size:20pt">
      <a title="iPhone" href="itms-services://?action=download-manifest&url=https://www.example.com/ipa.plist">点击下载</a><h1/></div>
</body>
</html>
```

`itms-services://?action=download-manifest&url=https://www.example.com/ipa.plist` 部分的 url 就是之前配置的 ipa.list 位置。

> ipa.list 必须放在支持 https 的服务器上，并且可访问
