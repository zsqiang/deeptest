# _*_ coding : utf-8 _*_
__author__ = "Jason"

'''
概述
    主要介绍使用smtplib进行文本格式、HTML格式和带有附件的邮件发送处理。
导入smtplib模块
    import smtplib
关键函数说明
    创建SMTP对象
        smtp = smtplib。SMTP([host[,port[,loaclhost]]])
        参数说明
            host                smtp服务地址，例如126邮箱的是smtp.126.com
            port                smtp服务端口
            localhost           如果你的smtp服务在本地，则只需指定localhost即可
    发送邮件函数
        SMTP.sendmail(from_addr,to_addr,msg[,mail_options,rcpt_options])
        参数说明
            from_addr                       邮件发送地址
            to_addr                         邮件接收地址列表
            msg                             邮件内容
            mail_options,rcpt_options       可选参数
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ == "__main__":
    print("发送文本邮件示例")

    # 邮件发送者
    sender = "deep_test@126.com"

    # 邮件接收地址列表
    # 需改成自己所想要接收的地址
    receivers = "472377371@qq.com"

    # 发送内容构建
    # text标识发送内容为文本内容
    msg = MIMEText("微信公众号号：开源优测","plain","utf-8")
    msg["From"] = sender
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("开源优测_DeepTest","utf-8")

    # smtp服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    # 发送人邮箱用户名或专用于smtp账户用户名
    username = "deep_test"

    # 发送人邮箱密码或专用于smtp账户的密码
    password = "123456a"

    # 构建smtp对象
    smtp = smtplib.SMTP()

    # 连接到smtp服务
    con = smtp.connect(smtpserver,smtpport)
    print("连接结果：",con)

    # 登录smtp服务
    log = smtp.login(username,password)
    print("登录结果：",log)

    # 发送邮件
    print(receivers)
    res = smtp.sendmail(sender,receivers,msg.as_string())
    print("邮件发送结果：",res)

    #退出
    smtp.quit()
    print("send email finish")