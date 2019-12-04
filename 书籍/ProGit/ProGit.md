
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

## 查看提交历史

提交若干更新或者克隆的新的项目之后想要查看提交历史，可以使用 `git log` 查看，按 `q` 退出。

如果不加参数，`git log` 会按时间列出所有的提交记录，最新的排在最上面，每次更新都有一个 SHA-1 校验和，作者的名字和电子邮箱、提交时间呢，最后一个缩进表示段落说明


通常我们使用 `-p` 参数显示每次提交的差异，用 `-2` 仅显示最近两次的更新。
```
$ git log -p -2
commit ca82a6dff817ec66f44342007202690a93763949
Author: Scott Chacon <schacon@gee-mail.com>
Date:   Mon Mar 17 21:52:11 2008 -0700

    changed the version number

diff --git a/Rakefile b/Rakefile
index a874b73..8f94139 100644
--- a/Rakefile
+++ b/Rakefile
@@ -5,5 +5,5 @@ require 'rake/gempackagetask'
 spec = Gem::Specification.new do |s|
     s.name      =   "simplegit"
-    s.version   =   "0.1.0"
+    s.version   =   "0.1.1"
     s.author    =   "Scott Chacon"
     s.email     =   "schacon@gee-mail.com

commit 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7
Author: Scott Chacon <schacon@gee-mail.com>
Date:   Sat Mar 15 16:40:33 2008 -0700

    removed unnecessary test code

diff --git a/lib/simplegit.rb b/lib/simplegit.rb
index a0a60ae..47c6340 100644
--- a/lib/simplegit.rb
+++ b/lib/simplegit.rb
@@ -18,8 +18,3 @@ class SimpleGit
     end

 end
-
-if $0 == __FILE__
-  git = SimpleGit.new
-  puts git.show
-end
\ No newline at end of file
```

如果你需要查看单词级别的对比，可以在 `git log -p` 后面加上 `--word-diff` 选项，这个在论文以及书籍类文件对比时相当有用。
```
$ git log -U1 --word-diff
commit ca82a6dff817ec66f44342007202690a93763949
Author: Scott Chacon <schacon@gee-mail.com>
Date:   Mon Mar 17 21:52:11 2008 -0700

    changed the version number

diff --git a/Rakefile b/Rakefile
index a874b73..8f94139 100644
--- a/Rakefile
+++ b/Rakefile
@@ -7,3 +7,3 @@ spec = Gem::Specification.new do |s|
    s.name      =   "simplegit"
    s.version   =   [-"0.1.0"-]{+"0.1.1"+}
    s.author    =   "Scott Chacon"
```

`git log` 还有别的好用的参数，比如 `--stat` 仅显示简要的增改行数统计
```
$ git log --stat
commit ca82a6dff817ec66f44342007202690a93763949
Author: Scott Chacon <schacon@gee-mail.com>
Date:   Mon Mar 17 21:52:11 2008 -0700

    changed the version number

 Rakefile |    2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
 ```

还有个常用的 `--pretty` 选项，可以指定使用不同于默认格式的方式展示提交历史，比如 `online` 将每个提交放到一行显示。

```
$ git log --pretty=oneline
ca82a6dff817ec66f44342007202690a93763949 changed the version number
085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7 removed unnecessary test code
a11bef06a3f659402fe7563abf99ad00de2209e6 first commit
```

你甚至可以使用 `format` 来自定义你想要显示的格式，便于后期的提取。

```
$ git log --pretty=format:"%h - %an, %ar : %s"
ca82a6d - Scott Chacon, 11 months ago : changed the version number
085bb3b - Scott Chacon, 11 months ago : removed unnecessary test code
a11bef0 - Scott Chacon, 11 months ago : first commit
```

`format` 常用格式占位符及写法

|选项	|说明 |
|--|--|
|%H|	提交对象（commit）的完整哈希字串|
|%h	|提交对象的简短哈希字串|
|%T	|树对象（tree）的完整哈希字串|
|%t	|树对象的简短哈希字串|
|%P	|父对象（parent）的完整哈希字串|
|%p	|父对象的简短哈希字串|
|%an|	作者（author）的名字|
|%ae|	作者的电子邮件地址|
|%ad|	作者修订日期（可以用 -date= 选项定制格式）|
|%ar|	作者修订日期，按多久以前的方式显示|
|%cn|	提交者(committer)的名字|
|%ce|	提交者的电子邮件地址|
|%cd|	提交日期|
|%cr|	提交日期，按多久以前的方式显示|
|%s	|提交说明|

使用 `oneline` 或者 `format` 时结合 `--graph` 选项，用简单图像展示分支状况

```
$ git log --pretty=format:"%h %s" --graph
* 2d3acf9 ignore errors from SIGCHLD on trap
*  5e3ee11 Merge branch 'master' of git://github.com/dustin/grit
|\
| * 420eac9 Added a method for getting the current branch.
* | 30e367c timeout code and tests
* | 5a09431 add timeout protection to grit
* | e1193f8 support for heads with slashes in them
|/
* d6016bc require time for xmlschema
*  11d191e Merge branch 'defunkt' into local
```

`git log` 常用选项

|选项	|说明|
|--|--|
|-p	|按补丁格式显示每个更新之间的差异。|
|--word-diff|	按 word diff 格式显示差异。|
|--stat	|显示每次更新的文件修改统计信息。|
|--shortstat	|只显示 --stat 中最后的行数修改添加移除统计。|
|--name-only	|仅在提交信息后显示已修改的文件清单。|
|--name-status|	显示新增、修改、删除的文件清单。|
|--abbrev-commit|	仅显示 SHA-1 的前几个字符，而非所有的 40 个字符。|
|--relative-date|	使用较短的相对时间显示（比如，“2 weeks ago”）。|
|--graph	|显示 ASCII 图形表示的分支合并历史。|
|--pretty	|使用其他格式显示历史提交信息。可用的选项包括 oneline，short，full，fuller 和 format（后跟指定格式）。|
|--oneline |	--pretty=oneline --abbrev-commit 的简化用法。|

