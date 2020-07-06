# 目录
+ [开始使用Jenkins](#开始使用Jenkins)
    + [准备工作](#准备工作)
    + [运行Jenkins](#运行Jenkins)
+ [创建第一个Pipeline](#创建第一个Pipeline)
    + [什么是JenkinsPipeline?](#什么是JenkinsPipeline?)
        + [Linux、BSD和MacOS](#Linux、BSD和MacOS)
+ [执行多个步骤](#执行多个步骤)
    + [超时、重试和更多](#超时、重试和更多)
    + [完成时动作](#完成时动作)
+ [定义执行环境](#定义执行环境)
+ [使用环境变量](#使用环境变量)
+ [记录测试和构建结果](#记录测试和构建结果)
+ [清理和通知](#清理和通知)
    + [电子邮件](#电子邮件)
    + [Hipchat](#Hipchat)
+ [Docker中使用Jenkins](#Docker中使用Jenkins)





# 开始使用 Jenkins
## 准备工作
机器要求：

+ 256 MB 内存，建议大于 512 MB
+ 10 GB 的硬盘空间（用于 Jenkins 和 Docker 镜像）

软件要求：

+ Java 8-11（开始没注意装成 java 13，不能运行。JRE 和 JDK 都可以）
+ Docker


## 运行 Jenkins

到指定目录运行

```
java -jar /Applications/Jenkins/jenkins.war
-- httpPort=8080
```

可以通过 httpPort 进行端口切换


# 创建第一个 Pipeline

## 什么是 Jenkins Pipeline?
Pipeline 是一套插件，将持续交付的实现和实施集成到 Jenkins 中。

Pipeline 的定义通常被写入到一个文本文件中（称为 Jenkinsfile），该文件可以被放入源代码控制库中。

整个打包过程都是通过 Jenkinsfile 来控制的。

### Linux、BSD 和 Mac OS

shell 命令对应 Pipeline 中的 一个 sh 步骤（step）。

```python
pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                    '''
            }
        }
    }
}

```

# 执行多个步骤
## 超时、重试和更多

Pipeline 提供多重步骤，可以相互组合嵌套，方便解决重复执行步骤直到成功（重试）和如果一个步骤执行花了太多时间则退出（超时）问题。

```python
pipeline{
    agent any
    stages{
        stage('Deploy'){
            steps{
                retry(3){
                    sh './flakey-deploy.sh'
                }

                timeout(time: 3, unit: 'MINUTES'){
                    sh './health-check.sh'
                }
            }
        }
    }
}

```

Deploy 阶段（stage） 重复执行 flakey-deploy.sh 脚本三次，然后等待 health-check.sh 脚本最长执行三分钟。如果其没有完成，就被标为失败。

## 完成时动作

Pipeline 运行完成时，你需要做一些清理工作或者根据处理结果进行不同操作，这些操作可以放在 post 部分完成。

```python
pipeline{
    agent any
    stages{
        stage('Deploy'){
            steps{
                retry(3){
                    sh './flakey-deploy.sh'
                }

                timeout(time: 3, unit: 'MINUTES'){
                    sh './health-check.sh'
                }
            }
        }
    }
    post{
        always{
            echo 'This will always run'
        }
        success{
            echo 'This will run only if successful'
        }
        failure{
            echo 'This will run only if failed'
        }
        unstable{
            echo 'This will run only if the run was marked as unstable'
        }
        changed{
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}

```

# 定义执行环境

agent 命令告诉 Jenkins 在哪里以及如何执行 Pipeline 或者 Pipeline 子集，所有的 Pipeline 都需要 agent 指令。

在执行引擎中， agent 指令会引起以下操作的执行：

+ 所在 block 中的 step 将被 Jenkins 放在一个执行队列中，一旦一个执行器 executor 是可用的，该执行器就会开始执行。
+ 分配一个 workspace，其中包含一些来自远程仓库的文件和用于 Pipeline 的文件。


# 使用环境变量

环境变量可以是全局的，也可以是 stage 级别的。

```python
pipeline{
    agent any

    environment{
        DISABLE_AUTH = 'true'
        DB_ENGINE = 'sqlite'
    }
}

```

定义环境变量的方法对于指令性的脚本定义非常有用，这样就可以在 Pipeline 中设置环境。

# 记录测试和构建结果

Jenkins 可以记录汇总测试结果，其通常和 junit 步骤捆绑使用，一般写在 post 部分。

```python
post{
    always{
        junit'build/reports/xxx.xml'
    }
}
```

这样获得测试结果，如果存在失败的测试用例，Pipeline 会被标记为 UNSTABLE ，在网页上用黄色表示，不同于用红色表示的 FAILED。


# 清理和通知

有多种方法可以发送通知

## 电子邮件
```python
post{
    failure{
        mail to:'team@example.com',
        subject:'Failed Pipeline:${currentBuild.fullDisplayName}",
        body:"Someting is wrong with ${env.BUILD_URL}"
    }
}
```

## Hipchat

```python
post{
    failure{
        hipchatSend message:"Attention @here ${env.JOB_NAME} #${env.BUILD_NUMBER} has failed",
        color: 'RED'
    }
}
```

这官方的入门看的一头雾水，看完还不知道 Jenkins 到底是干什么用的

后面在网上查了资料，感觉这人说的挺好的，链接贴在下面。

https://www.cnblogs.com/zz0412/p/jenkins01.html

Jenkins 主要用于：

+ 持续、自动的构建/测试软件项目
+ 监控定时执行任务


# Docker 中使用 Jenkins

首先需要运行 Docker，将 jenkinsci/blueocean 镜像下载下来

然后使用下面代码运行。

```python
docker run \
  --rm \
  -u root \
  -p 8080:8080 \
  -v jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$HOME":/home \
  jenkinsci/blueocean

```
发现之前用的 80 端口还在后台运行，然后尝试通过 kill 进程的方法关掉 Jenkins 后台程序。
结果发现关掉一个进程它就换一个进程号，最后通过关闭 Jenkins 服务才完成的，代码如下

启动\重启
```python

sudo launchctl load /Library/LaunchDaemons/org.jenkins-ci.plist

```
停止

```python

sudo launchctl unload /Library/LaunchDaemons/org.jenkins-ci.plist
```

还可以在url 加上 exit 后缀退出，前提是已登录状态下。

成功运行 docker 里 jenkins 之后，需要输入密码。

docker 中的 jenkins 和一般的不同，你在普通命令行中看不到密码信息，需要使用以下代码到 docker 中查看密码。

首先查看 docker 容器 ID
```python
docker ps -a
```
结果如下：
![avator](https://raw.githubusercontent.com/1oser5/CS-Notes/master/pic/dockerid.png)
红色标出的是对于的 ID 号。
之后获得相应 ID 的权限
```python
docker exec -u 0 -it 21ee4816aac1 /bin/bash
```
![avator](https://raw.githubusercontent.com/1oser5/CS-Notes/master/pic/docker&#32;exec.png)
-u 0 意味着是根权限。 -it 后面的根据你需要获取那个 ID 权限有关，对应即可。

最后在使用常规命令就可以得到密钥

```python
cat /var/jenkins_home/secrets/initialAdminPassword
```

经过一个周末忘记了 jenkins 的登陆密码 😂

可以通过修改 jenkins_home 中的 config.xml 来进行密码 reset

首先找到对应的 docker 容器，在进入 jenkins_home 文件夹，使用 vim 编辑器进行 config.xml

将
\<useSecurity>true\</useSecurity>  修改成  \<useSecurity>false\</useSecurity>即可，刷新网页，可以看到直接跳过登陆界面，进入 jenkins 主界面。

发现使用上述方法后，其将登录设置修改为可匿名登录，可能会影响安全性。以下操作重新配置账户

点击 左侧的 Manage Jenkins—>Configure Global Security进入如下界面：

（1）选中 “Enable security”；

         a.在Security Realm中 选中”Jenkins’ own user database“ 并勾选 “Allow users to sign up”

         b. 在 Authorization中，选择 “Matrix-based security”， 在 User/group to add 文本框中，输入admin，点击“Add”按钮，可以看到用户admin被添加到User/group表格中；

         c. 在User/group表格中，给admin选择所有权限。

![avator](https://raw.githubusercontent.com/1oser5/CS-Notes/master/pic/jenkins_pwd.jpeg)

介于上述问题，以后所有 jenkins 的账密都设置为 ：

账：xtl

密：123456

jenkins web 网页中英文切换需要使用到一个叫 local 的插件，下载完成后再系统设置中找到 local 选项，根据不同语言进行设置即可。

第一次按照教程克隆的时候出现无法启动问题
报错如下
```

java.io.FileNotFoundException

	at jenkins.plugins.git.GitSCMFile$3.invoke(GitSCMFile.java:173)

	at jenkins.plugins.git.GitSCMFile$3.invoke(GitSCMFile.java:165)

	at jenkins.plugins.git.GitSCMFileSystem$2.invoke(GitSCMFileSystem.java:190)

	at org.jenkinsci.plugins.gitclient.AbstractGitAPIImpl.withRepository(AbstractGitAPIImpl.java:29)

	at org.jenkinsci.plugins.gitclient.CliGitAPIImpl.withRepository(CliGitAPIImpl.java:78)

	at jenkins.plugins.git.GitSCMFileSystem.invoke(GitSCMFileSystem.java:186)

	at jenkins.plugins.git.GitSCMFile.content(GitSCMFile.java:165)

	at jenkins.scm.api.SCMFile.contentAsString(SCMFile.java:335)

	at org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition.create(CpsScmFlowDefinition.java:115)

	at org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition.create(CpsScmFlowDefinition.java:67)

	at org.jenkinsci.plugins.workflow.job.WorkflowRun.run(WorkflowRun.java:299)

	at hudson.model.ResourceController.execute(ResourceController.java:97)

	at hudson.model.Executor.run(Executor.java:429)

Finished: FAILURE
```

在 stackoverflow 查询后发现是因为 jenkinsfile 文件没在 git 根目录上。。。。
