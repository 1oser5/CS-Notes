+ [起步](#起步)
  + [关于版本控制](#关于版本控制)
  + [本地版本控制](#本地版本控制)
  + [集中化版本控制系统](#集中化版本控制系统)
  + [Git基础](#Git基础)
  + [初次运行Git前的配置](#初次运行Git前的配置)


# 起步

## 关于版本控制

版本控制是一种记录文件相关变化，以便将来查阅的特定版本的系统。

采用版本控制可以让你有效的保存各个版本的文件。在你操作失误或者心情不好乱弄一通时，版本控制可以有效帮你“回到过去”。


### 本地版本控制

许多人习惯用复制整个项目的方式来进行本地的版本控制，这样有效，但是未免会造成版本控制混乱，取名麻烦，复制时间消耗等问题。

之后人们也开发出了用简单数据库来记录文件差异的方式。
![avator](../../pic/local-version-control.png)
其中最流行的就是 rcs，许多计算机系统还看得到它的声影。它通过某种特定的补丁文件，记录对应文件修改前后的内容变化。每次修订完之后，rcs 将不断打补丁来计算各版本的文件内容。

### 集中化版本控制系统

那要在不同的系统中，或者不同的设备中进行版本控制呢？于是集中化版本控制系统（Centralized Version Control Systems, CVCS）出现了。类似 CVS, Subversion 等，都有一个集中管理的服务器，用户通过客户端统一向该服务器下载文件或者更新文件。

![avator](../../pic/centralized-version-control.png)

这种版本控制有一定好处，每个人可以在一定程度上看到项目上其他人在干什么，而管理员也可以轻松的分配权限，管理起来比本地版本控制容易得多。

但也存在隐患，比如中心服务器宕机一个小时，那么一个小时中所有人都不能提交或者下载，是否影响效率。亦或者更严重，中心服务器数据丢失，导致整个项目无法复原，只能依靠本地存储的快照进行修复。

### 分布式版本控制系统

于是分布式版本控制系统（Distributed Version Control System, DVCS）出现了。客户端不止提取最新版本的快照，而是将整个代码仓库进行镜像。这样一来，任何协调工作的服务器故障了，都可以使用任意一台电脑的本地仓库进行恢复。

![avator](../../pic/distributed-version-control.png)

## Git基础

Git 与其他 DVCS 系统的差异

### 直接记录快照，而非差异比较

Git 只关心文件数据的整体是否发生变化，其他系统则只关心文件具体内容的差异。
![avator](../../pic/svn-diff.png)

Git 并不保存这些文件的差异数据，相对来说，Git 更像是把变化的文件快照后，记录在一个微型的文件系统中，每次提交更像后，他会总览一遍所有文件的指纹信息并对修改了的文件做一快照，然后保存执行这个快照的索引。为了提高性能，如果文件没有变化，则只保存对上一次快照的链接。

![avator](../../pic/git-diff.png)

### 几乎所有的操作都是本地执行

Git 大多才做都可以在本地执行，不需要联网。因为本地仓库存储着最新版本的代码和修改记录，你完全可以在断网的情况下查阅版本修订和修改代码，再在连上网络之后上传到远程仓库。


### 时刻保持数据的完整性

保存到 Git 之前，所有数据都要进行内容的校验和（checksum），并将此结果作为数据的唯一标识和索引。

Git 使用 SHA-1 算法计算数据的校验和，通过对文件的内容或目录的结构计算出一个 SHA-1 哈希值，作为指纹字符串，该字符由 40 个 16 进制字符串组成，看上去像：
```
24b9da6552252987aa493b52f8696cd6d3b00373
```

事实上在 Git 数据库中都是用此哈希值来进行索引的，而不是文件名。

### 多数操作仅添加数据

Git 的大多数操作都只是在 Git 数据库中添加数据，因为多数的不可逆操作都会时重现历史版本变得困难重重。

### 文件的三种状态

对任何一个文件，在 Git 中只有三种状态，已提交（committed），已修改（modified），以暂存（staged）。

+ 已提交（committed）: 文件已经保存到本地仓库中。
+ 已修改（modified）: 文件被修改但还未提交保存。
+ 已暂存（staged）: 文件被放在下次提交要保存的清单中。

Git 保存文件的三个工作区域： Git 的工作目录，暂存目录，本地仓库。

![avator](../../pic/work.png)

每个项目都有一个 Git 目录（如果是 git clone 则 .git 是 Git 目录，如果是 git clone --bare，新建目录本身急速 Git 目录）。Git 目录用来保存元数据和对象数据库。该目录非常重要，每次克隆镜像仓库其实都是克隆该目录中的数据。

从项目中取出某个版本的所有文件和目录，用来后续工作的就是工作目录。这些文件实际上都是从 Git 目录中读取出来的。

暂存区只是一个存放在 Git 目录中的文件（Index 文件）

基本 Git 工作流程：

+ 在工作目录修改文件。
+ 对修改文件进行快照，保存到暂存区域。
+ 提交更新，将暂存区域的文件快照转储到 Git 目录中。

## 初次运行Git前的配置

Git 提供了一个叫 git config 的工具来管理相应的工作环境变量。正是这些环境变量，决定了 Git 在各个环节的行为和工作方式，变量可以存储在以下三个地方：

+ /etc/gitconfig 文件：系统中对所有用户普遍适用的配置，如果使用 git config --system 读取的就是该文件。
+ ~/.gitconfig 文件：用户目录下的配置文件，只适配与该用户，使用 git
config --global 读取的就是该文件。
+ 当前项目的 git 目录的配置文件（也就是工作目录的 .git/config 文件）：配置仅针对当前目录

**每一级别的配置会覆盖上一级相同配置**


### 用户信息

配置个人账户和电子邮箱，这很重要。在每次 Git 提交的时候这两条信息都会被引用，随着更新内容一起永久纳入历史记录：
```
git config --global user.name "xxxx"
git config --global user.email xxxx@example.com
```
使用了 global 关键字则修改的是用户目录的配置文件（即 ~/.gitconfig）。如果想在项目中使用不同的用户提交，去掉 global 关键字即可，新设定保存在 工作目录的 .git/config 文件。

### 文本编辑器

Git 需要你输入一下额外信息的时候，会自动调用一个外部编辑器，一般是操作系统默认的编辑器，一般可能是 vi 或者 vim。如果你有其他偏好，比如 Emacs，可以重新设置：
```
git config --global core.editor emacs
```
  
### 比较差异工具

在合并冲突是使用哪种差异分析工具，必须要修改为 vimdiff 的话
```
git config --global merge.tool vimdiff
```

### 查看配置信息

可以使用`git config --list `命令查看已有配置信息。

有时候会看到重复的变量，那说明他们来之不同的文件，Git 实际采用的是最后一个。

也可以直接查阅某个环境变量的设定，只把特定的名字跟在后面即可
```
git config user.name
```

# Git 基础

## 取得项目的 Git 仓库

### 在工作目录中初始化新库

要对某个现有的项目使用 Git 管理，只需到此项目的目录执行：

```
git init
```

初始化之后，当前目录会出现一个 .git 目录，所以 Git 目录下的资源和数据都被存放在该目录下，不过目前仅仅只是按照既有的结构和框架初始化好了里面的文件和目录，还没有开始追踪管理项目中的任何一个文件。

如果当前目录有几个文件向纳入版本控制，首先是要 `git add`命令告诉 Git 开始对这些文件进行追踪

```
git add *.c
git add README
git commit -m 'initial project version'
```

### 从现有仓库克隆

克隆仓库的命令格式为 `git clone [url]`

```
git clone git://github.com/schacon/grit.git
```

这会在当前目录创建一个名为 grit 的目录，其中包含一个 `.git` 目录。用于保存下载下来的所有版本的记录，然后取出最新版的记录进行拷贝。

如果你自定义克隆下来的项目的名字，可以在上面命令末尾指定新名字

```
git clone git://github.com/schacon/grit.git my_grit

```


## 记录每次更新到仓库

工作目录下的文件不外乎两种状态，已跟踪和未跟踪。

已跟踪的文件是指被纳入版本控制的文件，上次快照中有他们的记录，工作一段时间后，他们的状态可能是未更新，已修改或者已放入暂存区。其余的文件都是未跟踪文件。

克隆的所有文件都是已跟踪文件。

![avator](../../pic/git-file-status-lifecycyle.png)

### 检查当前文件状态

要确定哪些文件处于哪些状态，可以还是要 `git status` 命令。

如果你新建一个 README 文件，保存后运行 `git status` 会看到这些文件出现在未跟踪文件列表中：
```
$ vim README
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        README

nothing added to commit but untracked files present (use "git add" to track)
```

未追踪文件意味着 Git 在之前的快照中没有这些文件；Git 不会将纳入追踪范围。

### 追踪新的文件

使用 `git add` 开始追踪一个新文件，要追踪 README 文件，运行：

```
git add README
```

此时在运行 `git status` 会发现 README 已经被追踪，并处于暂存状态

```
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   README
```

只要在 “Changes to be committed” 这行下面的，就说明是已暂存状态，如果此时提交，那么该文件的版本将被保留在历史记录里。

`git add` 后面可以指明要跟踪的文件或目录路径，如果是目录，Git 会递归追踪目录下的所有文件。

git add 的潜台词就是把目标文件放在暂存区域，同时把未追踪的文件标记为已标记

### 暂存已修改的文件

修改之前已追踪的文件 `benchmarks.rb`，然后再次运行 `status` 命令

```
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   README

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   benchmarks.rb
```

文件 `benchmarks.rb` 出现在 “Changes not staged for commit” 这行下面，说明已追踪的文件内容发生了变化，但还没有放到暂存区，要暂存这次更新，需要 `git add`（这个是个多功能命令，根据目标文件状态不同，此命令的效果也不同，他可以用来追踪新文件，也可以把已追踪文件放到暂存区，还能用于合并时把有冲突的文件标记为已解决）。运行 `git add` 之后将 `benchmarks.rb` 放到暂存区，执行 `status`：
```
$ git add benchmarks.rb
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   README
        modified:   benchmarks.rb
```
现在两个文件都被暂存了，下次提交时会被一并送到仓库。此时如果你想在修改 `benchmarks.rb` 文件。再运行 `status`：
```
$ vim benchmarks.rb
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   README
        modified:   benchmarks.rb

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   benchmarks.rb
```

`benchmarks.rb` 出现了两次，一次未暂存，一次暂存，如果此时提交，那么提交的是第二次修改前的版本，如果想要提交最新版，需要再一次 `git add` 暂存起来。

### 忽略某些文件

一般我们总有些文件无需 Git 的管理，也不希望他们出现在未追踪文件列表里，通常是些日志文件或者临时文件等，我们可以创建一个名为 `.gitignore` 的文件，列出要忽略的文件:
```
$ cat .gitignore
*.[oa]
*~
```
第一行告诉 Git 忽略 `.o` 或 `.a` 结尾的文件，第二行告诉 Git 忽略以波浪符 `~` 结尾的文件。

文件 `.gitignore` 的格式规范如下：

+ 所有空行和 # 注释都被 Git 忽略
+ 使用标准的 glob 匹配模式
+ 如果匹配模式是目录需要在后面跟上一个 /
+ 要忽略指定模式之外的文件或目录，在文件前加上 ! 取反


所谓的 `glob` 模式是指 shell 所使用的简化了的正则表达式。星号（`*`）匹配零个或多个任意字符；`[abc]` 匹配任何一个列在方括号中的字符（这个例子要么匹配一个 a，要么匹配一个 b，要么匹配一个 c）；问号（`?`）只匹配一个任意字符；如果在方括号中使用短划线分隔两个字符，表示所有在这两个字符范围内的都可以匹配（比如 `[0-9]` 表示匹配所有 0 到 9 的数字）。

一个常见的 `.gitignore` 文件的例子：
```
# 此为注释 – 将被 Git 忽略
# 忽略所有 .a 结尾的文件
*.a
# 但 lib.a 除外
!lib.a
# 仅仅忽略项目根目录下的 TODO 文件，不包括 subdir/TODO
/TODO
# 忽略 build/ 目录下的所有文件
build/
# 会忽略 doc/notes.txt 但不包括 doc/server/arch.txt
doc/*.txt
# ignore all .txt files in the doc/ directory
doc/**/*.txt
```

`**/` 符号在 Git 1.8.2 之后可用


### 查看已暂存和为暂存的更新

```
$ git diff 
```
可以查看尚未暂存的文件更新了哪些部分

```
git diff --cached or git diff --staged
```

看看暂存文件和上次提交快照有哪些差异

### 提交更新

提交命令
```
$ git commit
```

配合 `-m` 参数提交说明
```
$ git commit -m "Story 182: Fix benchmarks for speed"
```

每一次提交操作，都是对项目的一次快照。


### 跳过使用暂存区域

只要在提交时给 `git commit` 加上 `-a` 选项，Git 就会把所有自动以跟踪过的文件放入暂存区一并提交，从而跳过 `git add` 步骤。
```
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   benchmarks.rb

no changes added to commit (use "git add" and/or "git commit -a")
$ git commit -a -m 'added new benchmarks'
[master 83e38c7] added new benchmarks
 1 files changed, 5 insertions(+)
```
### 移除文件

要从 Git 中删除某个文件，就必须要从已跟踪文件清单中移除（确切说，是从暂存区移除），然后提交。可以使用 `git rm` 完成，并连带着删除指定的文件。

如果你手动删除目录中的文件，那么运行 `git status` 会看到 `Changes not staged for commit`部分看到：

```
$ rm grit.gemspec
$ git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    grit.gemspec

no changes added to commit (use "git add" and/or "git commit -a")
```

然后在运行 `git rm` 记录此次移除文件的操作

```
$ git rm grit.gemspec
rm 'grit.gemspec'
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        deleted:    grit.gemspec
```

最后提交的时候，文件就不在纳入版本管理，如果删除之前已经放到暂存区域的话，必须要使用强制删除选项 `-f` ，以防误删文件丢失修改的内容。

另一种情况是你只是想将文件从 Git 仓库删除，但是将其保留在工作目录中。要移除追踪但不删除文件，运行
```
$ git rm -cached readme.txt
```
后面可以列出文件或者目录名，可以使用 glob 模式
```
$ git rm log/\*.log
```
不加反斜杠的话，不会递归调用，只会删除 log 目录下扩展名为 `.log` 的文件。

### 移动文件

不行别的 VSC 系统，Git 不跟踪文件移动操作，但是你在 Git 中重命名了某个文件，Git 仍然知道。

要在 Git 中对文件进行改名，运行
```
$ git mv f1 f2
```
他会如预期般工作，此时查看状态时，也会明白无误的看到关于重命名的操作
```
$ git mv README.txt README
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        renamed:    README.txt -> README
```
其实 `git mv` 相当于运行了

```
$ mv README.txt README
$ git rm README.txt
$ git add README
```