### 限制输出长度

限制时间长度，比如 `--since` 和 `--until`，下面命令列出近俩周内的提交：
```
$ git log --since=2.weeks
```

其他常用选择筛选方式

|选项	|说明|
|--|--|
|-(n)	|仅显示最近的 n 条提交|
|--since, --after|	仅显示指定时间之后的提交。|
|--until, --before|	仅显示指定时间之前的提交。|
|--author|	仅显示指定作者相关的提交。|
|--committer|	仅显示指定提交者相关的提交。|

可以多次使用删选条件，比如要筛选出 2008 年 10 月期间，Junio Hamano 提交的但未合并的测试脚本，可以使用

```
$ git log --pretty="%h - %s" --author=gitster --since="2008-10-01" \
   --before="2008-11-01" --no-merges -- t/
5610e3b - Fix testcase failure when extended attribute
acd3b9e - Enhance hold_lock_file_for_{update,append}()
f563754 - demonstrate breakage of detached checkout wi
d1a43f2 - reset --hard/read-tree --reset -u: remove un
51a94af - Fix "checkout --track -b newbranch" on detac
b0ad11e - pull: allow "git pull origin $something:$cur
```

## 撤销记录

### 修改最后一次提交

我们发现刚的提交有错误或者漏掉了某个文件会，可以修改上一次提交
```
$ git commit --amend
```
运行该命令后会启动文本编辑器，能看到上次提交的说明，可以编辑后保存，就会使用新的提交说明覆盖上一次提交。

如果你遗漏了某个文件，也可以运行
```
$ git commit -m 'initial commit'
$ git add forgottrn_file
$ git commit --amend
```

上面三条命令最终只是产生了一个提交，第二条命令修正了的第一条的提交内容。

### 取消已暂存的文件

有两份文件进行了修改，想要分开提交，但是一不小心用 `git add`，加到了暂存区域，如何撤销其中一个呢？
`git status` 告诉了我们怎么做
```
$ git add .
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   README.txt
        modified:   benchmarks.rb
```
可以使用 `git reset HEAD <file>` 方式取消暂存

试着取消暂存 `benchmark.rb` 文件

```
$ git reset HEAD benchmarks.rb
Unstaged changes after reset:
M       benchmarks.rb
```
`benchmarks.rb` 回到了已修改但为暂存状态

### 取消对文件的修改

如果觉得对 `benchmarks.rb` 的修改没有必要，需要取消，使用 `git checkout`指令。

```
git checkout -- benchmarks.rb
```

这条指令有风险，请确定你真不需要修改该文件

## 远程仓库的使用

### 查看当前的远程库

可以使用 `git remote` 操作查看当前配置了哪些远程仓库，他会列出每个仓库的简短名字。

在克隆完一个仓库之后，你至少可以看到一个名为 `origin` 的远程库，Git 默认使用该名字来标识你所克隆的远程库。
```
$ git clone git://github.com/schacon/ticgit.git
Cloning into 'ticgit'...
remote: Reusing existing pack: 1857, done.
remote: Total 1857 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (1857/1857), 374.35 KiB | 193.00 KiB/s, done.
Resolving deltas: 100% (772/772), done.
Checking connectivity... done.
$ cd ticgit
$ git remote
origin
```
可加上 `-v` 选项，查看对应克隆地址
```
$ git remote -v
origin  git://github.com/schacon/ticgit.git (fetch)
origin  git://github.com/schacon/ticgit.git (push)
```

如果有多个远程库，会将其全部列出
```
$ cd grit
$ git remote -v
bakkdoor  git://github.com/bakkdoor/grit.git
cho45     git://github.com/cho45/grit.git
defunkt   git://github.com/defunkt/grit.git
koke      git://github.com/koke/grit.git
origin    git@github.com:mojombo/grit.git
```
上面只有 `origin` 使用 `SSH URL` 链接，意味着我只有这个库我可以推送数据上去。

### 添加远程仓库

要添加一个远程仓库，并使用指定的简单名字，可以使用 `git remote add [shortname] [url]`:

```
$ git remote
origin
$ git remote add pb git://github.com/paulboone/ticgit.git
$ git remote -v
origin    git://github.com/schacon/ticgit.git
pb    git://github.com/paulboone/ticgit.git
```
现在可以用字符串 `pb` 指代对应的仓库地址，比如要抓取所有 Paul 有的，但本地仓库没有的信息，可以运行 `git fetch pb`:
```
$ git fetch pb
remote: Counting objects: 58, done.
remote: Compressing objects: 100% (41/41), done.
remote: Total 44 (delta 24), reused 1 (delta 0)
Unpacking objects: 100% (44/44), done.
From git://github.com/paulboone/ticgit
 * [new branch]      master     -> pb/master
 * [new branch]      ticgit     -> pb/ticgit
```

### 从远程库抓取数据

用以下命令从远程库抓取数据
```
$ git fetch [remote-name]
```
此命令回到远程库中拉取所有你本地仓库还没有的数据。运行完成后你可以在本地访问该远程仓库的所有分支，并将某个分支合并到本地。

