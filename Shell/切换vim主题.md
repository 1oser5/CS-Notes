我在 Mac 系统下使用 vim 没有任何配色，白白的很单调，在修改一些配置文档的时候也没有语法高亮的提示，有时候使用起来没有在 Linux 下来得方便。

查看 vim 系统配色
```
ls /usr/share/vim/vim80/colors
```

设置自己的配色方案

在当前用户目录 ~/ 下的 .vim 目录(如果没有，mkdir ~/.vim进行新建该目录)。
```
mkdir ~/.vim
mkdir ./.vim/colors
```
在 ~/.vim/ 下新建一个叫 colors 的目录，我们下一步下载的配色方案.vim文件便放到该目录下。

到一个配色网站上选择一个配色方案下载到 ~/.vim/colors 目录下面。


然后个人文件夹下建立一个 vim 的配置文档
```
vim ~/.vimrc
```

配置文档中写入以下内容：
```
set nu                " 显示行号
colorscheme 你下载的主题    " 颜色显示方案
syntax on             " 打开语法高亮
```

也可以使用插件管理

下载 vim-colorschemes 插件
```
mkdir ~/.vim
git clone https://github.com/flazz/vim-colorschemes.git ~/.vim
```
后续还是需要配置 vim 个人文件，但是插件会提供大量的主题可供挑选。
121

