## 原因

因为这两天公司事情比较轻松，在看 Python3.8 新特性，并且自己动手试一下。但是我目电脑上的 Python 版本为 3.7.0。如果是修改环境变量来进行新特性使用，未免有些太麻烦了。所以调研一下有什么好的切换版本的方法。

## pyenv

### 相关原理

#### 理解PATH

当你运行比如 `python` 或者 `pip` 命令是，你的操作系统会查找一系列的文件夹来找到一个对应名称的可执行文件，这一系列文件夹在环境变量中被称作 `PATH`，每个文件夹都被 `:` 分开。
```
/usr/local/bin:/usr/bin:/bin
```
上述文件夹时从左到右搜索的，因此开始部分的会比在结尾部分的有更高的优先级，上面示例中 `/usr/local/bin` 会先被搜索。

#### 理解Shims

pyenv 通过在 `PATH` 最前面插入 `shims` 文件夹工作。
```
$(pyenv root)/shims:/usr/local/bin:/usr/bin:/bin
```
该过程被称为 `rehashing`，pyenv 通过 `shims` 来匹配每一个 `Python` 命令行。

shims 是这样工作的，当你输入 `pip`，你的操作系统将会：

+ 查找你的 PATH 来找到名叫 `pip` 的可执行文件
+ 显而易见 shims 里被叫做 `pip` 的会被找到
+ 运行该 `pip`，将命令传递给 pyenv

#### 选择 Python 版本
当你执行 shim 时，pyenv 通过以下源来确定运行哪个版本的 Python，顺序如下：

+ `PYENV_VERSION` 环境变量（你可以通过 `pyenv shell` 在当前 shell 进行设定）
+ 当前文件夹的 `.python-version` 文件（你可以使用 `pyenv local` 命令来设定）
+ 在父级文件夹中找到的第一个 `.python-version` 文件，搜索至你的根目录。
+ 全局 `$(pyenv root)/version` 文件（可以使用 `pyenv global` 命令设定，如果不存在，pyenv 会默认使用 `system` Python）

### 总结

总的来说，pyenv 就是通过把 shims 文件夹插入到 `PATH` 来劫持你的 python 命令，然后将命令传递到对应版本的 Python 中。

## 安装

### homebrew
遇事不决，Homebrew
```
brew install pyenv
```
但我发现 homebrew 安装的没有 python3.8 版本

需要换一种安装方式。

### pyenv-installer

还很贴心的提供了下载脚本
```
curl https://pyenv.run | bash
```
然后添加一下环境变量
```
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc
```
就可以了

### git

通过 `git clone` 下载
```
cd ~
git clone git://github.com/yyuu/pyenv.git .pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc
```
## 命令


相关命令

```
使用方式: pyenv <命令> [<参数>]

命令:
  commands    查看所有命令
  local       设置或显示本地的Python版本
  global      设置或显示全局Python版本
  shell       设置或显示shell指定的Python版本
  install     安装指定Python版本
  uninstall   卸载指定Python版本)
  version     显示当前的Python版本及其本地路径
  versions    查看所有已经安装的版本
  which       显示安装路径
```