如果克隆了一个仓库，则自动将远程仓库归于 `origin`。所有 `git fetch origin` 会抓取你上次克隆或者 `fetch` 之后别人的更新。 `fetch` 只是将远端的数据拉到本地仓库，并自动合并到当前工作分支。

如果设置了某个分支用于追踪某个远程仓库的分支，可以使用 `git pull` 命令自动抓取数据下来，并且将远程仓库自动合并到本仓库中当前分支。实际上 `git clone` 本质上就是自动创建了本地的 `master` 分支用于追踪远程仓库的 `master` 分支。


### 推送数据到远程仓库

项目进行到一定阶段，或者要和别人分享成果，就需要将本地仓库中的数据推送到远程仓库。
```
git push [remote-name] [brance-name]
```
一般来讲会自动使用默认的 `master` 和 `origin` 名字
```
$git push origin master
```

只有在所克隆的服务器上有写权限，并且在你 `push` 之前没有别人 `push` 过，才能成功，也就是说你应当 `pull` 之后再进行 `push`。


### 查看远程仓库信息

使用 `git remote show [remote-name]` 查看某个远程仓库的详细信息。
```
$ git remote show origin
* remote origin
  URL: git://github.com/schacon/ticgit.git
  Remote branch merged with 'git pull' while on branch master
    master
  Tracked remote branches
    master
    ticgit
```

### 远程仓库的删除和命名

可以使用 `git remote rename` 命令修改某个远程仓库在本地的简称，比如把 `pb` 改成 `paul`:
```
$ git remote rename pb paul
$ git remote
origin
paul
```
仓库迁移或者不再贡献代码，移除对应远程仓库，使用 `git remote rm` 命令:
```
$ git remote rm paul
$ git remote
origin
```

## 打标签
Git 可以在某一时间节点的版本打上标签，人们在发布版本的时候经常怎么做。
### 列显已有的标签
运行 `git tag` 即可:

```
$ git tag
v0.1
v1.3
```

标签是按字母顺序排序，所以标签先后不表示重要程度。

可以使用特定的搜索模式列出符合条件的标签
```
$ git tag -l 'v1.4.2.*'
v1.4.2.1
v1.4.2.2
v1.4.2.3
v1.4.2.4
```

### 新建标签

Git 的标签有两种 : 轻量级的（lightweight）和含附注的（annotated）

轻量级标签：不会变化的分支，实际上他就是一个指向特定标签的引用。
附注标签：存储在仓库中的一个独立对象，有自身的校验和信息，标签的名字，电子邮箱和日期

### 含附注的标签

创建一个含附注类型的标签非常简单，用 `-a`（annotated） 指定标签名字即可：
```
$ git tag -a v1.4 -m 'my version 1.4'
$ git tag
v0.1
v1.3
v1.4
```
而 `-m` 选项则指定了对应的标签说明，Git 会将其一同保存在标签对象，如果没给出，Git 会启动文本编辑软件供你输入。

可以使用 `git show` 命令查看相应标签的版本信息，并显示打标签的提交对象

```
$ git show v1.4
tag v1.4
Tagger: Scott Chacon <schacon@gee-mail.com>
Date:   Mon Feb 9 14:45:11 2009 -0800

my version 1.4

commit 15027957951b64cf874c3557a0f3547bd83b3ff6
Merge: 4a447f7... a6b4c97...
Author: Scott Chacon <schacon@gee-mail.com>
Date:   Sun Feb 8 19:02:46 2009 -0800

    Merge branch 'experiment'
```

### 签署标签

如果你有私钥，可以用 GPG 来签署标签，只需要把之前的 `-a` 改为 `-s`（signed）
```
$ git tag -s v1.5 -m 'my signed 1.5 tag'
You need a passphrase to unlock the secret key for
user: "Scott Chacon <schacon@gee-mail.com>"
1024-bit DSA key, ID F721C45A, created 2009-02-09
```

再运行 `git show` 会看到对应的 GPG 签名
```
$ git show v1.5
tag v1.5
Tagger: Scott Chacon <schacon@gee-mail.com>
Date:   Mon Feb 9 15:22:20 2009 -0800

my signed 1.5 tag
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1.4.8 (Darwin)

iEYEABECAAYFAkmQurIACgkQON3DxfchxFr5cACeIMN+ZxLKggJQf0QYiQBwgySN
Ki0An2JeAVUCAiJ7Ox6ZEtK+NvZAj82/
=WryJ
-----END PGP SIGNATURE-----
commit 15027957951b64cf874c3557a0f3547bd83b3ff6
Merge: 4a447f7... a6b4c97...
Author: Scott Chacon <schacon@gee-mail.com>
Date:   Sun Feb 8 19:02:46 2009 -0800

    Merge branch 'experiment'
```

### 轻量级标签

轻量级标签保存着对应提交对象的校验信息的文件，要创建这样一个标签，直接给出标签名即可
```
$ git tag v1.4-lw
$ git tag
v0.1
v1.3
v1.4
v1.4-lw
v1.5
```

### 验证标签
可以使用 `git tag -v [tag-name]` 的方式来验证已签署标签。
```
$ git tag -v v1.4.2.1
object 883653babd8ee7ea23e6a5c392bb739348b1eb61
type commit
tag v1.4.2.1
tagger Junio C Hamano <junkio@cox.net> 1158138501 -0700

GIT 1.4.2.1

Minor fixes since 1.4.2, including git-mv and git-http with alternates.
gpg: Signature made Wed Sep 13 02:08:25 2006 PDT using DSA key ID F3119B9A
gpg: Good signature from "Junio C Hamano <junkio@cox.net>"
gpg:                 aka "[jpeg image of size 1513]"
Primary key fingerprint: 3565 2A26 2040 E066 C9A7  4A7D C0C6 D9A4 F311 9B9A
```

