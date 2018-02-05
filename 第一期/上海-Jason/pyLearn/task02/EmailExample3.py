# _*_ coding : utf-8 _*_
__author__ = "Jason"

'''
附件格式邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

if __name__ == "__main__":
    print("发送HTML邮件示例")

    sender = "deep_test@126.com"

    receivers = "472377371@qq.com"

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receivers

    msg["Subject"] = Header("开源优测_DeepTest","utf-8")

    # 构建邮件正文内容
    msg.attach(MIMEText("微信公众号：开源优测","plain","utf-8"))

    # 构建邮件附件，多个附件同理
    attach1 = MIMEText(open("EmailExample.py","rb").read(),"base64","utf-8")

    # 这里filename随意写，将会在邮件中显示
    attach1["content_Disposition"] = "attachment;filename = code.py"

    # 关联附件到邮件中
    msg.attach(attach1)

    smtpserver = "smtp.126.com"
    smtpport = 25

    username = "deep_test"
    password = "123456a"

    smtp = smtplib.SMTP()

    con = smtp.connect(smtpserver,smtpport)
    print("连接结果：",con)

    log = smtp.login(username,password)
    print("登录结果：",log)

    print(receivers)
    res = smtp.sendmail(sender,receivers,msg.as_string())
    print("邮件发送结果：",res)

    smtp.quit()
    print("send email finish")