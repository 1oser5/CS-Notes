## 原因

公司有一个 RN 开发的移动应用，需要本地测试，希望有一套完整的 ipa 包发布程序，将中间过程都隐藏起来，之前刚来公司的时候配置过一次，这次看来上次配置成功属实侥幸。但是说实话，苹果的东西，真的坑很多，很多限制在里面，研究了很久最后才把完整的流程搞清楚。

首先我们想要的一个自动化流程应该是这样的：

+ 版本更新（svn or git）
+ npm 更新
+ rn-ios打包
+ pod install
+ xcodebuild 构筑打包 ipa
+ 将对应二维码传输到外网服务器（为了钉钉能够识别）
+ 将对应的 ipa 文件传输到 nginx 服务器（一定要是 https）
+ 钉钉发送二维码，可进行扫码下载

## 过程


基本上问题都集中在 xcode 之后，首先来了解一下 xcode 打包需要手动配置好的东西

+ profile（最好建议不同的应用使用不同证书）
+ exportoptions.plist(ipa导出配置)
+ manifest.plist(扫码下载配置)

证书的话，去苹果开发者官网，自己生成，一个Provisioning Profile文件包含了上述的内容:Certificate, App ID, Devices。这里需要注意对应关系。

### profile

在生成好对应的 Provisioning Profile 之后，将其下载下来，在 xcode 中打开对应项目，在 选择账户部分，将 bundle identifier 选择为 Provisioning Profile 中对应的 APPLE ID ，再在 Provisioning Profile 中导入之前下载的 Provisioning Profile 即可。

### exportoptions.plist

我选择的是手动 archive 之后，获得打包出来的 exportoptions.plist 。在 xcode 中选择 product 然后 archive ，然后打包方式选择 Ad-Hoc，之后将对应的 profile 选择对就行。打包完有一个文件夹，里面包含我们想要的 exportoptions.plist

### manifest.plist

这个可用手动打包生成，但是需要配置图片 url，我就手动写了一个，需要注意的是对应的 url 键值对，要改成 ipa 的实际位置，**并且必须要是 https 服务器**。这是整个扫码下载的关键一步，其余的都安装不同项目配置好即可。


## 扫码下载

扫码下载主要是使用了苹果的 itms-services 服务，二维码里的文本信息其实就是 `itms-services://?action=download-manifest&url=.plist`
最后的 plist 就是你服务器上 plist的位置，这里必须要是 https 服务器。

然后苹果会去读取 plist 文件中的实际 ipa 位置，进行下载。


## 踩坑

### 1.扫码提示无法连接到 xxx.xxx.xxx.xxx

我先到网上直接搜索了这个问题，回答可以说是千奇百怪，而且情景都不完全一致。
我之后使用 爱思手机助手，连接对应设备，扫码下载失败后查看日志，发现了真实的报错 ` Error Domain=kCFErrorDomainCFNetwork Code=-1202 "(null)"` 查了一下是因为证书的问题，自签的证书， IOS 13 是可以直接识别的，但是 IOS 12 会报上述错误。我将 nginx 的 crt 证书也挂载到了 服务器上，在扫码之前，先下载对应证书，然后到 对应设备上的 设置 中，安装描述文件，然后再到 描述文件中手动进行信任就行，再次下载就行。




