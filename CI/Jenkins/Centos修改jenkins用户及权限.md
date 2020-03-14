## 原因
需要运行在 root 目录下的文件，jenkins 默认用户权限不足

## 过程

Open up the this script (using VIM or other editor):
```
vim /etc/sysconfig/jenkins
```

Find this `$JENKINS_USER` and change to `“root”`:
```
$JENKINS_USER="root"
```
Then change the ownership of Jenkins home, webroot and logs:
```
chown -R root:root /var/lib/jenkins
chown -R root:root /var/cache/jenkins
chown -R root:root /var/log/jenkins
```
Restart Jenkins and check the user has been changed:
```
service jenkins restart
ps -ef | grep jenkins
```