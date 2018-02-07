#coding = utf-8

__author__ = 'Aimee'

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

if __name__ == "__main__":
    print("文本发送邮件")

    #邮件发送者
    sender = "aimee_hj@126.com"
    #邮件接收者
    receivers = "aimee_hj@126.com"

    #构建邮件的内容
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receivers

    #构建邮件标题
    msg["Subject"] = Header("开源优测","utf-8")

    #构建邮件正文
    msg.attach(MIMEText("aimee love testing","plain","utf-8"))

    #构造附件，多个附件同理

    attach1 = MIMEText( open("lesson13 smtp.py","rb").read(),"base64","utf-8")
    attach1["Content-Type"] = "application/octet-stream"

    # 这里filename随意写，将会在邮件中显示
    attach1["Content-Disposition"] = "attrachment;filename=code.py"
    # 关联附件到邮件中
    msg.attach(attach1)


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



    #三种格式 文本格式，html格式，附件格式