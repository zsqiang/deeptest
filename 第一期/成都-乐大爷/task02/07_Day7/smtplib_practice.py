# -*- coding:utf-8 -*-

__author__ = 'catleer'

import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def work_dir_change():

    path = __file__
    path_demo = os.path.dirname(path)
    os.chdir(path_demo)
    
def text_example():
    print("发送文本邮件示例")

    # 邮件发送者
    sender = "2114361817@qq.com"

    # 邮件接收地址
    receivers = "215486362@qq.com"

    # 发送内容构建
    # text标识发送内容为文本格式
    msg = MIMEText("微信公众号号：开源优测", "plain", "utf-8")
    msg["From"] = sender
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("开源优测_DeepTest", "utf-8")

    # smtp服务
    smtpserver = "smtp.qq.com"
    smtpport = 465

    # # 发送人邮件用户名或专用于smtp账户用户名
    username = "2114361817@qq.com"

    # 发送人邮件密码或专用于smtp账户的密码,用465端口密码要采用授权码
    password = "ntizzdhzaqodeeda"

    # 构建smtp对象
    smtp = smtplib.SMTP_SSL()

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

def html_example():
    print("发送html格式的邮件")

    sender = "2114361817@qq.com"
    receivers = "215486362@qq.com"

    # 邮箱服务器
    smtpserver = "smtp.qq.com"
    smtpport = 465

    # 邮件发送、接收人员，邮件标题、正文
    msg = MIMEText("<p>微信公众号号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>>", 
        "html", 
        "utf-8")
    msg["From"] = sender
    msg["To"] = receivers
    msg["Subject"] = Header("开源优测_DeepTest_from_chenlele", "utf-8")

    # 连接邮箱服务器
    username = "2114361817@qq.com"
    password = "ntizzdhzaqodeeda"
    smtp = smtplib.SMTP_SSL()
    smtp.connect(smtpserver, smtpport)
    smtp.login(username, password)
    
    # 发送邮件
    smtp.sendmail(sender, receivers, msg.as_string())

    # 退出
    smtp.quit()

from email.mime.multipart import MIMEMultipart

def attachment_example():
    print("发送附件格式的邮件示例")

    # 发送、接收人员
    sender = "2114361817@qq.com"
    receivers = "215486362@qq.com"

    # 邮件格式说明、发送、接收人员信息、邮件标题
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receivers
    msg["Subject"] = Header("开源优测_DeepTest_from_chenlele", "utf-8")

    # 构建带附件的邮件正文
    msg.attach(MIMEText("微信公众号：开源优测", "plain", "utf-8")) 
    
    # 构造附件,多个附件同理
    attach1 = MIMEText(open("简单excel写示例.xlsx", 'rb').read(), "base64", "utf-8")
    attach1["Content-Type"] = "application/octet-stream"

    # 这里filename随意写，将会在邮件中显示
    attach1["Content-Disposition"] = "attrachment;filename=code.py"
    
    # 关联附件到正文
    msg.attach(attach1)

    # smtp服务器信息
    smtpserver = "smtp.qq.com"
    smtpport = 465

    username = "2114361817@qq.com"
    password = "ntizzdhzaqodeeda"

    # 连接、登陆服务
    smtp = smtplib.SMTP_SSL()
    smtp.connect(smtpserver, smtpport)
    smtp.login(username, password)

    # 发送邮件
    smtp.sendmail(sender, receivers, msg.as_string())

    # 断开服务
    smtp.quit()

work_dir_change()
# text_example()
# html_example()
attachment_example()