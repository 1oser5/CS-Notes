# idea云同步配置

在多台计算机中进行开发是比较常见的情况，因此很多编辑器都推出了云储存功能。让我们简单介绍一下IDEA的云储存功能。


## 云配置

+ 通过设置 `Settings Repository` 插件进行同步，但是需要想要共享的设置创建 Git 存储库，共享起来更加方便
+ 通过 IDE Settings Sync 插件，其使用的是 JetBrains 服务器，不需要额外配置，但是同步设置和 JetBrains 绑定，无法共享

这里只介绍 Settings Repository 的使用方法。IDEA 默认和该插件绑定，默认开启，如果未启用，可以去 `Settings -> Preferences` Dialog 对话框的 Plugins 页上启用它。

1. 在任何托管库上创建 Git 储存库，例如 GitHub
2. 打开 IDEA，进入 `File -> Manage IDE Settings-> Settings Repository`
3. 将第一步创建库的url输入，选择 `Overwrite Remote`，第一次同步会让你输入token
4. 如果想从远端下载设置，点击 `Overwrite Local` 即可，如果想要应用俩端的配置，点击 `Merge`。

IDEA 默认为自动同步设置，如果想关闭自动设置同步，可以前往设置中关闭

## GitHub 获得 token 方法

> 文档地址 https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token