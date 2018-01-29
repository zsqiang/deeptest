import smtplib
from datetime import time
from email.mime.multipart import MIMEMultipart
from email.mime.nonmultipart import MIMENonMultipart
from email.mime.text import MIMEText
from email.header import Header

if __name__ == "__main__":
    print("发送文本邮件示例")

    # 邮件发送者
    # sender = "zhzxweijing@126.com"
    sender = "deep_test@126.com"
    # 邮件接收地址列表
    # 请将xxx改为你的126邮箱名或整个改为你的目标接收邮箱地址
    # receivers = "deep_test@126.com"
    receivers = sender
    msg = MIMEMultipart()

    # 发送内容构建
    # text标识发送内容为文本格式
    # msg = MIMEText("zoujielun：地表最强掩藏会", "plain", "utf-8")
    # msg=MIMENonMultipart(MIMEText( "<p>微信公众号号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>>", 'html', _charset="utf-8",  policy=None))

    # msg = MIMEText("<p>微信公众号号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>>",
    #                "html",
    #                "utf-8")

    msg.attach(MIMEText("zoujielun：地表最强掩藏会", "plain", "utf-8"))
    attch1 = MIMEText(open("books.csv", "rb").read(), "base64", "utf-8")
    attch1["Content-Type"] = "application/octet-stream"
    attch1["Content-Disposition"] = "attrachment;filename=test_smtp.py"
    msg.attach(attch1)

    # msg= MIMEText( "<p>微信公众号号：开源优测</p><a href='http://www.testingunion.com'>开源优测社区</a>>", _subtype='html', _charset="utf-8",  policy=None)



    msg["From"] = sender

    msg["To"] = receivers

    # 构建邮件标题
    msg["Subject"] = Header("yong_DeepTest", "utf-8")

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

    for i in range(1, 1000):
        res = smtp.sendmail(sender, receivers, msg.as_string(unixfrom=False, maxheaderlen=0, policy=None))
        import time
        # time.sleep(5)

    print("邮件发送结果： ", res)

    # 退出
    smtp.quit()
    print("send email finish")

    print(help(MIMEText))
