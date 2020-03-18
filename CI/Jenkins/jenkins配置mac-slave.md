## 原因

之前公司的 jenkins 服务一直在 mac 机器上，但是 mac 多用户很不方便，然后迁移到 liunx 上，之前的 mac 服务器就需要作为一个 slave 了。

## 过程

我开始首先选择的是和之前 windows slave 一样的连接方式，使用 `Launch agent by connecting it to the master` 连接，但是我把对应的 jar 文件下载下来之后，发现 mac 无法运行文件，提示为 `您需要下载 Java Runtime Enviroment 才能打开此文件`，简单查了一下是因为苹果觉得 java 不太安全，进行了一些封禁。我没找到特别好的解决方案。

在网上看到有人使用 ssh 连接进行 slave 配置，由于 mac 之前已经配置过 ssh 共享了。所以可以一试。这次选择 `Launch agents via SSH` 的启动方式，主机就写 mac 的ip 地址，账户密码则写登录mac的账户密码。记得要把账户密码设置为 jenkins 的 credentials。然后很关键的一点，将下面的 `Host Key Verification Strategy` 选择为 `Non verifying Verification Strategy` 这样才能正常连上。