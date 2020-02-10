远程办公的时候公司需要使用 svn 的钩子功能进行一个 web 服务器的自动更新

## 需求
确定 svn 仓库位置

web 服务器位置

并且由于 svn 仓库中又很多项目，需要对用户输入进行一个简单的甄别


## 遇到的坑

首先最坑爹的，svn hook 的默认目录居然不是当前目录，而是根目录！

其次 svn 的中文编码问题，虽然我在代码中配置了相关编码，但是 svn 执行的时候还是有问题。需要在命令行前面强制加上环境变量。

## 代码
```python
def main(argv):
    repo = argv[1]
    rev = argv[2]
    changed_command = f'svnlook dirs-changed {repo}'
    author_command = f'svnlook author -r {rev} {repo}'
    log_command = f'env LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 svnlook log {repo}'
    stdout = subprocess.check_output(changed_command.split(' ')).decode('utf-8').strip()
    author = subprocess.check_output(author_command.split(' ')).decode('utf-8').strip()
    log = subprocess.check_output(log_command.split(' ')).decode('utf-8').strip()
    stdout_list = stdout.split('\n')
    for s in stdout_list:
        #目录判断
        if s.startswith('pneumonia/client/'):
            os.chdir('/home/web_sh/web_dev/httpd/www/test')
            up_command = 'svn up'
            subprocess.check_output(up_command.split(' ')).decode('utf-8').strip()
            print(f' {author} commit pneumonia/client/ {rev} auto update sucessfully')
            send_msg(author, log)
            break
if __name__ == '__main__':
    #默认工作目录居然为根目录   
    work_dir = sys.path[0]
    os.chdir(work_dir)
    main(sys.argv)
    sys.exit(0)

```