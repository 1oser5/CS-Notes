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