### 后期加注标签

你可以在后期对早期提交打上标签，比如
```
$ git log --pretty=oneline
15027957951b64cf874c3557a0f3547bd83b3ff6 Merge branch 'experiment'
a6b4c97498bd301d84096da251c98a07c7723e65 beginning write support
0d52aaab4479697da7686c15f77a3d64d9165190 one more thing
6d52a271eda8725415634dd79daabbc4d9b6008e Merge branch 'experiment'
0b7434d86859cc7b8c3d5e1dddfed66ff742fcbc added a commit function
4682c3261057305bdd616e23b64b0857d832627b added a todo file
166ae0c4d3f420721acbb115cc33848dfcc2121a started write support
9fceb02d0ae598e95dc970b74767f19372d61af8 updated rakefile
964f16d36dfccde844893cac5b347e7b3d44abbc commit the todo
8a5cbc430f1a9c3d00faaeffd07798508422908a updated readme
```

忘记在提交 'update rakefile' 后打上版本号 v1.2。没关系，只需要在打标签的时候跟上对应对象的校验和（或者前几位）即可：
```
$ git tag -a v1.2 9fceb02
```


### 分享标签

默认情况下， `git push` 并不会把标签传送到远端服务器，只有通过显示命令才能分享标签，比如 `git push origin [tagname]` 即可。

```
$ git push origin v1.5
Counting objects: 50, done.
Compressing objects: 100% (38/38), done.
Writing objects: 100% (44/44), 4.56 KiB, done.
Total 44 (delta 18), reused 8 (delta 1)
To git@github.com:schacon/simplegit.git
* [new tag]         v1.5 -> v1.5
```

如果需要一次推送所有标签，可以使用 `--tags` 选项
```
$ git push origin --tags
Counting objects: 50, done.
Compressing objects: 100% (38/38), done.
Writing objects: 100% (44/44), 4.56 KiB, done.
Total 44 (delta 18), reused 8 (delta 1)
To git@github.com:schacon/simplegit.git
 * [new tag]         v0.1 -> v0.1
 * [new tag]         v1.2 -> v1.2
 * [new tag]         v1.4 -> v1.4
 * [new tag]         v1.4-lw -> v1.4-lw
 * [new tag]         v1.5 -> v1.5
```

在 `Github` 里可以从 `release

## 技巧和敲门

### Git命令别名

你想偷懒少输几个字符，可以使用 `Git config` 为命令设置别名：
```
$ git config --global alias.co checkout
$ git config --global alias.br branch
$ git config --global alias.ci commit
$ git config --global alias.st status
```
现在你要输入 `git commit` 时只需要输入 `git ci` 即可。

你甚至可以创造出新的命令
```
$ git config --global alias.unstage 'reset HEAD --'
```
这样一来下面命令完全相同：
```
$ git unstage fileA
$ git reset HEAD fileA
```

# Git 分支

Git 分支管理的轻便让他在一众版本控制系统中脱颖而出。

在 Git 提交时，会保存一个提交（commit）对象，它包含一个指向暂存内容快照的指针，包含本次提交的作者等相关附属信息，包含零个或多个指向该提交对象的父对象指针：首次提交没有直接祖先，普通提交有一个祖先，有两个或者多个分支合并的提交有多个祖先。

+ commit 对象：存储 tree 对象，以及其他提交元数据（作者，提交者等）。
+ tree 对象：存储 blob 对象，一个 blob 对象对应一个校验和。

+ blob 对象：文件快照内容。

仓库中各个对象保存的数据和相互关系看起像如图 3-1

![avator](../../pic/progit-data-struction.png)

commit 对象会包含一个指向上次提交的指针。

![avator](../../pic/progit-commit-parent.png)

分支其实就是一个默认指向最新 commit 的指针，Git 会使用 master 作为分支的默认名字。

![avator](../../pic/progit-commit-branch.png)

Git 新建分支可以使用 `git branch` 命令。
```shell
git branch testing
```

这会在当前 commit 对象上新建一个分支指针。

![avator](../../pic/progit-add-branch.png)

Git 通过一个叫 `HEAD` 的特殊指针，来告诉你你目前在哪个分支工作。如果你仅仅只是新建了分支，Git 不会把你的当前的工作目录切换成分支，你依然在 master 分支工作。
gitp

![avator](../../pic/progit-still-in-master.png)

使用 `git checkout` 命令切换分支
```
git checkout testing
```

切换到 testing 分支之后进行一次提交，那么历史记录看上去会是这样

![avator](../../pic/progit-commit-on-testing.png)

我们会到 master 分支，作出修改后提交，然后我们的提交历史就出现了分叉。

![avator](../../pic/progit-diff-branch.png)

也就是说切换分支的操作，只需要 `git checkout` 和 `git brance` 就可以完成。


与别的版本控制系统不同的是，Git 的分支实际上仅仅是一个包含了所指对象校验和（40 个字符长度 SHA-1 字串）的文件，所以创建和销毁分支操作十分简单

## 分支的新建与合并

比如一个已经上线的项目，你需要更新一些新的需求，你可以新建一个分支，在需求通过测试之后，合并回主分支。

### 分支的切换与新建

假设我们在完成一个项目，做了几次提交

![avator](../../pic/pro-git-little-commit.png)

现在你需要修补 #53 的问题，要新建并切换到该分支
```
git checkout -b iss53
```

上述命令相当于执行下面俩个命令
```
git branch iss53
git checkout iss53
```

![avator](../../pic/porgit-branch-iss53.png)

当你在 `iss53` 分支干的热火朝天的时候，你老板打电话来让你紧急修复一下 `master` 分支上的某个 bug。

因此我们要先切换到 `master` 分支，再运行
```
git checkout -b hoxift
```
在进行快速修复之后，你提交了记录

![avator](../../pic/progit-commit-on-hotfix.png)

之后你需要将其合并到 `master` 分支，并发布到服务器，使用 `git merge` 命令来进行合并
```
$ git checkout master
$ git merge hotfix
Updating f42c576..3a0874c
Fast-forward
 README | 1 -
 1 file changed, 1 deletion(-)
