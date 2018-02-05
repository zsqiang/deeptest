#coding = utf-8

__author__ = 'Aimee'

import smtplib

#创建smtp对象
# smtp = smtplib.SMTP([host [,port [,localhost]]])

# host： smtp服务地址，例如126邮箱的是：smtp.126.com
# port： smtp服务端口
# localhost： 如果你的smtp服务在本机，则只需指定localhost即可

# 发送邮件函数
# SMTP.sendmail(from_addr,to_addrs,msg[,mail_options,rcpt_options])

# from_addr： 邮件发送地址
# to_addrs： 邮件接收地址列表
# msg： 邮件内容
# mail_options, rcpt_options  可选参数，暂时不需要了解


import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ == "__main__":
    print("文本发送邮件")

    #邮件发送者
    sender = "aimee_hj@126.com"
    #邮件接收者
    receivers = "aimee_hj@126.com"

    #发送内容构建，text标识发送内容为文本格式
    # msg = MIMEText("微信公众号：Aimee的小屋","plain","utf-8")
    #html文件标识发送内容
    msg = MIMEText("<p>微信公众号号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>>","html","utf-8")

    msg["From"] = "aimee_hj@126.com"
    msg["To"] = receivers


    #构建邮件标题
    msg["Subject"] = Header("开源优测","utf-8")

    #smtp服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    #发送人账号密码
    username = "aimee_hj@126.com"
    password = "15179163344jj"

    #构建smtp对象
    smtp = smtplib.SMTP()

    #连接到smtp服务
    con = smtp.connect(smtpserver,smtpport)
    print("连接结果：",con)

    #登录smtp服务
    login = smtp.login(username,password)
    print("登录结果：",login)

    #发送邮件
    print(receivers)
    res = smtp.sendmail(sender,receivers,msg.as_string())
    print("发送邮件结果：",res)

    #退出
    smtp.quit()
    print("send email finish")






