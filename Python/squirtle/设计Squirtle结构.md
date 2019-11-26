Squirtle 是用于将 vue 或者 React-native 自动化打包的库。

他首先需要有以下几个模块：

+ git 模块：处理 git 相关的操作
+ npm 模块：处理 npm 相关操作
+ cordova 模块：处理 cordova 相关操作
+ xcode 模块：处理 xcode 相关操作
+ exceptions 模块：处理 exceptions
+ `__init__` 模块：处理配置信息

最后在 squirtle 文件中组合各模块，暴露成 API 给用户。

vue - apk successfully
rn - apk successfully

TODO

1.文件路径问题，使用装饰器

2.设置 squirtle 文件的函数调用 是否可以尝试 yield 跳转？

3.优化 vue 部分的结构

4.环境检查到底应该怎么做？ 使用 subprocess 真的可行么？

5.由上述问题引出的报错监测机制

6.是不是不用每次都 install 花费大量时间？ 

7.import 都是红色的？

8.vue 和 rn 项目的 ipa 打包细节上区别？

9.npm 模块是否隔离开 vue 和 rn

10.调研 init 模块作用

11.还是把 命令行命令转化为 subprocess.run 指令封装成函数吧 需要去掉换行符么？

12.暴露的接口能否再友善些？

13.调研单元测试

14 研究 requests 为什么能引用成功

15 rn 和 cordova 生成的 安卓打包文件位置不一样，如何修正？
