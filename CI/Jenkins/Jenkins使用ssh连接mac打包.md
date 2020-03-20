## 原因

这一礼拜一直在研究 ios 打包的机制，实在是踩了很多坑，十分值得记录一下，我发现所有的问题的出现都是有前应后果的，如果不清楚问题出在哪里，可以回溯一下步骤和之前有什么差异，然后通过差异得出结论。

## Mac的开发证书

### Certificates, Identifiers & Profiles

我相信每个人一开始看到这个是懵逼的，说真的苹果的开发环境真的是很严格，事实上上一次配置ios打包的时候我就没有特别去理解这个东西，默认使用的是自动配置的登录账号，但是这样是有问题的，接下来简单介绍一下，这三个东西是干么的。


### Certificates

Certificates 翻译过来就是证书，说白了就是给应用程序进行签名的。

其生成了一堆公钥和私钥，而代码签名(Code Signing)就是使用这种基于非对称秘钥的加密方式。用私钥进行签名，用公钥进行验证。

公钥和私钥都存储在 Mac 的 KeyChain 的 login 中，证书中是公钥。

而且 Certificates 分为两种，一种是 Development，就是开发的时候使用的，另一种是 Distribution ，发布的时候使用的。

你可以在 Xcode 登录对应账户，直接自动将对应证书导入到 KeyChain


### Identifiers

App ID:用来标识一个或者一组App，App ID是要和Xcode的Bundle ID保持一致或者是匹配的(通配)。

App ID分为下面2种：

+ Explicit App ID:唯一的App ID，这种App ID用于唯一标识一个APP.
+ Wildcard App ID:通配符App ID，用于标识一组APP.

每创建一个App ID，我们都可以设置该ID所需要使用的APP Services，即该App所需要使用的其他服务。

### Devices

Device就是能运行你APP的设备。Devices中包含了该账号中所有可用于开发和测试的设备UDID。每个账户中的设备数量限制是100个。假设你已经包含了100台设备，然后希望101这台设备能加入该账号下，于是你把100这个设备解除绑定，然后添加101这个设备.这是不可能这样子操作的，只能在membership year开始的时候才能这样子操作。

### Provisioning Profiles

一个Provisioning Profile文件包含了上述的内容:Certificate, App ID, Devices
我们要打包或在真机上运行一个APP

首先用证书来进行签名，用来标识这个APP是可信任的，完整的等等。指明它的App ID，并且验证Bundle ID是否一致。
如果是真机调试，需要确认这台设备是或包含在该账号下的测试设备中，以此来决定是否能运行程序。
而Provisioning Profile就是把这些信息全部囊括在一起，方便我们在调试和打包时使用，这样子我们只要在不同情况下选择不同的profile文件就行了。这个Provisioning Profile文件会在打包时嵌入到包内。

## Jenkins 的 ssh 连接问题

这次把 mac 作为 slave 机器，使用的是 ssh 连接，我在运行自动打包脚本的时候，无论如何都打包失败，报错为 `Command CodeSign failed with a nonzero exit code` 可以看到就是 上文说到的 代码签名错误，也就是说和证书有关，我发现网上说 SSH 连接是无用户的，因此需要重载 Mac 的 Keychain 。说实话真的找了很多资料才发现的。之前一直思路不对。

在运行脚本之前，加上这段，重载对应账户的 keychain 即可。
`security unlock-keychain -p "your pwd" ~/Library/Keychains/login.keychain`

