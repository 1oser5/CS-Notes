## 原因

公司需求，需要使用 http 请求来对 jenkins 发送构筑请求，实现远程构筑，jenkins 也提供了相当丰富的 API 来实现类似功能。


## 过程

### 安装插件

需要支持远程授权，需要下载对应插件 `Build Authorization Token Root Plugin`

### token配置

选择对应用户，点击设置，然后将其 API Token 保存下来（只会显示一次，所以一定要记得保存）。

![avator](../../pic/jenkins-user-token-config.jpg)

### 项目配置

在对应的项目，`构建触发器` 部分勾选 `触发远程构建`，再讲之前生成的 token 写入。

![avator](../../pic/jenkins-build-remote-trigger.jpg)

在输入 token 下发有对应的 url 提示，其 url 地址格式应该为 `JENKINS_URL/job/test/build?token=TOKEN_NAME` 或者 ` /buildWithParameters?token=TOKEN_NAME`，同时你可以使用添加额外参数 `cause` 来描述构筑原因， `&cause=Cause+Text`。

### 请求发送


#### 问题1

我想使用 postman 对 jenkins 提供的地址进行请求的发送，遇到了第一个问题 `Error 403 No valid crumb was included in the request`

### 解决方案

在jenkins 的Configure Global Security下 , 取消“防止跨站点请求伪造（Prevent Cross Site Request Forgery exploits）”的勾选。

![avator](../../pic/jennkins-prevent-croess.jpeg)


#### 问题2

在解决上述问题之后，我再次进行 post 请求尝试，则报错为 `Authentication required`，似乎是用户权限的问题，在查找了一些解决方案之后，找到了最好的解决方案

#### 解决方案

在 url 中加入账户信息 `https://user:password@JENKINS_URL/job/test/build?token=TOKEN_NAME`，这样就可以通过用户验证。



## Jenkins HTTP API

jenkins 提供了一系列有趣的 API，这里暂列几个非常有用的：

这里定义 `BaseUrl` 为 `<jenkins url>/view/<view name>/job/<job name>`

+ 查看构筑状态: `BaseUrl/<id>/api/json`
+ 查看最后一次构筑: `BaseUrl/lastBuild/api/json`
+ 查看最后一次控制台输出: `BaseUrl/lastBuild/consoleText`