```

注意合并的时候出现了 "Fast forward" 提示，由于当前 `master` 分支所在的提交对象是要并入 `hotfix` 分支的上游，Git 只需要把 `master` 分支指针直接右移。

如果可以直接顺着一个分支走到达另一个分支的话，Git 在合并二者时，就会简单的把指针右移，因为这种单线的历史分支不要解决任何分歧，这种操作就被称为**快进 （Fast forward）**。

合并后历史记录变成了这样

![avator](../../pic/progit-merge-hotfix.png)


`hotfix` 已经完成了它的使命，你可以将他删除了，使用 `git branch -d` 选项删除。

```
$ git branch -d hotfix
Deleted branch hotfix (was 3a0874c).
```

![avator](../../pic/progit-finish-del.png)

现在 `hotfix` 的修改内容还未包含到 `iss53` 中，你可以使用 `git merge master` 把分支合并到 `iss53`

### 分支的合并

当你完成 `iss53` 的工作之后，你需要将其合并到 `master`,只需要回到 `master` 分支，运行 `git merge` 命令指定要合并的分支。

```
$ git checkout master
$ git merge iss53
Auto-merging README
Merge made by the 'recursive' strategy.
 README | 1 +
 1 file changed, 1 insertion(+)
```

这次合并操作的底层实现有别于之前 `hotfix` 的并入方式。

由于当前的 `master` 并非 hotfix 的祖先，所以 Git 需要找到他们的共同祖先进行三方合并计算。

![avator](../../pic/progit-find-ancestor.png)

Git 会为分支合并自动识别出最佳的同源合并点。

在合并成功之后，提交记录变成这样，Git 自动创建并包含了合并结果的提交对象 C6，它比较特殊，拥有两个祖先。

![avator](../../pic/progit-two-ancetors.png)

### 遇到冲突时的分之合并

如果你在 hotfix 和 master 中都修改了同一文件的同一部分，那么合并冲突就没按么简单了，你会得到类似下面结果：
```shell
$ git merge iss53
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```
Git 做了合并但没有提交，他在等你解决冲突，如果你想查看哪些文件冲突，使用 `git status`

```
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")

Unmerged paths:
  (use "git add <file>..." to mark resolution)

        both modified:      index.html

no changes added to commit (use "git add" and/or "git commit -a")
```

任何包含未解决冲突的文件都会以 **未合并（unmerged）** 的状态列
出。
```python
<<<<<<< HEAD
<div id="footer">contact : email.support@github.com</div>
=======
<div id="footer">
  please contact us at support@github.com
</div>
>>>>>>> iss53
```

使用 `=======` 隔开的上半部，就是当前分支，即 `HEAD` 所在。下面是你想要合并分支的内容。

你需要进行二选一，或者修改其中之一。

## 分支的管理

使用 `git branch` 不添加任何参数，会列出所有分支的清单
```
$ git branch
  iss53
* master
  testing
```
带 * 字符表示当前所在分支。

使用参数 `-v` 查看各分支最后一次提交信息，运行 `git branch -v`
```
$ git branch -v
  iss53   93b412c fix javascript issue
* master  7a98805 Merge branch 'iss53'
  testing 782fd34 add scott to the author list in the readmes
```

你可以使用 `--merged` 和 `--no-merged` 选项进行分支的筛选，比如查看已经被并入当前分支的分支
```
$git branch --merged
iss53
* master
```

如果你想强制删除那些未被合并的分支，使用 `-D` 参数强制删除。
```
$ git branch -D testing
```

## 利用分支进行开发的工作流程

### 长期分支

许多使用 Git 的开发者都喜欢用这种方式来开展工作，比如仅在 master 分支中保留完全稳定的代码，即已经发布或即将发布的代码。与此同时，他们还有一个名为 develop 或 next 的平行分支，专门用于后续的开发，或仅用于稳定性测试 — 当然并不是说一定要绝对稳定，不过一旦进入某种稳定状态，便可以把它合并到 master 里。这样，在确保这些已完成的特性分支（短期分支，比如之前的 iss53 分支）能够通过所有测试，并且不会引入更多错误之后，就可以并到主干分支中，等待下一次的发布。

![avator](../../pic/progit-long-branch.png)

使用流水线可能可以更好理解

![avator](../../pic/progit-long-branch-waterflow.png)

### 特性分支

在任何规模的项目中都可以使用特性（Topic）分支。一个特性分支是指一个短期的，用来实现单一特性或与其相关工作的分支。可能你在以前的版本控制系统里从未做过类似这样的事情，因为通常创建与合并分支消耗太大。然而在 Git 中，一天之内建立、使用、合并再删除多个分支是常见的事。

![avator](../../pic/progit-topic-branch.png)

## 远程分支

远程分支存储在远程仓库中，一般使用 (`远程仓库名/分支名`)这样的形式表示远程分支。
当你进行克隆的时候，默认把远程仓库的 `master` 分支和你本地 ``master` 分支关联。

![avator](../../pic/progit-git-clone.png)

可以使用 `git fetch origin` 来同步远程服务器上的数据到本地。

