做了一个简单的天气爬虫想要放到 Liunx 服务器上去

使用 `crontab` 即可

### 操作级别

+ crontab -e: 用户级，不能设置用户字段
+ /etc/crontab: 系统级，只能root用户权限使用，需要设置用户字段


我这个任务只需要简单的

```
crontab -e
```
然后在新建文件中添加定时任务，比如每周一三点执行 Python脚本
```
0 3 * * 1 python /data/www/test.py
```

`wq` 保存就行

时间设置语法为：
```
# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * command to be executed

```

如果你想看那你有哪些定时任务，可以使用 `crontab -l` 命令。

再增加了 `crontab` 任务之后，在 `var/spool/cron` 目录下会有一个当前**登录账号命名**的文件，该文件内容就是添加的 `crontab` 任务。
```
$ cat /var/spool/cron/root 
*/1 * * * * /dd/shell/test1.sh
*/1 * * * * /dd/shell/test2.sh
```
你可以手动修改文件内容，进行定时任务的修改或者删除

也可以使用 `sed` 命令来处理该文件，比如删除含有 `test2.sh` 的行的内容
```
$ sed -i 'test2.sh/d' /var/spool/cron/root 
```
删除crontab内容空白行

在执行上述命令之后，你会发现 `crontab -l` 多处一行空白，如果你想删除它，执行 
```
$ sed -i '/^$/d' /var/spool/cron/root
```