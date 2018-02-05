# _*_ coding : utf-8 _*_
__author__ = "Jason"

'''
HTML格式邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ == "__main__":
    print("发送HTML邮件示例")

    sender = "deep_test@126.com"

    receivers = "472377371@qq.com"

    # 发送内容构建
    #html标识发送内容为文本格式
    msg = MIMEText("<p>微信公众号号：开源优测</p><a href = 'http://www.testingunion.com'>开源优测社区</a>",
                   "html",
                   "utf-8")
    msg["From"] = sender
    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("开源优测_DeepTest","utf-8")

    # smtp服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    username = "deep_test"
    password = "123456a"

    # 构建smtp对象
    smtp = smtplib.SMTP()

    # 链接到smtp服务
    con = smtp.connect(smtpserver,smtpport)
    print("连接结果：",con)

    #登录smtp服务
    log = smtp.login(username,password)
    print("登录结果：",log)

    #发送邮件
    print(receivers)
    res = smtp.sendmail(sender,receivers,msg.as_string())
    print("邮件发送结果：",res)

    #退出
    smtp.quit()
    print("send email finish")
