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
Pipe'li'ne 是一套插件，将持续交付的实现和实施集成到 Jenkins 中。

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

Jenkins 可以记录汇总测试结果，其通常和 junit步骤捆绑使用，一般写在 post 部分。

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

### 电子邮件
```python
post{
    failure{
        mail to:'team@example.com',
        subject:'Failed Pipeline:${currentBuild.fullDisplayName}",
        body:"Someting is wrong with ${env.BUILD_URL}"
    }
}
```

### Hipchat

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