**写在前面的话**
&emsp;&emsp;写文档其实比敲代码要累，需要组织文章结构，需要想清楚说什么，怎么去表达，这是我最不擅长的事情，但还是想要做这件事情，不擅长的事情才更有挑战，才更想尝试去做，看看自己能做到什么程度。今天是个小任务，顺便写个文档练练手。
**任务内容**：封装一个通用的ini文件操作类
**测试环境**：win7+Python3
#### 1.什么是ini
>INI是英文“初始化”（initialization）的缩写，被用来对操作系统或特定程序初始化或进行参数设置。以节(section)和键(key)构成。

**ini文件格式**
节(section) 用方括号括起来，单独占一行
键(key)用等号连接键名和键值，单独占一行
注释(comment)使用英文分号（;）开头，单独占一行。在分号后面的文字，直到该行结尾都为注释
eg：
```
[mysql]
;host
host=127.0.0.1
;port
port=3306
```
#### 2.需求梳理
&emsp;&emsp;拿到任务先梳理一下需求，对INI文件应用场景，一般都是用于做初始化配置文件用的。想了想平时对配置文件的使用，基本都是相同内容会放置同一section内，然后多个内容设置多个section，用的时候会使用同一section下的配置，so，需要完成的需求为：读取某一section下的全部数据。（后期使用如果还需要其他功能再添加方法）
#### 3.类的设计
根据2中需求进行类设计:
![](http://upload-images.jianshu.io/upload_images/3971728-9c50bed4d14774e1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
**tips:**
* 使用Python标准模块ConfigParser提供的ConfigParser类操作；
* 注意异常情况的捕获
#### 4.测试一下
######4.1 创建readini.ini文件，添加内容如下：
```
[addsection]
option1 = value1
option2 = value2

[addsection1]
option3 = value3
```
######4.2  先用正确用例测试一下(get_conf_data为获取的方法名)
```python
path  = "readini.ini"
conf = iniconf(path)
print(conf.get_conf_data("addsection"))
print(conf.get_conf_data("addsection1"))
```
运行结果：
![](http://upload-images.jianshu.io/upload_images/3971728-ef6d13b947585154.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
######4.3 使用异常用例试试
**文件不存在**（以下均以4.2中代码为对比修改）
```
 path  = "readini1.ini"
```
运行结果
![](http://upload-images.jianshu.io/upload_images/3971728-88e6d01bb03dcd62.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
**section不存在**
```python
print(conf.get_conf_data("addsection3"))
```
运行结果：
![](http://upload-images.jianshu.io/upload_images/3971728-a7529e18c6f72e28.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### 4.结束语
&emsp;&emsp;一个简单的小任务就完成啦，又学习到一些Markdown的语法，感觉简书对Markdown支持的还不是很好啊。