![avator](../../pic/progit-git-fecth-origin.png)

### 推送本地分支

如果你需要有一个分支和他人一起开发，可以运行 `git push (远程仓库名)（分支名）`

```
$ git push origin serverfix
Counting objects: 20, done.
Compressing objects: 100% (14/14), done.
Writing objects: 100% (15/15), 1.74 KiB, done.
Total 15 (delta 5), reused 0 (delta 0)
To git@github.com:schacon/simplegit.git
 * [new branch]      serverfix -> serverfix
```
实际上这里走了一点捷径，Git 自动吧 `serverfix` 分支名扩展为 
`ref/heads/serverfix:refs/heads/serverfix`，意为“取出我本地的 serverfix 分支，推送到远程仓库的 serverfix 分支中去”。

你也可以使用 `git push origin serverfix:serverfix` 来实现相同效果，意为“上传我本地的 serverfix 分支到远程仓库中，仍叫他 serverfix 分支”。因此，如果你想把远程分支叫做 `awesomebranch` 可以使用 `git push origin serverfix:aswesomebranch` 来推送数据。

这样其他开发者再次从服务器上获得数据的实时，他们将得到一个新的远程分支 `origin/serverfix`。并指向服务器上的 `serverfix`。
```
$ git fetch origin
remote: Counting objects: 20, done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 15 (delta 5), reused 0 (delta 0)
Unpacking objects: 100% (15/15), done.
From git@github.com:schacon/simplegit
 * [new branch]      serverfix    -> origin/serverfix
```

需要注意的是，你无法在本地编辑该分支，你需要将该远程分支合并到当前分支或者分化一个新分支来进行开发。

合并到当前分支
```
git merge origin/serverfix
```
分化新分支
```
git checkout -b serverfix origin/serverfix
```

### 跟踪远程分支

从远程分支里 `checkout` 出来的本地分支，称为 **跟踪分支（tracking branch）**。在追踪分支里输入 `git push`，Git 会自行判断应该向哪个服务器的哪个分支推送数据。


当你进行克隆的时候，默认把远程仓库的 `master` 分支和你本地 ``master` 分支关联。这就是为什么一开始 `git pull` 和 `git push` 就能使用的原因。

如果你有 1.6.2 以上版本的 Git，还可以使用 `--track` 选项简化
```
$ git checkout --track origin/serverfix
Branch serverfix set up to track remote branch serverfix from origin.
Switched to a new branch 'serverfix'
```

要为本地分支设定不同于远程分支的名字，只需要在第一个版本的命令里换个名字
```
$ git checkout -b sf origin/serverfix
Branch sf set up to track remote branch serverfix from origin.
Switched to a new branch 'sf'
```

现在你的本地分支 `sf` 会自动将推送和抓取数据的位置定位到 `origin/serverfix` 了。

### 删除远程分支

非常无厘头的命令来删除远程分支
```
git push origin :serverfix
```

有种方便记忆这条命令的方法：记住我们不久前见过的 git push [远程名] [本地分支]:[远程分支] 语法，如果省略 [本地分支]，那就等于是在说“在这里提取空白然后把它变成[远程分支]”。

## 分支的衍合

把一个分支的修改整合到另一个分支的方法有两种：`merge` 和 `rebase`（暂时翻译为“衍合”）


### 基本的衍合操作

当我们有俩个不同分支时

![avator](../../pic/progit-reabase-show.png)

最容易的整合方式是 `merge`，他会把两个分支最新的快照以及二者的共同祖先进行三方合并，产生一个新的提交对象（C5）

![avator](../../pic/progit-rebase-merge.png)

其实还有另一种选择，你把在 C3 里的变化补丁在 C4 的基础上重新再打一遍，这就叫做 衍合（rebase），这样可以把一个分支里的提交改变移到另一个分支里重放一遍。

上述例子运行
```
$ git checkout experiment
$ git rebase master
First, rewinding head to replay your work on top of it...
Applying: added staged command
```

其原理的回到两个分支的共同祖先，根据需要衍合的分支生成一系列补丁，然后以基地分支最后一个提交对象为新出发点，逐个应用之前准备好的补丁，最后生成一个新的合并提交对象 C3，改写 `experiment` 的提交记录，使它成为 `master` 的直接下游。

![avator](../../pic/progit-show-rebase.png)

衍合的目的可以让远程仓库拥有一个比较整洁的提交历史

### 有趣的衍合

衍合也可以放到其他分支进行，并不一定非得根据分化之前的分支。

![avator](../../pic/progit-client-server.png)

你想把 client 分支合并会主分支，但是 server 分支还有待测试，那么你可以通过 `git rebase` 的 `--onto` 指定基底分支 `master`。

```
$ git rebase --onto master server client
```

这好比再说 “取出 client 分支，找出 server 和 client 分支共同祖先之后的变化，把他们在 master 重现一遍”。

![avator](../../pic/progit-rebase-client.png)

现在只需要快进 `master` 分支即可
```
$ git checkout master
$ git merge client
```

![avator](../../pic/progit-fast-master.png)


现在决定把 `server` 分支的变化也包含进来，我们可以直接把 `server` 分支衍合到 `master`，而不用手动切换到 `server` 再继续衍合，`git rebase [主分支] [特性分支]`会先取出特性分支，在主分支上重演。
```
$ git rebase master server
```

![avator](../../pic/progit-rebase-server.png)

然后就可以快进 `master`，再删除 `client` 和 `server` 分支。

### 衍合的风险

**一旦分支中的提交对象发布到公共仓库，就千万不要对该分支进行操作！！**

在进行衍合的时候，实际上抛弃了一些现存的提交对象而创造了一些类似但不同的新的提交对象。如果你把原来分支中的提交对象发布出去，并且其他人更新下载后在其基础上开展工作，而稍后你又用 git rebase 抛弃这些提交对象，把新的重演后的提交对象发布出去的话，你的合作者就不得不重新合并他们的工作，这样当你再次从他们那里获取内容时，提交历史就会变得一团糟。

如果有人的修改是基于你的分支，而你把这些分支进行 `rebase` 之后，他们就不得不重新进行一次 `merge` 操作，以为 `reabse` 虽然有类似的结构，但是 SHA-1 校验值完全不同。

## 服务器上的Git

### 协议

Git 可以使用四种主要协议来传输数据：本地传输、SSH 协议、Git 协议 和 HTTP 协议，除了 HTTP 协议之外，其他协议都要求在服务器安装并运行 Git。

### 本地协议

本地协议就是远程仓库在硬盘的另一个目录，你可以通过
```
$ git clone /opt/git/project.git
```
或者这样
```
$ git clone file:///opt/git/project.git
```
如果你只给出路径，那么 Git 会尝试使用硬连接或者直接复制它所需要的文件。如果使用 file://，Git 会调用它平时通过网络来传输数据的供需，其效率较低。

### SSH协议
因为大多数环境以及支持通过 SSH 对服务器的访问，如果没有那么架设一个也十分容易，并且 SSH 是唯一一个同时支持读写的网络协议。SSH 同时也是一个验证授权的网络协议。

你可以这样通过 SSH 克隆一个仓库
```
$ git clone ssh://user@server/project.git
```
如果不指名协议，Git 会默认使用 SSH
```
$ git clone user@server:project.git
```
不指名用户，Git 会默认使用当前登录的用户名连接服务器。

#### 优点

+ 可以读写
+ 架构简单
+ 传输前会尽可能压缩数据

#### 缺点

+ 不能实现匿名访问，不适合开源项目


### Git协议
Git 协议是包含在 Git 软件包中的特殊守护进程，他会监听一个提供类似于 SSH 服务的特定端口（9418），而不需任何授权，要支持 Git 协议的仓库，你需要创建 git-daemon-export-ok 文件，他是协议进程提供仓库服务的必要条件。要么所有人都能克隆或推送，要么所有人都不能。

#### 优点
传输最快的协议

#### 缺点

缺少授权机制，如果一个项目只有 Git 协议是不可取得，一般来说是同时提供 SSH 接口，让几个开发者拥有推送权限，而其他人则只能通过 `git://` 读取

