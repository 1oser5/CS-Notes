## 缘起

Windows 的换行符为 `CRLF`（也就是`\r\n`），而 Unix 家族的换行符为 `LF`(`\n`)。

为什么不同平台的换行符有所不同呢？

当时的电动打字机使用 `CR-LF` 作为换行，其中的 `CR` 表示将头移至行首，而 `LF`表示将其一直下一行，所以后来的 `DOS` 就遵循了类似设计。

计算器科学早期存储器很贵，有些人觉得在每行后面加两个字符太浪费了，于是就出现了分歧，也就是出现了 `LF` 作为换行符的系统。


## Git 跨平台问题


### autocrlf

跨平台开发最大的问题是，换行符发生改变之后，Git 会认为整个文件发生了修改，导致无法 `diff`。对这个问题，Git 提供了 `autocrlf` 的配置项，用于在提交和检出时自动转化换行符，该配置有三个选项：

+ **true** : 提交时转化为 `LF`，检出时转化为 `CRLF`
+ **false** : 提交检出均不转化
+ **input** : 提交时转化为 `LF`，检出不转化

配置方法:
```
# 提交时转换为LF，检出时转换为CRLF
git config --global core.autocrlf true

# 提交时转换为LF，检出时不转换
git config --global core.autocrlf input

# 提交检出均不转换
git config --global core.autocrlf false
```

### safecrlf

还有用于检查文件是否包含混合换行符的配置 `safecrlf` ，当你把 `autocrlf` 设置为 `false` 时，`safecrlf` 最好为 `true`，不然将会是灾难界别的错误。`autocrlf` 也有对应的三个可选项：

+ **true** : 拒绝提交包含混合换行符的文件
+ **false** : 允许提交包含混合换行符的文件
+ **warn** : 提交包含混合换行符的文件时给出警告

配置方法:
```
# 拒绝提交包含混合换行符的文件
git config --global core.safecrlf true

# 允许提交包含混合换行符的文件
git config --global core.safecrlf false

# 提交包含混合换行符的文件时给出警告
git config --global core.safecrlf warn
```

### 问题

1.换行策略需要与项目同步，不能仅仅依靠个人配置
2.文件需要进行什么处理，和文件本身属性相关


### 完美方案

在 对应的 Git 仓库配置 `.gitattributes` 文件，可以将上述问题完美解决

+ `.gitattributes` 拥有最高优先级，保证换行符风格一致
+ 可以对不同的文件进行不同处理

`.gitattributes` 配置
```
*               text=auto
*.txt		text
*.jpg		-text
*.bat	text eol=crlf
*.sh		text eol=lf
*.py		eol=lf
```
