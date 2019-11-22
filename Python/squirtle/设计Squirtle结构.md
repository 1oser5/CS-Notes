Squirtle 是用于将 vue 或者 React-native 自动化打包的库。

他首先需要有以下几个模块：

+ git 模块：处理 git 相关的操作
+ npm 模块：处理 npm 相关操作
+ cordova 模块：处理 cordova 相关操作
+ xcode 模块：处理 xcode 相关操作
+ exceptions 模块：处理 exceptions
+ `__init__` 模块：处理配置信息

最后在 squirtle 文件中组合各模块，暴露成 API 给用户。