架构起来比较难，同时要求防火墙开放 9418 端口。

### HTTP/S 协议

HTTP 和 HTTPS 协议的优美在于，只需要能访问服务器的web服务的用户就可以进行克隆操作。只需要把 Git 的裸库文件放在 HTTP 根目录下，配置一个特定的 `post-update` 挂钩即可。

HTTP 协议也可以用来推送，但这种做法不常见。


#### 优点

+ 易于架构
+ 端口很常见，不会封锁
+ 占用资源很小

#### 缺点

+ 传输开销大，速度慢
+ 没有服务端的动态计算--因此 HTTP 协议经常被称为傻瓜（dumb）协议。


## 生成 SSH 公钥

大多数 Git 服务器都是要 SSH 公钥进行授权，SSH 公钥默认存储在主目录下的 `~/.ssh` 目录。

`~/.ssh/something` 为私钥

`~/.ssh/something.pub` 为公钥

如果没有 `~/.ssh` 目录，可以通过 `ssh-keygen` 生成一个。

你只需要把 `.pub` 文件的内容发送给管理员。

同时你可以在多个操作系统设定相同的 SSH 公钥，教程在
```
http://github.com/guides/providing-your-ssh-key。
```
## 架设服务器


在服务器新建一个账户，并且创建 `~/.ssh` 目录
```
$ sudo adduser git
$ su git
$ cd
$ mkdir .ssh
```
然后你只需要把开发者的 SSH 公钥添加到这个用户的 `authorized_keys` 文件中，就可以实现不需要密码的 SSH 通信

只需要把他们逐个加入 `authorized_keys` 文件尾部即可
```
$ cat /tmp/id_rsa.john.pub >> ~/.ssh/authorized_keys
$ cat /tmp/id_rsa.josie.pub >> ~/.ssh/authorized_keys
$ cat /tmp/id_rsa.jessica.pub >> ~/.ssh/authorized_keys
```

开发者就可以通过如下操作进行开发

```
# 在 John 的电脑上
$ cd myproject
$ git init
$ git add .
$ git commit -m 'initial commit'
$ git remote add origin git@gitserver:/opt/git/project.git
$ git push origin master
```

如果你想现在开发者只能使用 git 账号登录的 shell ，你可以使用 Git 自带的工具。
```
$sudo vim /etc/passwd
```
上面那个文件应该是管理不同工具使用的命令行工具的

在文末你可以找到
```
git:x:1000:1000::/home/git:/bin/sh
```

把 `bin/sh` 改成 `/user/bin/git-shell` 或者使用 `which git-shell` 
```
git:x:1000:1000::/home/git:/usr/bin/git-shell
```
这样 git 用户只能用 SSH 连接来推送和获取 Git 仓库，尝试普通连接会被拒绝。

```
$ ssh git@gitserver
fatal: What do you think I am? A shell?
Connection to gitserver closed.
```

## 公共访问

那么该如何实现匿名化的读取呢，对于小型配置来说最简单的就是运行一个静态 web 服务，把其根目录设定为 Git 仓库所在的位置，然后使用 `post-update` 挂钩，我们用 Apache 服务器做例子。

