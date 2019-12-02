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
rn - ipa successfully

TODO

1.文件路径问题，使用装饰器

2.设置 squirtle 文件的函数调用 是否可以尝试 yield 跳转？

3.优化 vue 部分的结构 √

4.环境检查到底应该怎么做？ 使用 subprocess 真的可行么？

5.由上述问题引出的报错监测机制

6.是不是不用每次都 install 花费大量时间？ 

7.import 都是红色的？ √

8.vue 和 rn 项目的 ipa 打包细节上区别？ √

9.npm 模块是否隔离开 vue 和 rn √

10.调研 init 模块作用

11.还是把 命令行命令转化为 subprocess.run 指令封装成函数吧 需要去掉换行符么？ 可以使用封装级别再高些的函数么

12.暴露的接口能否再友善些？

13.调研单元测试

14 研究 requests 为什么能引用成功 √

15 rn 和 cordova 生成的 安卓打包文件位置不一样，如何修正？

16 需要修改 `project.pbxproj` 文件

17 生成的 ios 目录也不一样，怎么适配？

18 在何处进行错误捕捉更加合适？是每一个调用 subprocess 的函数还是暴露的接口部分。


## topic 版本

2019.12.02

修正了部分结构，将函数进行更完善的封装，使得其可以服务于不同的情况。

整理的 xcode 打包部分，将 rn 和 vue 目录结构不同的问题修正，实现了使用一套函数流程实现不同项目的打包

将 Node 类设立子类，实现了 vue 和 rn 子类，调用不同方法。

### vue2apk done
### rn2apk done




发现 vue 和 rn 的 project.pbxproj 文件设置不一样，project.pbxproj 可以通过右键 xxx.xcodeproj，选择显示包内容打开。

vue2ios的，需要修改两处地方，230行和362

230行需要添加
```
DevelopmentTeam = 打包team编号
```

362 行需要添加
```
DEVELOPMENT_TEAM = 打包team编号
```
如何找到位置成了关键


使用 pbxproj 第三方库解析 pbxproj，这就是 python 语言的特点，啥第三方库都找到

我现在比较担心的就是 rn 和 vue 的 project.pbxproj 的目录机构不一样，得再找一遍也太难了吧。

这个文件里的变量名全部是乱码，真的恶心人。只能通过自己一层一层的剥离找到自己想要的变量的 key 值

vue 的 teamid 添加成功了，但是还有一个问题就是在使用 cordova 打包的时候，是没具体设置为 iphone developer 的

看看能不能修改 sign 方式为手动，修复这个问题，还是修改 pbxproj 可以修改这个问题！