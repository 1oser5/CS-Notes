# Spring-boot 注解大全

## @RestController

@RestController 注解 @Controller 和 @ResponseBody 的合集，属于 REST风格的控制器。

+ 类：表示该类都为 RESTFUL 接口
+ 方法：该方法为 RESTFUL

## @RequestMapping

@RequestMapping 提供了初步请求信息的映射。

### 属性

+ value: 请求路径， /project/login
+ method: 请求方法, POST/GET
+ consumes: 提交内容类型，application/json，text/html
+ produces：返回内容类型
+ params：只有请求中包含以上参数，才进行处理
+ headers：只有请求中包含指定 header值才进行处理

+ 类：该类中的所有请求方法都以该地址为父路径
+ 方法：如果该类已经定义了@RequestMapping，则为相对于父路径的路径，若未定则相对于WEB根路径

## @Autowired

自动导入对象到类中，被注入进的类同样要被 spring 容器管理，比如 Service 注入到 Controller 类中。