首先开启挂钩
```
$ cd project.git
$ mv hooks/post-update.sample hooks/post-update
$ chmod a+x hooks/post-update
```

`post-update` 大概作用就是，当通过 SSH 向服务器推送时，Git 将运行这个 `git-update-server-info` 命令来匿名更新 HTTP 访问获得数据时所需要的文件。

再在 Apache 服务器上配置一下请求即可。

然后需要把 `git` 根目录的 Unix 用户组设置为 `www-data`，这样 web 服务才能读取仓库内容，因为运行 CGI 脚本的 Apache 实例进程默认以用户身份
```
$ chgrp -R www-data /opt/git
```

重启之后就可以通过项目 URL 进行克隆了
```
$ git clone http://git.gitserver/project.git
```

## Gitosis

把所有用户的公钥保存在 `authorized_keys` 文件的做法，并不适合大型项目，同时该做法还缺少必要的管理权限-每个人都对项目有完整的读写权限。

我们可以使用 Gitosis 进行账户管理，确实它是通过一个特殊的 Git 仓库来管理的。


# Git 工具

### 简短的SHA

Git 很聪明，你只需要提供的 SHA-1 不少于 4 个字符并且是唯一的，Git 就能帮你找到他。

下面的命令是等价的
```
$ git show 1c002dd4b536e7479fe34593e72e6c6c1819e53b
$ git show 1c002dd4b536e7479f
$ git show 1c002d
```

### 分支引用

如果你想看到分支指向哪个具体的 SHA ，就可以使用 `rev-parse` ，注意这个工具是为底层设计的。
```
$ git rev-parse topic
ca82a6dff817ec66f44342007202690a93763949
```

### 引用日志的简称

在你工作的时候， Git 在后台的工作之一就是保存一份引用日志，记录你几个月（可能是90天）的 HEAD 和分支引用的日志。

你可以使用 `git relog` 来查看

```
$ git reflog
734713b... HEAD@{0}: commit: fixed refs handling, added gc auto, updated
d921970... HEAD@{1}: merge phedders/rdocs: Merge made by recursive.
1c002dd... HEAD@{2}: commit: added some blame and merge stuff
1c36188... HEAD@{3}: rebase -i (squash): updating HEAD
95df984... HEAD@{4}: commit: # This is a combination of two commits.
1c36188... HEAD@{5}: rebase -i (squash): updating HEAD
7e05da5... HEAD@{6}: rebase -i (pick): updating HEAD
```

你可以使用 `@{n}` 语法，来指定引用

比如查看引用日志的前五次值
```
$ git show HEAD@{5}
```

你也可以使用这个语法来查看某个分支在一定时间前的位置，比如查看昨天的 `master` 分支在哪
```
$ git show master@{yesterday}
```
**引用日志信息只存于本地**！

## 祖先引用

你可以在引用后面加上一个 `^` 来查看此次提交的父提交。

比如，你想查看上一次提交的父提交

```
$ git show HEAD^
```

你甚至可以在 `^` 后面加一个数字，比如 `d921970^2`，意思是 d921970 的第二次父提交。这种情况只有在合并的时候有用，因为只有在合并的时候会有多个父提交。

```
$ git show d921970^
commit 1c002dd4b536e7479fe34593e72e6c6c1819e53b
Author: Scott Chacon <schacon@gmail.com>
Date:   Thu Dec 11 14:58:32 2008 -0800

    added some blame and merge stuff

$ git show d921970^2
commit 35cfb2b795a55793d7cc56a6cc2060b4bb732548
Author: Paul Hedderly <paul+git@mjr.org>
Date:   Wed Dec 10 22:22:03 2008 +0000

    Some rdoc changes
```

另一个指明父祖先的方法是 `~`，也是默认指向第一父提交。但当你指定数字时会和 `^` 有不一样的表现。 `HEAD~2` 指 “第一父提交的第一父提交”，也就是祖父提交。

### 提交范围
如果你想查哪些分支的工作我还没有合并到主分支的，需要查看一些问题。

#### 双点
主要让 Git 区分出可以从一个分支中获得而不能从另一个分支中获得的提交。例如你有如下提交历史。

![avator](../../pic/progit-doubleclick.png)

您可以使用 `master..experiment` 来让 Git 显示这些提交的日志。这句话的意思就是“所有可以从 exeriment 分支中获得而不能从 master 分支中获得的提交”

```
$ git log master..experiment
D
C
```

下面这条命令可以查看你将把模式提艾到远程仓库：
```
$ git log origin/master..HEAD
```
该命令的含义是显示你在当前分支而不再远程 `origin` 上的提交，你可以使用 `git log origin/masetr..` 得到相同效果。

#### 多点

你可以查看某些提交被包含在某些分支，但是不包含在你当前分支的情况。Git 允许你使用 `^` 字符或者 `--not` 指明你不希望提交被包含其中的分支。

下面三个命令是等同的
```
$ git log refA..refB
$ git log ^refA refB
$ git log refB --not refA
```

同时它允许多个分支比较，比如 `refA` 或 `refB` 包含但是不被 `refC` 包含。
```
$ git log refA refB ^refC
$ git log refA refB --not refC
```

#### 三点

你可以使用该语法指定被两个引用的一个包含但又不被两者同时包含的分支
```python
master and experimnet == Fasle
amster or experment == True
```
大概就是上面👆这个意思
```
$ git log master...experiment
F
E
D
C
```

你可以加上 `--left-right` 来看每个提交到底在哪一侧分支
```
$ git log --left-right master...experiment
< F
< E
> D
> C
```