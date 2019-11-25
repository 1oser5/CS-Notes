把大象放进冰箱里需要几步？xcode 打包就需要几步。

虽然命令很长但是还是比较好理解的


## 1.清空工作区
```
xcodebuild clean -workspace <workspace_path>  -scheme <app_scheme> -configuration <Debug Or Release>

// 实际操作：
xcodebuild clean -workspace /Users/wuzhihua/Desktop/Project/hiveconsumer/HiveConsumer/HiveConsumer.xcworkspace -scheme HiveConsumer -configuration Release
```

+ workspace : 项目.xcworkspace的绝对路径
+ app_scheme : 项目App的scheme (非Extension App)
+ configuration : 编译环境，Debug Or Release

## 2.导出 archive 文件目录

```
xcodebuild archive -workspace <workspace_path> -scheme <app_scheme> -archivePath <xcarchive_path>

// 实际操作：
xcodebuild archive -workspace /Users/wuzhihua/Desktop/Project/hiveconsumer/HiveConsumer/HiveConsumer.xcworkspace -scheme HiveConsumer -archivePath /Users/wuzhihua/Desktop/App/archive/hiveconsumer.xcarchive
```

+ archivePath : 导出 xcarchive 路径


## 3.配置导包
```
xcodebuild -exportArchive -archivePath <xcarchive_path> -exportPath <export_ipa_path> -exportOptionsPlist <exportOptionsPlist_path>

// 实际操作:
xcodebuild -exportArchive -archivePath /Users/wuzhihua/Desktop/App/archive/hiveconsumer.xcarchive -exportPath /Users/wuzhihua/Desktop/App/ipa/ -exportOptionsPlist /Users/wuzhihua/Desktop/App/fcapp_config.plist
```

+ xcarchive_path : 操作2中的 archivePath
+ export_ipa_path ipa 文件导出路径
+ exportOptionsPlist_path : 导报配置文件

就是这么简单，现在的问题就是 exportOptionsPlist 文件能不能适配所有项目