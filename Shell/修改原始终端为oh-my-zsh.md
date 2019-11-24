zsh 是一个强大的 bash 替代，而 oh-my-zsh 是 zsh 的一个傻瓜化配置工具。


## 安装
在终端执行下面的语句安装Oh-My-ZSH
```
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

## 配置
设置默认的shell为Oh-My-ZSH
```
chsh -s /bin/zsh
```

### 安装过程如下

```

xxxx% sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" 
Cloning Oh My Zsh...
Cloning into '/Users/xxxx/.oh-my-zsh'...
remote: Counting objects: 831, done.
remote: Compressing objects: 100% (700/700), done.
remote: Total 831 (delta 14), reused 775 (delta 10), pack-reused 0
Receiving objects: 100% (831/831), 567.67 KiB | 75.00 KiB/s, done.
Resolving deltas: 100% (14/14), done.
Looking for an existing zsh config...
Found ~/.zshrc. Backing up to ~/.zshrc.pre-oh-my-zsh
Using the Oh My Zsh template file and adding it to ~/.zshrc
             __                                     __   
      ____  / /_     ____ ___  __  __   ____  _____/ /_  
     / __ \/ __ \   / __ `__ \/ / / /  /_  / / ___/ __ \ 
    / /_/ / / / /  / / / / / / /_/ /    / /_(__  ) / / / 
    \____/_/ /_/  /_/ /_/ /_/\__, /    /___/____/_/ /_/  
                            /____/                       ....is now installed!
Please look over the ~/.zshrc file to select plugins, themes, and options.
p.s. Follow us at https://twitter.com/ohmyzsh.
p.p.s. Get stickers and t-shirts at http://shop.planetargon.com.

```


## 配置

### 设置主题

设置固定主题
安装完毕后，我们就可以使用了，先来简单配置一下，Oh My Zsh 提供了很多主题风格，我们可以根据自己的喜好，设置主题风格

终端输入命令 
```
open ~/.zshrc
```

找到 ZSH_THEME ，ZSH_THEME="robbyrussell" ，robbyrussell ，是默认的主题，修改 ZSH_THEME="样式名称"
```
source ~/.zshrc
```
保存这个文件文件，重新打开终端。


### 高亮插件

下载
```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```
配置
```
vim ~/.zshrc
```
中加入插件的名字
```
plugins=( [plugins...] zsh-syntax-highlighting)

```
生效
```
source ~/.zshrc 
```
或是重启终端

### 自动补全

下载
```
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```
配置
```
vim ~/.zshrc
```
中加入插件的名字
```
plugins=( [plugins...] zsh-syntax-highlighting)
```
生效
```
source ~/.zshrc
```
 或是重启终端


## extract 解压缩

再也不用 Google 了，直接一键解压。

直接把 extract 加入 plugins 即可使用。

## autojump 智能跳转

linux 系统
```
$ git clone git://github.com/joelthelion/autojump.git
```

mac 系统
```
brew install autojump
```

切换到 autojump 目录
```
cd /autojump
```

运行
```
$ ./install.py
```
vim ~/.zshrc，把以下代码加到尾部
```
# 使用brew安装的

[[ -s $(brew --prefix)/etc/profile.d/autojump.sh ]] && . $(brew --prefix)/etc/profile.d/autojump.sh
source $ZSH/oh-my-zsh.sh

# 使用git安装的

[[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && . ~/.autojump/etc/profile.d/autojump.sh
```