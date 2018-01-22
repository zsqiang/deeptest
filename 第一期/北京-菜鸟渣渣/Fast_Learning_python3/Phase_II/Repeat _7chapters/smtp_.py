# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   Author :       Young
   Change Activity: 2018/1/21:
-------------------------------------------------
"""
import smtplib
from email.mime.multipart import MIMEMultipart

__author__ = 'Young'

'''
使用smtplib进行文本格式、HTML格式和带附件的邮件发送处理。

导入smtplib模块
import smtplib
关键函数说明
# 创建smtp对象
smtp = smtplib.SMTP([host [, port [, localhost]]] )

# 参数说明
# host： smtp服务地址，例如126邮箱的是：smtp.126.com
# port： smtp服务端口
# localhost： 如果你的smtp服务在本机，则只需指定localhost即可


# 发送邮件函数
SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])

# 参数说明
# from_addr： 邮件发送地址
# to_addrs： 邮件接收地址列表
# msg： 邮件内容
# mail_options, rcpt_options  可选参数，暂时不需要了解


'''
from email.mime.text import MIMEText
from email.header import Header

if __name__ == "__main__":
    print("发送文本邮件示例")

    # 邮件发送者
    sender = "zhzxweijing@126.com"

    # 邮件接收地址列表
    # 请将xxx改为你的126邮箱名或整个改为你的目标接收邮箱地址
    receivers = "zhzxweijing@126.com"

    # 发送内容构建
    # text标识发送内容为文本格式
    msg = MIMEText("微信公众号号：开源优测", "plain", "utf-8")
    msg["From"] = sender
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("开源优测_DeepTest", "utf-8")

    # smtp服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    # 发送人邮件用户名或专用于smtp账户用户名
    username = sender

    # 发送人邮件密码或专用于smtp账户的密码
    password = "weiye13469619523"

    # 构建smtp对象
    smtp = smtplib.SMTP()

    # 连接到smtp服务
    con = smtp.connect(smtpserver, smtpport)
    print("连接结果： ", con)

    # 登录smtp服务
    log = smtp.login(username, password)
    print("登录结果：", log)

    # 发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("邮件发送结果： ", res)

    # 退出
    smtp.quit()
    print("send email finish")

    # HTML格式邮件
    # 将文本格式邮件代码中的以下部分替换如下：
    '''
    # html标识发送内容为文本格式
msg = MIMEText("<p>微信公众号号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>>",
         "html", 
         "utf-8")
    '''


    
    print("发送HTML邮件示例")

    # 邮件发送者
    sender = "deep_test@126.com"

    # 邮件接收地址列表
    # 请将xxx改为你的126邮箱名或整个改为你的目标接收邮箱地址
    receivers = "xxx@126.com"

    # 发送内容构建
    # html标识发送内容为文本格式
    msg = MIMEText("<p>微信公众号号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>>",
                   "html",
                   "utf-8")
    msg["From"] = "deep_test@126.com"
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("开源优测_DeepTest", "utf-8")

    # smtp服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    # 发送人邮件用户名或专用于smtp账户用户名
    username = "deep_test"

    # 发送人邮件密码或专用于smtp账户的密码
    password = "123456a"

    # 构建smtp对象
    smtp = smtplib.SMTP()

    # 连接到smtp服务
    con = smtp.connect(smtpserver, smtpport)
    print("连接结果： ", con)

    # 登录smtp服务
    log = smtp.login(username, password)
    print("登录结果：", log)

    # 发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("邮件发送结果： ", res)

    # 退出
    smtp.quit()
    print("send email finish")
    '''
    注：
    
    将plain改为html标识邮件内容为html格式
    邮件内容采用html语言来格式化
    '''

    """
    下面看看如何发送带附件的邮件。 需要导入新的类，如下：

from email.mime.multipart import MIMEMultipart
需要使用MIMEMultipart构建内容结构，关键代码如下：

# 发送内容构建# html标识发送内容为文本格式
msg = MIMEMultipart()
msg["From"] = "deep_test@126.com"
msg["To"] = receivers

# 构建邮件标题
msg["Subject"] = Header("开源优测_DeepTest", "utf-8")

# 构建邮件正文内容
msg.attach(MIMEText("微信公众号：开源优测", "plain", "utf-8"))
# 构造附件,多个附件同理
attach1 = MIMEText(open("发送附件邮件.py", 'rb').read(), "base64", "utf-8")
attach1["Content-Type"] = "application/octet-stream"

# 这里filename随意写，将会在邮件中显示
attach1["Content-Disposition"] = "attrachment;filename=code.py"

# 关联附件到邮件中msg.attach(attach1)
    
    """
    '''
    
    
    
    print("发送HTML邮件示例")
    # 邮件发送者
    sender = "deep_test@126.com"

    # 邮件接收地址列表
    # 请将xxx改为你的126邮箱名或整个改为你的目标接收邮箱地址
    receivers = "xxx@126.com"

    # 发送内容构建
    # html标识发送内容为文本格式
    msg = MIMEMultipart()
    msg["From"] = "deep_test@126.com"
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("开源优测_DeepTest", "utf-8")

    # 构建邮件正文内容
    msg.attach(MIMEText("微信公众号：开源优测", "plain", "utf-8"))

    # 构造附件,多个附件同理
    attach1 = MIMEText(open("openpyxl.xlsx", 'rb').read(), "base64", "utf-8")
    attach1["Content-Type"] = "application/octet-stream"

    # 这里filename随意写，将会在邮件中显示
    attach1["Content-Disposition"] = "attrachment;filename=code.py"

    # 关联附件到邮件中
    msg.attach(attach1)

    # smtp服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    # 发送人邮件用户名或专用于smtp账户用户名
    username = "deep_test"

    # 发送人邮件密码或专用于smtp账户的密码
    password = "123456a"

    # 构建smtp对象
    smtp = smtplib.SMTP()

    # 连接到smtp服务
    con = smtp.connect(smtpserver, smtpport)
    print("连接结果： ", con)

    # 登录smtp服务
    log = smtp.login(username, password)

    print("登录结果：", log)

    # 发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())

    print("邮件发送结果： ", res)

    # 退出
    smtp.quit()

    print("send email finish")

    '''

    '''
    构建文本和html格式的邮件使用MIMEText构建，使用plain标识文本内容格式，使用html标识html内容格式

    对于附件格式则需使用MIMEMultipart
    
    '''
