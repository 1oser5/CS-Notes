从Linux服务器下载文件夹到本地

使用scp命令


#把本地的source.txt文件拷贝到192.168.0.10机器上的/home/work目录下
```
scp /home/work/source.txt work@192.168.0.10:/home/work/
```

#把192.168.0.10机器上的source.txt文件拷贝到本地的/home/work目录下
```
scp work@192.168.0.10:/home/work/source.txt /home/work/
```


#把192.168.0.10机器上的source.txt文件拷贝到192.168.0.11机器的/home/work目录下
```
scp work@192.168.0.10:/home/work/source.txt work@192.168.0.11:/home/work/
````

#拷贝文件夹，加-r参数
```
scp -r /home/work/sourcedir work@192.168.0.10:/home/work/  
```