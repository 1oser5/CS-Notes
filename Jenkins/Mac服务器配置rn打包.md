开发说一般项目分两种，react-native 和 Vue，所有两种打包都得研究。并且从目前来看 rn 的打包需求更急一些。

简单看了一下文档，发现 rn 对于移动端打包更加友好些。

## IPA 打包

首先全局安装下 rn 
```
npm install -g react-native
```

安装 CocoaPods
```
sudo gem install cocoapods
```

配置依赖
```
npm install
```

在 ios 文件夹下新建一个 bundle 文件夹

在 git 项目下输入
```
react-native bundle --entry-file index.ios.js --bundle-output ./ios/main.jsbundle --platform ios --assets-dest ./ios --dev false
```

相关参数含义：

+ --entry-file ：入口文件
+ --platform ：平台名称（ios 或 android）
+ --dev ：是否为开发模式，如果为 false 则会对 js 进行优化
+ --bundle-output ： 生成的 jsbundle 文件的名称
+ --assets-dest ：其他项目资源的存放位置

可以把打包命令集成到 ```package.json```

```
"scripts": {
    "start": "node node_modules/react-native/local-cli/cli.js start",
    "test": "jest",
    "bundle-ios": "node node_modules/react-native/local-cli/cli.js bundle --entry-file index.js --platform ios --dev false --bundle-output ./ios/bundle/index.jsbundle --assets-dest ./ios/bundle"
  },
```
之后就可以使用
```
npm run bundle-ios
```

这样资源都被打包到 `bundle` 文件夹中了。

在 `ios` 文件夹中输入 `pod install` 安装依赖

第一次安装真的慢，切换至国内镜像

新版的 CocoaPods 不允许用pod repo add直接添加master库了，但是依然可以：

```
cd ~/.cocoapods/repos 
pod repo remove master
git clone https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git master

```
最后进入自己的工程，在自己工程的podFile第一行加上：
```
source 'https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git'
```

但是还是安装的好慢啊，等待安装的时候研究了一下苹果的证书，真的是复杂

首先有这么三个东西：Certificates，Identifier，Devices，Profiles

**Certifiactes**

+ 就是证书，适用于把一台 Mac 电脑作为开发者电脑所必备的证明
+ 开发证书 Development Certificate 用于授权开发权限
+ 发布证书 Distribution Certificate 用于授权发布权限
+ 每台 Mac 需要导出本地证书才能生成开发证书和发布证书
+ **一个证书只对应一台电脑**


**Identifier**

+ Identifier 就是身份证，把一个应用标志为开发者应用
+ Apple ID 是每一个应用所特有的 ID，与应用内的 Bundle ID 所对应

**Devices**

+ Devices 是开发者设备列表
+ 只有注册了的开发者的设备才能进行真机调试
+ 使用 UDID 可以对设备进行注册

**Profiles**

+ 配置文件，用于把上述三项整合成一个文件，有个该文件才能真机测试
+ 生成的配置文件和 Certificate 一样有 开发 和 发布 两种
+ 现在 Xcode 可以自动生成该文件



## APK


生成一个签名密钥
```
$ keytool -genkeypair -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000
```